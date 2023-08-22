from python.load_data import load_data, normalize_data
import itertools
import shutil
import datetime
import mlflow
from functools import partial
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from multiprocess import Pool, cpu_count
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

#############
# Filepaths #
data_dir = 'database/'
results_dir = 'results/'

############
# Function #


def delete_models(models_path):
    for item in os.listdir(models_path):
        item_path = os.path.join(models_path, item)
        shutil.rmtree(item_path)


def run_training(X_train, Y_train, X_test, Y_test, run_params):
    import mlflow
    from python.load_data import sequence_data, denormalize_data
    from python.lstm import create_model, train_model, predict_data, plot_loss
    from python.evaluate_model import compute_metrics
    with mlflow.start_run(run_name=f"run-{run_params['run_id']}", experiment_id=run_params['experiment_id']):
        # Sequencing
        sequence_length = run_params['P'] + run_params['Q']
        X_train, Y_train = sequence_data(
            X_train, Y_train, run_params['P'], run_params['Q'], run_params['H'])
        X_test, Y_test = sequence_data(
            X_test, Y_test, run_params['P'], run_params['Q'], run_params['H'])
        y_means = Y_test.mean(axis=0)
        y_stds = Y_test.std(axis=0)

        # Define model
        model = create_model(
            sequence_length, run_params['num_features_input'], run_params['num_features_output'], random_seed=42, summary=False)

        # Training
        model, history = train_model(
            model, X_train, Y_train, run_params['batch_size'], run_params["num_epochs"], run_params["validation_split"])

        # Prediction
        Y_pred = predict_data(model, X_test)
        for i in range(num_features_output):
            Y_pred[:, i] = denormalize_data(
                Y_pred[:, i], y_means[i], y_stds[i])  # Denormalize

            Y_test[:, i] = denormalize_data(
                Y_test[:, i], y_means[i], y_stds[i])  # Denormalize

        loss = compute_metrics(Y_test, Y_pred).mean()
        # Log params
        for key, value in run_params.items():
            mlflow.log_param(key, value)

        # Log metrics
        mlflow.log_metric("loss", loss)

        # Save model
        mlflow.keras.save_model(
            model, path=results_dir + f"models/run_{run_params['run_id']}")

        metrics = run_params
        metrics['loss'] = loss
    return metrics


# Load data
X_train, Y_train, X_test, Y_test = load_data(data_dir)
num_features_input = X_train.shape[1]
num_features_output = Y_train.shape[1]

# Slice to fit sequencing
X_train = X_train[:1000, :]
Y_train = Y_train[:1000, :]
X_test = X_test[:1000, :]
Y_test = Y_test[:1000, :]

Y_train = normalize_data(Y_train)
Y_test = normalize_data(Y_test)

# Remove previous models
delete_models(results_dir+'models/')

# set search space for hp's
hp_search_space = {
    'P': np.arange(5, 51, 5),
    'Q': np.arange(5, 51, 5),
    'H': [1],
    'batch_size': [16, 32, 64],
    'num_epochs': [25],
    'validation_split': [0.1]
}

hp_combinations = list(itertools.product(*hp_search_space.values()))

# Create study
experiment_name = f"LSTM_{datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S')}"
experiment = mlflow.create_experiment(experiment_name)

# iterate every combination
list_run_params = []
i = 1
for hp_comb in hp_combinations:
    run_params = {param_name: param_value for param_name,
                  param_value in zip(hp_search_space.keys(), hp_comb)}
    run_params['num_features_input'] = num_features_input
    run_params['num_features_output'] = num_features_output
    run_params['experiment_id'] = experiment
    run_params['run_id'] = i
    # print(f'Run: #{i}:, Params={run_params}')
    list_run_params.append(run_params)
    i += 1

num_processes = 2
with Pool(processes=num_processes) as pool:
    results = pool.starmap(run_training, [(X_train, Y_train, X_test, Y_test, run_params,)
                                          for run_params in list_run_params])
