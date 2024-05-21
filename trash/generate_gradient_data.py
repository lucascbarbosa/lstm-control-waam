import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tqdm import tqdm

import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
from models.process_data import (
    build_train_data,
    load_train_data,
    sequence_data,
    normalize_data,
)

# Data paths
data_dir = "database/"
results_dir = "results/"

#############
# Functions #


def build_sequence(u, y):
    """
    Build sequence input from history arrays

    Args:
        u (np.array): historical inputs
        y (np.array): historical outputs

    Returns:
        np.array: sequence input
    """
    num_features_input = u.shape[1]
    num_features_output = y.shape[1]
    u = u.ravel()
    y = y.ravel()
    return np.hstack((u, y)).reshape(
        (1, P * num_features_input + Q*num_features_output, 1)
    )


def update_hist(current_hist, new_states):
    """
    Updates history array

    Args:
        current_hist (np.array): current history array
        new_states (np.array): new elements to be added in the file

    Returns
        new_hist (np.array): updated history array
    """
    new_hist = current_hist.copy()
    len_new = new_states.shape[0]
    new_hist[:-len_new, :] = current_hist[len_new:, :]
    new_hist[-len_new:, :] = new_states
    return new_hist


def build_gradient_dataset(
    X_process, gradient_process, gradient_inputs, test_split
):
    """
    Builds gradient dataset

    Args:
        X_process (np.array): sequenced input from process data
        gradient_process (np.array): gradients of each input-output pair of process data
        gradient_inputs (np.array): pair input-output used to gradient dataset input
        test_split (float): percentage of dataset used to test

    Returns:
        input_train (np.array): inputs of train dataset
        output_train (np.array): outputs of train dataset
        input_test (np.array): inputs of test dataset
        output_test (np.array): outputs of test dataset
    """
    input_gradient = X_process[:, :gradient_inputs]
    output_gradient = gradient_process
    idx_split = int(N * (1 - test_split))
    input_train = input_gradient[:idx_split, :]
    input_test = input_gradient[idx_split:, :]
    output_train = output_gradient[:idx_split, :]
    output_test = output_gradient[idx_split:, :]

    return input_train, input_test, output_train, output_test


def split_gradient(grad):
    """Split gradient in the portion w.r.t. the inputs and outputs

    Args:
        grad (np.array): gradient of model

    Returns:
        input_gradient (np.array): gradient w.r.t. the inputs
        output_gradient (np.array): gradient w.r.t. the outputs
    """
    grad = grad.reshape((P * num_features_input + Q * num_features_output,))
    u = grad[: num_features_input * P].reshape((P, num_features_input))
    y = grad[num_features_input * P:].reshape((Q, num_features_output))
    return u[:, 0], y


# Process model parameters
metrics_process = pd.read_csv(
    results_dir + f"models/experiment/hp_metrics.csv"
)
best_model_id = 16
best_model_filename = f"run_{best_model_id:03d}.keras"
best_params = metrics_process[metrics_process["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

# Load model
model = load_model(
    results_dir + f"models/experiment/best/{best_model_filename}"
)
opt = Adam(learning_rate=best_params["lr"])
model.compile(optimizer=opt, loss=mean_squared_error)

# Load train and test data
input_train, output_train, input_test, output_test = load_train_data(
    data_dir + "experiment/calibration/"
)

input_train = input_train[:, 1:]
output_train = output_train[:, 1:]
input_test = input_test[:, 1:]
output_test = output_test[:, 1:]

u_min = input_train.min(axis=0)
u_max = input_train.max(axis=0)
y_min = output_train.min(axis=0)
y_max = output_train.max(axis=0)

num_features_input = input_train.shape[1]
num_features_output = output_train.shape[1]

# Scale database
input_train = normalize_data(input_train, u_min, u_max)
output_train = normalize_data(output_train, y_min, y_max)
input_test = normalize_data(input_test, u_min, u_max)
output_test = normalize_data(output_test, y_min, y_max)

X_train, Y_train = sequence_data(input_train, output_train, P, Q, 1)
X_train = X_train[max(P-1, Q):]
Y_train = Y_train[max(P-1, Q):]
X_test, Y_test = sequence_data(input_test, output_test, P, Q, 1)
X_test = X_test[max(P-1, Q):]
Y_test = Y_test[max(P-1, Q):]

gradient_train = []
gradient_test = []
for i in tqdm(range(len(X_train)), desc="Processing Train", unit="iteration"):
    seq_input_train = X_train[i:i+1, :, :]
    input_tensor = tf.convert_to_tensor(seq_input_train)
    for j in range(num_features_output):
        with tf.GradientTape() as t:
            t.watch(input_tensor)
            output_tensor = model(input_tensor)
            gradient = t.gradient(
                output_tensor[:, j], input_tensor
            ).numpy()[0, :, 0]
            seq_output = output_tensor.numpy()
            gradient, _ = split_gradient(gradient)
    gradient_train.append(gradient)

input_train = X_train[:, :, 0]
output_train = np.concatenate(gradient_train).reshape(
    (len(X_train), len(gradient)))
for i in tqdm(range(len(X_test)), desc="Processing Test", unit="iteration"):
    seq_input_test = X_test[i:i+1, :, :]
    input_tensor = tf.convert_to_tensor(seq_input_test)
    for j in range(num_features_output):
        with tf.GradientTape() as t:
            t.watch(input_tensor)
            output_tensor = model(input_tensor)
            gradient = t.gradient(
                output_tensor[:, j], input_tensor
            ).numpy()[0, :, 0]
            seq_output = output_tensor.numpy()
            gradient, _ = split_gradient(gradient)
    gradient_test.append(gradient)

input_test = X_test[:, :, 0]
output_test = np.concatenate(gradient_test).reshape(
    (len(X_test), len(gradient)))


np.savetxt(data_dir + "gradient/input_train.csv", input_train, delimiter=',')
np.savetxt(data_dir + "gradient/output_train.csv", output_train, delimiter=',')
np.savetxt(data_dir + "gradient/input_test.csv", input_test, delimiter=',')
np.savetxt(data_dir + "gradient/output_test.csv", output_test, delimiter=',')
