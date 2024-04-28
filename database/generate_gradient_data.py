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


# Functions
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


def split_gradient(seq):
    """Split gradient in the portion w.r.t. the inputs and outputs

    Args:
        seq (np.array): sequence input model

    Returns:
        input_gradient (np.array): gradient w.r.t. the inputs
        output_gradient (np.array): gradient w.r.t. the outputs
    """
    seq = seq.ravel()
    input_gradient = seq[: num_features_input * P]
    output_gradient = seq[num_features_input * P:]
    return input_gradient, output_gradient


# Process model parameters
metrics_process = pd.read_csv(
    results_dir + f"models/experiment/hp_metrics.csv"
)
best_model_id = 169
best_model_filename = f"run_{best_model_id:03d}.keras"
best_params = metrics_process[metrics_process["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

# Load model
process_model = load_model(
    results_dir + f"models/experiment/best/{best_model_filename}"
)
opt = Adam(learning_rate=best_params["lr"])
process_model.compile(optimizer=opt, loss=mean_squared_error)

beads_test = [3, 6, 10, 15]
beads_train = [1, 2, 4, 5, 7, 8, 9, 11, 12, 13, 14]

# Build input data
source = "experiment"
if source == "random":
    input_type = "step"  # or step
    N = 10_000
    if input_type == "cont":
        u_process = normalize_data(
            np.cumsum(
                np.random.normal(loc=0.0, scale=0.01,
                                 size=(N, num_features_input))
            ).reshape((N, num_features_input))
        )
    elif input_type == "step":
        num_steps = 51
        step_period = 50  # @ 5 Hz
        u_process = np.random.randint(
            0, num_steps, size=(int(N / step_period), num_features_input)
        ) / (num_steps - 1)
        u_process = np.repeat(u_process, step_period, axis=0)
    y_process = np.zeros((N, num_features_output))
    gradient_inputs = P * num_features_input + 3
    gradient_process = np.zeros((N, num_features_input * P))
    u_hist = np.zeros((P, num_features_input))
    y_hist = np.zeros((Q, num_features_output))
    for i in tqdm(range(N), desc="Processing", unit="iteration"):
        u_row = u_process[i]
        u_hist = update_hist(u_hist, u_row.reshape((1, num_features_input)))
        seq_input = build_sequence(u_hist, y_hist)
        input_tensor = tf.convert_to_tensor(seq_input, dtype=tf.float32)
        for j in range(1):
            with tf.GradientTape() as t:
                t.watch(input_tensor)
                output_tensor = process_model(input_tensor)
                gradient = t.gradient(
                    output_tensor[:, j], input_tensor
                ).numpy()[0, :, 0]
                gradient, _ = split_gradient(gradient)
                gradient_process[i, :] = gradient

        y_row = output_tensor.numpy()
        y_process[i] = y_row
        y_hist = update_hist(y_hist, y_row.reshape((1, 1)))

    X_process, Y_process = sequence_data(u_process, y_process, P, Q, 1)
    N = X_process.shape[0]
    gradient_process = gradient_process[-N:, :]
    X_process = X_process.reshape((X_process.shape[:2]))
    Y_process = Y_process.reshape((Y_process.shape[:2]))

elif source == "experiment":
    build_train_data(data_dir + "experiment/calibration/",
                     beads_train, beads_test)
    input_process, output_process, _, _ = load_train_data(
        data_dir + "experiment/calibration/"
    )

    input_process = input_process[:, 1:]
    output_process = output_process[:, 1:]

    num_features_input = input_process.shape[1]
    num_features_output = output_process.shape[1]

    # Scale database
    input_process = normalize_data(input_process)
    output_process = normalize_data(output_process)

    X_process, Y_process = sequence_data(
        input_process, output_process, P, Q, 1)
    N = X_process.shape[0]
    gradient_inputs = P * num_features_input + 3
    gradient_process = np.zeros((N, num_features_input * P))
    for i in tqdm(range(N), desc="Processing", unit="iteration"):
        input_tensor = tf.convert_to_tensor(
            X_process[i, :].reshape(
                (1, P * num_features_input + Q * num_features_output, 1)),
            dtype=tf.float32
        )
        for j in range(1):
            with tf.GradientTape() as t:
                t.watch(input_tensor)
                output_tensor = process_model(input_tensor)
                gradient = t.gradient(
                    output_tensor[:, j], input_tensor
                ).numpy()[0, :, 0]
                gradient, _ = split_gradient(gradient)
                gradient_process[i, :] = gradient

input_train, input_test, output_train, output_test = build_gradient_dataset(
    X_process, gradient_process, gradient_inputs, test_split=0.2
)

# Reshape
input_test = input_test[:, :, 0]
input_train = input_train[:, :, 0]

np.savetxt(
    data_dir + f"gradient/{source}/input_train.csv", input_train, delimiter=',')
np.savetxt(
    data_dir + f"gradient/{source}/input_test.csv", input_test, delimiter=',')
np.savetxt(
    data_dir + f"gradient/{source}/output_train.csv", output_train, delimiter=',')
np.savetxt(
    data_dir + f"gradient/{source}/output_test.csv", output_test, delimiter=',')

#
# plt.plot(u_process[:, 0], label="wfs")
# plt.plot(u_process[:, 1], label="ts")
# plt.plot(y_process, label="w")
# plt.legend()
# plt.show()
