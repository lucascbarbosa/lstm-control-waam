"""SINDY model script."""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from models.process_data import build_train_data, load_train_data
import control
from scipy.interpolate import interp1d

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


# Load data
wfs = pd.read_csv(data_dir + "experiment/series/bead1_wfs.csv").to_numpy()
command = pd.read_csv(
    data_dir + "experiment/series/bead1_command.csv").to_numpy()
command[:, 1] = pow2wfs(command[:, 1])
w = pd.read_csv(data_dir + "experiment/series/bead1_w.csv").to_numpy()

# Process data
T = 0.004  # Sampling period in seconds]
time = np.arange(wfs[0, 0], len(wfs)*T, T)
wfs_real = resample_data(wfs[:, 1], wfs[:, 0], time)
command_real = resample_data(command[:, 1], command[:, 0], time)
w_measured = resample_data(w[:, 1], w[:, 0], time)

# Create tf
numerator = [0, 0, 0.8]
denominator = [0.2, 1.2, 1]
G_continuous = control.TransferFunction(numerator, denominator)

# Discretize the transfer function using Tustin's method
G_discrete = control.sample_system(G_continuous, T, method='tustin')

# Convert to ss
ss_discrete = control.tf2ss(G_discrete)

# Generate output prediction
y_hat_wfs = np.zeros(w_measured.shape)
y_hat_command = np.zeros(w_measured.shape)

x_wfs_k = np.zeros((2, 1))
x_command_k = np.zeros((2, 1))
for i in range(1, len(y_hat_wfs)):
    # WFS value
    wfs_k = wfs_real[i]
    x_wfs_k = np.dot(ss_discrete.A, x_wfs_k) + np.dot(ss_discrete.B, wfs_k)
    y_hat_wfs[i] = np.dot(ss_discrete.C, x_wfs_k) + \
        np.dot(ss_discrete.D, wfs_k)

    # WFS command
    command_k = command_real[i]
    x_command_k = np.dot(ss_discrete.A, x_command_k) + \
        np.dot(ss_discrete.B, command_k)
    y_hat_command[i] = np.dot(ss_discrete.C, x_command_k) + \
        np.dot(ss_discrete.D, command_k)


# Plot results
fig, axs = plt.subplots(2, 1)
fig.set_size_inches((12, 10))

axs[0].set_title('Inputs')
axs[0].step(wfs[:, 0], wfs[:, 1], color='r', label='WFS value', where='post')
axs[0].step(command[:, 0], command[:, 1], color='b',
            label='WFS command', where='post')
axs[0].legend()
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Input')


axs[1].set_title('Outputs')
axs[1].plot(w_measured*1000, label='Measured width', color='k')
axs[1].plot(y_hat_wfs, label='Predicted width with WFS value',
            color='r', linestyle='--')
axs[1].plot(y_hat_command, label='Predicted width with WFS command',
            color='b', linestyle='--')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Output')
axs[1].legend()

plt.tight_layout()
plt.show()
