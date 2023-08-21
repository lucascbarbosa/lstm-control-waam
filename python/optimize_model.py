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


def objective(trial, X_train, Y_train, X_test, Y_test):
    with mlflow.start_run(run_name=f'trial-{trial.number+1}') as run:
        # Sequencing
        inputs_seq_len = trial.suggest_int("P", 5, 50, step=5)  # hp
        outputs_seq_len = trial.suggest_int("Q", 5, 50, step=5)  # hp
        forecast_h = 1  # hp
        # forecast_h = trial.suggest_int("H", 1, 10)  # hp
        sequence_length = inputs_seq_len + outputs_seq_len
        X_train, Y_train = sequence_data(
            X_train, Y_train, inputs_seq_len, outputs_seq_len, forecast_h)
        X_test, Y_test = sequence_data(
            X_test, Y_test, inputs_seq_len, outputs_seq_len, forecast_h)
        y_means = Y_test.mean(axis=0)
        y_stds = Y_test.std(axis=0)

        # Define model
        model = create_model(
            sequence_length, num_features_input, num_features_output)

        # Training
        batch_size = 2**5  # hp
        # batch_size = trial.suggest_int("batch_size", 4, 6)  # hp
        num_epochs = 25  # hp
        # num_epochs = trial.suggest_int("num_epochs", 20, 100, step=10)  # hp
        validation_split = 0.1   # hp
        # validation_split = trial.suggest_flot(
        #     "validation_split", 0.1, 0.3, step=0.02)  # hp
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
        # mlflow.log_param("H", trial.params["H"])
        mlflow.log_param("H", forecast_h)
        # mlflow.log_param("batch_size", trial.params["batch_size"])
        mlflow.log_param("batch_size", batch_size)
        mlflow.log_param("num_epochs", num_epochs)
        mlflow.log_param("validation_split", validation_split)

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

objective_with_params = partial(
    objective, X_train=X_train, Y_train=Y_train, X_test=X_test, Y_test=Y_test)

# Remove previous models
delete_models(results_dir+'models/')

# Create study
n_trials = 10
experiment_name = f"LSTM_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
experiment = mlflow.create_experiment(experiment_name)
study = optuna.create_study(study_name=experiment_name, direction="minimize")
study.optimize(objective_with_params, n_trials=n_trials)
for trial in study.trials:
    print(
        f"Trial #{trial.number+1}: Value={trial.value:.3f}, Params={trial.params}")

best_params = study.best_trial.params
