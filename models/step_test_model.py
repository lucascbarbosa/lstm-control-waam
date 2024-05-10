import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from models.process_data import sequence_data, load_train_data, normalize_data

import tensorflow
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam

from scipy.signal import find_peaks
from control import tf2ss
from pydmd import DMDc

import time
# Data paths
data_dir = "database/"
results_dir = "results/"

# Functions


def update_hist(current_hist, new_states):
    new_hist = current_hist.copy()
    len_new = new_states.shape[0]
    new_hist[:-len_new, :] = current_hist[len_new:, :]
    new_hist[-len_new:, :] = new_states
    return new_hist


def build_sequence():
    u = u_hist.ravel()
    y = y_hist.ravel()
    P = u_hist.shape[0]
    Q = y_hist.shape[0]
    sequence = np.hstack((u, y)).reshape(
        (1, P * process_inputs + Q * process_outputs, 1))
    return sequence


def compute_dmd(input_data, output_data, r=2):
    """
    Estimate the state-space matrices A, B, C, and D using DMD.

    Args:
    - X: Input snapshot matrix
    - Y: Output snapshot matrix
    - r: Number of DMD modes to compute

    Returns:
    - A: State matrix
    - B: Input matrix
    - C: Output matrix
    - D: Feedthrough matrix
    """
    # Convert to matrices
    X = np.vstack((output_data[:-1], output_data[1:]))
    U = input_data.T[:, :-2]

    dmdc = DMDc()
    dmdc.fit(X, U)

    Phi = dmdc.modes
    Lambda = np.diag(dmdc.eigs)
    A, B, C, D = calculate_state_space(Phi, Lambda, X, U)
    return A, B, C, D


def calculate_state_space(Phi, Lambda, X, U):

    # Calculate A matrix
    A = np.dot(np.dot(Phi, Lambda), np.linalg.pinv(Phi))

    # Calculate B matrix
    B = U[:, -2:].reshape((2, 1))

    C = np.array([[1, 0]])

    D = np.array([[0]])
    return A, B, C, D


# def compute_ss(output_data):
#     peaks, _ = find_peaks(output_data)
#     if len(peaks) > 1:
#         time_constant = time[peaks[1]] - time[peaks[0]]
#         overshoot = (output_data[peaks[0]] -
#                      output_data[-1]) / output_data[-1]
#         zeta = np.abs(np.log(overshoot)) / \
#             np.sqrt(np.pi**2 + np.log(overshoot)**2)
#         omega_n = 4 / (zeta * time_constant)
#         print(f"Zeta: {zeta} W_n: {omega_n}")
#
#         num = [[omega_n**2]]
#         den = [[1, 2*zeta*omega_n, omega_n**2]]
#         print(f"Num: {num} Den: {den}")
#
#         A, B, C, D = tf2ss(num, den)

def predict(input_data):
    output_data = np.zeros((input_data.shape[0]+1, 1))
    x = np.zeros((2, 1))
    for i in range(len(input_data)):
        u = input_data[i, :].reshape((2, 1))
        x = A @ x + B @ u


# Load data
(input_train,
 output_train,
 _,
 _) = load_train_data(data_dir + "experiment/calibration/")

input_train = input_train[:, 1:]
output_train = output_train[:, 1:]

u_min = input_train.min(axis=0)
u_max = input_train.max(axis=0)
y_min = output_train.min(axis=0)
y_max = output_train.max(axis=0)

process_inputs = input_train.shape[1]
process_outputs = output_train.shape[1]

# Model parameters
metrics = pd.read_csv(results_dir + f"models/experiment/hp_metrics.csv")
best_model_id = 16
best_model_filename = f"run_{best_model_id:03d}.keras"
best_params = metrics[metrics["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

# Load model
model = load_model(
    results_dir + f"models/experiment/best/{best_model_filename}"
)

opt = Adam(learning_rate=best_params["lr"])
model.compile(optimizer=opt, loss=mean_squared_error)

# Create steps
N = 50
T = 0.2
time = np.arange(0.0, N*T, T)
wfs_steps = np.arange(0.8, 1.1, 0.1)
ts_steps = np.arange(0.25, 1.1, 0.25)
for ts_step in ts_steps:
    for wfs_step in wfs_steps:
        input_data = np.zeros((N, process_inputs))
        input_data[:] = [wfs_step, ts_step]

        # Historic data
        u_hist = np.zeros((P, process_inputs))
        y_hist = np.zeros((Q, process_outputs))
        output_data = []
        for i in range(input_data.shape[0]):
            u = input_data[i]
            u_hist = update_hist(u_hist, u)
            input_seq = build_sequence()
            input_tensor = tensorflow.convert_to_tensor(
                input_seq, dtype=tensorflow.float32)
            y = model(input_tensor).numpy()
            y_hist = update_hist(y_hist, y)
            y_descaled = y[0, 0] * (y_max[0] - y_min[0]) + y_min[0]
            output_data.append(y[0, 0])

        input_data = input_data * (u_max - u_min) + u_min
        output_data = output_data * (y_max - y_min) + y_min

        print(f"WFS: {input_data[0,0]} TS: {input_data[0,1]}")

        # A, B, C, D = compute_ss(output_data)

        A, B, C, D = compute_dmd(input_data[:, :1], output_data)
        predict_output(input_data)
        # plt.plot(input_data[:, 0], label='WFS (mm/min)')
        # plt.plot(input_data[:, 1], label='TS (mm/s)')
        # plt.plot(output_data, label='Width (mm)')
        # plt.legend()
        # plt.tight_layout()
        # plt.show()
