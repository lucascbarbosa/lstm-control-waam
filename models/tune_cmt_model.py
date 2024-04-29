from scipy.optimize import minimize
from scipy.interpolate import interp1d
import control
from models.process_data import build_train_data, load_train_data
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#############
# Filepaths #
data_dir = "database/"
results_dir = "results/"

# Load database
beads_train = [1]
beads_test = [1]

#############
# Functions #


def pow2wfs(p):
    return 0.09*p + 1.5


def split_data(data):
    list_data = []
    time = data[:, 0]
    start_idxs = np.concatenate(
        ([0], np.where(np.diff(time) < 0)[0] + 1, [len(data)]))
    for i in range(len(start_idxs)-1):
        list_data.append(data[start_idxs[i]:start_idxs[i+1], :])
    return list_data


def create_ss(numerator, denominator):
    G_continuous = control.TransferFunction(numerator, denominator)

    # Discretize the transfer function using Tustin's method
    G_discrete = control.sample_system(G_continuous, T, method='tustin')

    # Convert to ss
    ss_discrete = control.tf2ss(G_discrete)

    return ss_discrete


def predict_data(ss_discrete, u, y_real):
    y_pred = np.zeros(y_real.shape)
    x_k = np.zeros((2, 1))
    for i in range(1, len(y_pred)):
        u_k = u[i]
        x_k = np.dot(ss_discrete.A, x_k) + np.dot(ss_discrete.B, u_k)
        y_pred[i] = np.dot(ss_discrete.C, x_k) + \
            np.dot(ss_discrete.D, u_k)
    return y_pred


def compute_metrics(gain, u_real, y_real):
    numerator = [0, 0, gain[0]]
    ss_discrete = create_ss(numerator, denominator)
    y_pred = predict_data(ss_discrete, u_real, y_real)
    return np.sum((y_pred-y_real)**2)


def resample_data(original_data, original_time, new_time):
    """
    Resample dataset given the original and resampled time points

    Args:
        original_data (np.array): original dataset
        original_time (np.array): original dataset time points
        new_time (np.array): resampled time points

    Returns:
        resampled_data (np.array): resampled dataset
    """
    interp_func = interp1d(
        original_time,
        original_data,
        kind="linear",
        fill_value="extrapolate",
    )

    resampled_data = interp_func(new_time)
    return resampled_data


# Load database
beads_test = [3, 6, 10, 15]
beads_train = [1, 2, 4, 5, 7, 8, 9, 11, 12, 13, 14]
build_train_data(data_dir + "experiment/calibration/", beads_train, beads_test)
input_train, output_train, input_test, output_test = load_train_data(
    data_dir + "experiment/calibration/"
)

# Load data
time = input_train[:, 0]
u_train = input_train[:, 1]
y_train = output_train[:, 1]

# Constant
T = 0.02
denominator = [0.2, 1.2, 1]

# Optimization
initial_gain = 1.0

# Minimize MSE function to optimize parameters
result = minimize(compute_metrics, initial_gain, args=(u_train, y_train))

# Extract optimized parameters
gain_opt = result.x.round(2)[0]
num_opt = [0, 0, gain_opt]
ss_opt = create_ss(num_opt, denominator)


inputs_test = split_data(input_test)
outputs_test = split_data(output_test)
for bead_test, input_test, output_test in zip(
        beads_test, inputs_test, outputs_test):

    time = input_test[:, 0]
    u_real = input_test[:, 1]
    y_real = output_test[:, 1]
    # Generate output prediction
    y_pred = predict_data(ss_opt, u_real, y_real)

    # Plot results
    fig = plt.figure(figsize=(12, 6))
    plt.title('Outputs')
    plt.plot(time, y_real, label='Measured width', color='k')
    plt.plot(time, y_pred, label='Predicted width with WFS value',
             color='r', linestyle='--')
    plt.xlabel('Time')
    plt.ylabel('Output')
    plt.legend()

    plt.tight_layout()
    plt.savefig(
        results_dir + f'plots/experiment/calibration/calibration_bead{bead_test}_tf_prediction.png')
    plt.show()
