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
lag = 1.25
time = np.arange(wfs[0, 0], len(wfs)*T, T)
wfs_real = resample_data(wfs[:, 1], wfs[:, 0], time)
wfs_real = np.concatenate((np.zeros(int(lag/T)), wfs_real[:-int(lag/T)]))
command_real = resample_data(command[:, 1], command[:, 0], time)
command_real = np.concatenate(
    (np.zeros(int(lag/T)), command_real[:-int(lag/T)]))
w_measured = resample_data(w[:, 1], w[:, 0], time)

# Create tf
numerator = [0, 0, 0.8]
denominator = [0.2, 1.2, 1]
G_continuous = control.TransferFunction(numerator, denominator)

# Discretize the transfer function using Tustin's method
G_discrete = control.sample_system(G_continuous, T, method='tustin')
y_hat_wfs = control.forced_response(
    G_discrete, T=time, U=wfs_real)[1][int(lag/T):]
y_hat_command = control.forced_response(
    G_discrete, T=time, U=command_real)[1][int(lag/T):]

fig, axs = plt.subplots(2, 1)
fig.set_size_inches((12, 10))

axs[0].set_title('Inputs')
axs[0].step(wfs[:, 0], wfs[:, 1], color='r', label='WFS', where='post')
axs[0].step(command[:, 0], command[:, 1], color='b',
            label='command', where='post')
axs[0].legend()
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Input')


axs[1].set_title('Outputs')
axs[1].plot(w_measured*1000, label='Measured width', color='k')
axs[1].plot(y_hat_wfs, label='Predicted width with wfs',
            color='r', linestyle='--')
axs[1].plot(y_hat_command, label='Predicted width with command',
            color='b', linestyle='--')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Output')
axs[1].legend()

plt.tight_layout()
plt.show()
