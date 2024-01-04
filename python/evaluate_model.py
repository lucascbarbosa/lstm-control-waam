from python.process_data import (
    load_simulation,
    load_experiment,
    load_mpc,
    sequence_data,
    standardize_data,
    normalize_data,
    destandardize_data,
    denormalize_data,
)
from python.lstm import predict_data

import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import mean_squared_error

import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load data
data_dir = "database/"
results_dir = "results/"

def compute_metrics(Y_pred, Y_real):
    mses = []
    error = Y_pred - Y_real
    sq_error = error**2
    mses = np.mean(sq_error, axis=0)
    return mses

source = "experiment"
input_scaling = "min-max"
output_scaling = "min-max"

# Load metrics
best_model_id = 33
best_model_filename = f"run_{best_model_id:03d}.keras"
metrics_df = pd.read_csv(results_dir + f"models/{source}/hp_metrics.csv")
best_params = metrics_df[metrics_df["run_id"] == int(best_model_id)]

# Load best model
model = load_model(results_dir + f"models/{source}/best/{best_model_filename}")
model.compile(
    optimizer=Adam(learning_rate=best_params["lr"]), loss=mean_squared_error
)

# Load and sequence data accordingly
if source == "simulation":
    _, _, inputs_test, outputs_test = load_simulation(
        data_dir + f"{source}/"
    )
    y_means = outputs_test.mean(axis=0)
    y_stds = outputs_test.std(axis=0)

    # Scale database
    inputs_test = normalize_data(inputs_test)
    outputs_test = standardize_data(outputs_test)
    num_features_input = inputs_test.shape[1]
    num_features_output = outputs_test.shape[1]

    # Slice to fit sequencing
    inputs_test = inputs_test[:1000, :]
    outputs_test = outputs_test[:1000, :]

    # Sequence data
    X_real, Y_real = sequence_data(
        inputs_test,
        outputs_test,
        int(best_params["P"]),
        int(best_params["Q"]),
        int(best_params["H"]),
    )

    # Prediction
    Y_pred = predict_data(model, X_real)
    for i in range(num_features_output):
        Y_pred[:, i] = destandardize_data(
            Y_pred[:, i], y_means[i], y_stds[i]
        )  # Destandardize

        Y_real[:, i] = destandardize_data(
            Y_real[:, i], y_means[i], y_stds[i]
        )  # Destandardize

    np.savetxt(results_dir + "predictions/simulation/y_real.csv", Y_real)
    np.savetxt(results_dir + "predictions/simulation/y_pred.csv", Y_pred)

    mses = compute_metrics(Y_pred, Y_real)
    print(f"MSE: we={mses[0]:.3f} h={mses[1]:.3f}")

elif source == "experiment":
    for idx_test in range(7,8):
        _, output_train, input_test, output_test = load_experiment(
            data_dir + f"{source}/", [1, 2, 3, 4, 5, 6], [idx_test]
        )
        num_features_input = 1
        num_features_output = 1

        # Scale database
        if input_scaling == "mean-std":
            input_train = standardize_data(input_train)
            input_test = standardize_data(input_test)

        elif input_scaling == "min-max":
            input_train = normalize_data(input_train)
            input_test = normalize_data(input_test)

        if output_scaling == "mean-std":
            train_y_stds = output_train.std(axis=0)
            train_y_means = output_train.mean(axis=0)
            test_y_stds = output_test.std(axis=0)
            test_y_means = output_test.mean(axis=0)
            output_train = standardize_data(output_train)
            output_test = standardize_data(output_test)

        elif output_scaling == "min-max":
            train_y_mins = output_train.min(axis=0)
            train_y_maxs = output_train.max(axis=0)
            test_y_mins = output_test.min(axis=0)
            test_y_maxs = output_test.max(axis=0)
            output_train = normalize_data(output_train)
            output_test = normalize_data(output_test)

        # Sequence data
        X_real, Y_real = sequence_data(
            input_test,
            output_test,
            int(best_params["P"]),
            int(best_params["Q"]),
            int(best_params["H"]),
        )

        # Prediction
        Y_pred = predict_data(model, X_real)
        for i in range(num_features_output):
            if output_scaling == "mean-std":
                Y_pred[:, i] = destandardize_data(
                    Y_pred[:, i], train_y_means[i], train_y_stds[i]
                )  # Destandardize

                Y_real[:, i] = destandardize_data(
                    Y_real[:, i], test_y_means[i], test_y_stds[i]
                )  # Destandardize

            elif output_scaling == "min-max":
                Y_pred[:, i] = denormalize_data(
                    Y_pred[:, i], train_y_mins[i], train_y_maxs[i]
                )  # Denormalize

                Y_real[:, i] = denormalize_data(
                    Y_real[:, i], test_y_mins[i], test_y_maxs[i]
                )  # Denormalize
        # Save real and predicted data
        np.savetxt(results_dir + f"predictions/experiment/bead{idx_test}_y_real.csv", Y_real)
        np.savetxt(results_dir + f"predictions/experiment/bead{idx_test}_y_pred.csv", Y_pred)

        mse = compute_metrics(Y_pred, Y_real)
        print(f"MSE for bead {idx_test}: we={mse[0]:.3f}")

elif source == "mpc":
    input_train, output_train, input_test, output_test = load_mpc(data_dir + f"{source}/")

    num_features_input = 1
    num_features_output = 1

    # Convert output to error (r-y)
    input_train = input_train.mean(axis=0)[0] - input_train
    input_test = input_test.mean(axis=0)[0] - input_test

    # Scale database
    if input_scaling == "mean-std":
        input_train = standardize_data(input_train)
        input_test = standardize_data(input_test)
    elif input_scaling == "min-max":
        input_train = normalize_data(input_train)
        input_test = normalize_data(input_test)

    if output_scaling == "mean-std":
        train_y_stds = output_train.std(axis=0)
        train_y_means = output_train.mean(axis=0)
        test_y_stds = output_test.std(axis=0)
        test_y_means = output_test.mean(axis=0)
        output_train = standardize_data(output_train)
        output_test = standardize_data(output_test)

    elif output_scaling == "min-max":
        train_y_mins = output_train.min(axis=0)
        train_y_maxs = output_train.max(axis=0)
        test_y_mins = output_test.min(axis=0)
        test_y_maxs = output_test.max(axis=0)
        output_train = normalize_data(output_train)
        output_test = normalize_data(output_test)

    # Sequence data
    X_real, Y_real = sequence_data(
        input_test,
        output_test,
        int(best_params["P"]),
        int(best_params["Q"]),
        int(best_params["H"]),
    )
    # Prediction
    Y_pred = predict_data(model, X_real)
    for i in range(num_features_output):
        if output_scaling == "mean-std":
            Y_pred[:, i] = destandardize_data(
                Y_pred[:, i], train_y_means[i], train_y_stds[i]
            )  # Destandardize

            Y_real[:, i] = destandardize_data(
                Y_real[:, i], test_y_means[i], test_y_stds[i]
            )  # Destandardize
        elif output_scaling == "min-max":
            Y_pred[:, i] = denormalize_data(
                Y_pred[:, i], train_y_mins[i], train_y_maxs[i]
            )  # Denormalize

            Y_real[:, i] = denormalize_data(
                Y_real[:, i], test_y_mins[i], test_y_maxs[i]
            )  # Denormalize
    
    mse = compute_metrics(Y_pred, Y_real)
    print(f"MSE for we={mse[0]:.3f}")

    np.savetxt(results_dir + f"predictions/mpc/u_real.csv", Y_real)
    np.savetxt(results_dir + f"predictions/mpc/u_pred.csv", Y_pred)