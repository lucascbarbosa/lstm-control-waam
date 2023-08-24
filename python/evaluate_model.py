from python.process_data import (
    load_data,
    sequence_data,
    normalize_data,
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


# Load metrics
metrics_df = pd.read_csv(results_dir + "models/hp_metrics.csv")
best_model_id = metrics_df.iloc[0, 0]
best_model_filename = os.listdir(results_dir + "models/best/")[0]
best_params = metrics_df.iloc[0, 1:]
# Load best model
model = load_model(results_dir + "models/best/" + best_model_filename)
model.compile(
    optimizer=Adam(learning_rate=best_params["lr"]), loss=mean_squared_error
)

# Load and sequence data accordingly
_, _, X_test, Y_test = load_data(data_dir)
num_features_input = X_test.shape[1]
num_features_output = Y_test.shape[1]

# Slice to fit sequencing
X_test = X_test[:1000, :]
Y_test = Y_test[:1000, :]

Y_test = normalize_data(Y_test)

X_real, Y_real = sequence_data(
    X_test,
    Y_test,
    int(best_params["P"]),
    int(best_params["Q"]),
    int(best_params["H"]),
)
y_means = Y_test.mean(axis=0)
y_stds = Y_test.std(axis=0)

# Prediction
Y_pred = predict_data(model, X_real)
for i in range(num_features_output):
    Y_pred[:, i] = denormalize_data(
        Y_pred[:, i], y_means[i], y_stds[i]
    )  # Denormalize

    Y_test[:, i] = denormalize_data(
        Y_test[:, i], y_means[i], y_stds[i]
    )  # Denormalize

# # Cutout the first P+Q elements
# Y_real = Y_real[int(best_params["P"]) + int(best_params["Q"]) :]

# Save real and predicted data
np.savetxt(results_dir + "predictions/y_real.csv", Y_real)
np.savetxt(results_dir + "predictions/y_pred.csv", Y_pred)

mses = compute_metrics(Y_pred, Y_real)
print(f"MSE: we={mses[0]:.3f} h={mses[1]:.3f}")

bins = 32
# histogram_error(Y_pred, Y_real, 32)
