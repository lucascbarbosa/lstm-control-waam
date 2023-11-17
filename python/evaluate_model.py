from python.process_data import (
    load_simulation,
    load_experiment,
    sequence_data,
    standardize_data,
    normalize_data,
    destandardize_data,
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
source = "experiment"


def compute_metrics(Y_pred, Y_real):
    mses = []
    error = Y_pred - Y_real
    sq_error = error**2
    mses = np.mean(sq_error, axis=0)
    return mses


# Load metrics
best_model_id = 281
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
    _, outputs_train, inputs_test, outputs_test = load_simulation(
        data_dir + f"{source}/"
    )
    y_means = outputs_train.mean(axis=0)
    y_stds = outputs_train.std(axis=0)

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
    for idx_test in range(2,8):

        _, output_train, input_test, output_test = load_experiment(
            data_dir + f"{source}/", 1, idx_test
        )
        y_mean = output_train.mean().reshape((1,))
        y_std = output_train.std().reshape((1,))

        # Scale database
        input_test = normalize_data(input_test)
        output_test = standardize_data(output_test)
        num_features_input = 1
        num_features_output = 1

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
        Y_pred[:, 0] = destandardize_data(
            Y_pred[:, 0], y_mean, y_std
        )  # Destandardize

        Y_real[:, 0] = destandardize_data(
            Y_real[:, 0], y_mean, y_std
        )  # Destandardize

        # Cutout the first P+Q elements
        # Y_real = Y_real[int(best_params["P"]) + int(best_params["Q"]) :]

        # Save real and predicted data
        
        np.savetxt(results_dir + f"predictions/experiment/bead{idx_test}_y_real.csv", Y_real)
        np.savetxt(results_dir + f"predictions/experiment/bead{idx_test}_y_pred.csv", Y_pred)

        mses = compute_metrics(Y_pred, Y_real)
        print(f"MSE for bead {idx_test}: we={mses[0]:.3f}")