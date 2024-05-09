import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from models.process_data import sequence_data, load_train_data, normalize_data

import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam

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
N = 500
ts = 8.0
ts_scaled = (ts - u_min[1]) / (u_max[1] - u_min[1])
input_data = np.zeros((N, process_inputs))
input_data[:100, :] = [0.2, ts_scaled]
input_data[100:20, :] = [0.6, ts_scaled]
input_data[200:300, :] = [0.4, ts_scaled]
input_data[300:400, :] = [0.8, ts_scaled]
input_data[400:, :] = [1.0, ts_scaled]

# Historic data
u_hist = np.zeros((P, process_inputs))
y_hist = np.zeros((Q, process_outputs))
output_data = []
for i in range(input_data.shape[0]):
    u = input_data[i]
    u_hist = update_hist(u_hist, u)
    input_seq = build_sequence()
    input_tensor = tf.convert_to_tensor(input_seq, dtype=tf.float32)
    y = model(input_tensor).numpy()
    y_hist = update_hist(y_hist, y)
    y_descaled = y[0, 0] * (y_max[0] - y_min[0]) + y_min[0]
    output_data.append(y[0, 0])

input_data = input_data * (u_max - u_min) + u_min
output_data = output_data * (y_max - y_min) + y_min
plt.plot(input_data[:, 0], label='input')
plt.plot(output_data, label='output')
plt.legend()
plt.tight_layout()
plt.show()
