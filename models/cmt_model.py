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


build_train_data(data_dir + "experiment/", beads_train, beads_test)
input_train, output_train, input_test, output_test = load_train_data(
    data_dir + "experiment/"
)
T = 0.02  # Sampling period in seconds]
lag = 1.25
time = np.arange(input_train[0, 0], len(input_train)*T, T)
u_real = resample_data(input_train[:, 1], input_train[:, 0], time)
u_real = np.concatenate((np.zeros(int(lag/T)), u_real[:-int(lag/T)]))
y_real = resample_data(output_train[:, 1], output_train[:, 0], time)

# Create tf
numerator = [0, 0, 0.8]
denominator = [0.2, 1.2, 1]
G_continuous = control.TransferFunction(numerator, denominator)

# Discretize the transfer function using Tustin's method
G_discrete = control.sample_system(G_continuous, T, method='tustin')
y_hat = control.forced_response(G_discrete, T=time, U=u_real)[1][int(lag/T):]

plt.plot(y_real*1000, label='Real Output')
plt.plot(y_hat, label='Predicted Output')
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Comparison of Real and Predicted Outputs')
plt.legend()
plt.show()
