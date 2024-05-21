import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam

from models.process_data import load_train_data
import pandas as pd
import numpy as np
import time

# Paths
data_dir = "database/"
results_dir = "results/"

# Load process data
(process_input_train,
 process_output_train,
 _,
 _) = load_train_data(data_dir + "experiment/calibration/")

process_input_train = process_input_train[:, 1:]
process_output_train = process_output_train[:, 1:]

process_u_min = process_input_train.min(axis=0)
process_u_max = process_input_train.max(axis=0)
process_y_min = process_output_train.min(axis=0)
process_y_max = process_output_train.max(axis=0)

process_inputs = process_input_train.shape[1]
process_outputs = process_output_train.shape[1]

# Load process model
metrics_process = pd.read_csv(results_dir +
                              f"models/experiment/hp_metrics.csv"
                              )
best_process_model_id = 2
best_process_model_filename = f"run_{best_process_model_id:03d}.keras"
best_params = metrics_process[
    metrics_process["run_id"] == int(best_process_model_id)
]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

process_model = load_model(
    results_dir +
    f"models/experiment/best/{best_process_model_filename}"
)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


# Define your new input observation
# Replace this with your actual observation
new_observation = np.random.rand(
    1, process_inputs * P + process_outputs * Q, 1)

time0 = time.time()

# Extract the weights for each layer
lstm_kernel, lstm_recurrent_kernel, lstm_bias = process_model.layers[0].weights
dense_kernel, dense_bias = process_model.layers[1].weights

for i in range(P):
    # LSTM layer computations
    h_tm1 = np.zeros((1, 64))  # Initial hidden state
    c_tm1 = np.zeros((1, 64))  # Initial cell state
    for t in range(new_observation.shape[1]):
        x_t = new_observation[:, t, :]  # Current input at time step t
        z = np.dot(x_t, lstm_kernel) + np.dot(h_tm1,
                                              lstm_recurrent_kernel) + lstm_bias
        i, f, c, o = np.split(z, 4, axis=-1)
        i = sigmoid(i)
        f = sigmoid(f)
        c = relu(c)
        o = sigmoid(o)
        c = f * c_tm1 + i * c
        h = o * relu(c)  # Using ReLU activation for the LSTM units
        h_tm1 = h
        c_tm1 = c

    # Dense layer computation
    output = h @ dense_kernel + dense_bias
time1 = time.time()
print(f"Predicted value math: {output.numpy()[0, 0]} in {time1- time0} s")
for i in range(P):
    output = process_model(new_observation).numpy()[0, 0]
time2 = time.time()
print(f"Predicted value NN: {output} in {time2 - time1} s")
