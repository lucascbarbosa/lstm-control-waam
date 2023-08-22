import shutil
import datetime
import mlflow.tensorflow
import mlflow
import optuna
from load_data import load_data, normalize_data, sequence_data, denormalize_data
from LSTM import create_model, train_model, predict_data, plot_loss
from evaluate_model import compute_metrics
from functools import partial
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

#############
# Filepaths #
data_dir = 'C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/database/'
results_dir = 'C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/results/'

############
# Function #


def delete_models(models_path):
    for item in os.listdir(models_path):
        item_path = os.path.join(models_path, item)
        shutil.rmtree(item_path)


def objective(trial, X_train, Y_train, X_test, Y_test, hp_search_space):
    with mlflow.start_run(run_name=f'trial-{trial.number+1}') as run:
        # Sequencing
        inputs_seq_len = trial.suggest_categorical(
            "P", hp_search_space["P"])  # hp
        outputs_seq_len = trial.suggest_categorical(
            "Q", hp_search_space["Q"])  # hp
        forecast_h = trial.suggest_categorical("H", hp_search_space["H"])  # hp
        sequence_length = inputs_seq_len + outputs_seq_len
        X_train, Y_train = sequence_data(
            X_train, Y_train, inputs_seq_len, outputs_seq_len, forecast_h)
        X_test, Y_test = sequence_data(
            X_test, Y_test, inputs_seq_len, outputs_seq_len, forecast_h)
        y_means = Y_test.mean(axis=0)
        y_stds = Y_test.std(axis=0)

        # Define model
        model = create_model(
            sequence_length, num_features_input, num_features_output, random_seed=42, summary=False)

        # Training
        batch_size = trial.suggest_categorical(
            "batch_size", hp_search_space["batch_size"])  # hp
        num_epochs = trial.suggest_categorical(
            "num_epochs", hp_search_space["num_epochs"])  # hp
        validation_split = trial.suggest_categorical(
            "validation_split", hp_search_space["validation_split"])  # hp
        model, history = train_model(
            model, X_train, Y_train, batch_size, num_epochs, validation_split)

        # Prediction
        Y_pred = predict_data(model, X_test)
        for i in range(num_features_output):
            Y_pred[:, i] = denormalize_data(
                Y_pred[:, i], y_means[i], y_stds[i])  # Denormalize

            Y_test[:, i] = denormalize_data(
                Y_test[:, i], y_means[i], y_stds[i])  # Denormalize

        loss = compute_metrics(Y_test, Y_pred).mean()
        mlflow.log_param("P", trial.params["P"])
        mlflow.log_param("Q", trial.params["Q"])
        mlflow.log_param("H", trial.params["H"])
        mlflow.log_param("batch_size", trial.params["batch_size"])
        mlflow.log_param("num_epochs", trial.params["num_epochs"])
        mlflow.log_param("validation_split", trial.params["validation_split"])

        mlflow.log_metric("loss", loss)

        mlflow.keras.save_model(
            model, path=results_dir + f"models/trial_{trial.number+1}")
    return loss


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

# set which hyperparameters will be tuned

hp_search_space = {
    'P': np.arange(5, 51, 5),
    'Q': np.arange(5, 51, 5),
    'H': [1],
    'batch_size': [16, 32, 64],
    'num_epochs': [25],
    'validation_split': [0.1]
}

objective_with_params = partial(
    objective, X_train=X_train, Y_train=Y_train, X_test=X_test, Y_test=Y_test, hp_search_space=hp_search_space)

# Remove previous models
delete_models(results_dir+'models/')

# Create study
n_trials = 100
experiment_name = f"LSTM_{datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S')}"
experiment = mlflow.create_experiment(experiment_name)
study = optuna.create_study(study_name=experiment_name, direction="minimize",
                            sampler=optuna.samplers.GridSampler(hp_search_space))
study.optimize(objective_with_params, n_trials=n_trials)
for trial in study.trials:
    print(
        f"Trial #{trial.number+ 1}: Value={trial.value:.3f}, Params={trial.params}")

best_params = study.best_trial.params
best_id = study.best_trial.number + 1
