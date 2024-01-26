import numpy as np
import pandas as pd
from tqdm import tqdm

import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
from python.process_data import (sequence_data, 
                                 normalize_data, 
                                 standardize_data,
                                 load_experiment)

# Data paths
data_dir = "database/"
results_dir = "results/"

# Functions
def build_sequence(u, y):
    u = u.ravel()
    y = y.ravel()
    return np.hstack((u, y)).reshape((1, P + Q, 1))

def update_hist(current_hist, new_states):
    new_hist = current_hist.copy()
    len_new = new_states.shape[0]
    new_hist[:-len_new, :] = current_hist[len_new:, :]
    new_hist[-len_new:, :] = new_states
    return new_hist

def build_gradient_dataset(X_process, gradient_process, gradient_inputs, test_split):
    input_gradient = X_process[:, :gradient_inputs]
    output_gradient = gradient_process
    idx_split = int(N * (1-test_split))
    input_train = input_gradient[:idx_split, :]
    input_test = input_gradient[idx_split:, :]
    output_train = output_gradient[:idx_split, :]
    output_test = output_gradient[idx_split:, :]

    return input_train, input_test, output_train, output_test

def split_gradient(seq):
    seq = seq.ravel()
    input_gradient = seq[: 1 * P]
    return input_gradient

# Process model parameters
metrics_process = pd.read_csv(results_dir + f"models/experiment_igor/hp_metrics.csv")
best_model_id = 121
best_model_filename = f"run_{best_model_id:03d}.keras"
best_params = metrics_process[metrics_process["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

# Load model
process_model = load_model(
    results_dir + f"models/experiment_igor/best/{best_model_filename}"
)
opt = Adam(learning_rate=best_params["lr"])
process_model.compile(optimizer=opt, loss=mean_squared_error)

# Build input data
source = "random" ##
if source == "random":
    process_inputs = 1
    process_outputs = 1
    input_type = "step" # or step
    N = 10_000
    if input_type == "cont":
        u_process = normalize_data(
            np.cumsum(
                np.random.normal(loc=0.0, scale=0.01, size=(N, process_inputs)
                                )
                ).reshape((N, process_inputs))
            )
    elif input_type == "step":
        num_steps = 51
        step_period = 25 # @ 10 Hz
        u_process = np.random.randint(0, num_steps, 
                                      size=(int(N/step_period), process_inputs)) / (num_steps - 1)
        u_process = np.repeat(u_process, step_period, axis=0)
    y_process = np.zeros((N, process_inputs))
    gradient_inputs = P + 3
    gradient_process = np.zeros((N, P))
    u_hist = np.zeros((P, process_inputs))
    y_hist = np.zeros((Q, process_outputs))
    for i in tqdm(range(N), desc='Processing', unit='iteration'):
        u_row = u_process[i]
        u_hist = update_hist(u_hist, u_row.reshape((1, 1)))
        seq_input = build_sequence(u_hist, y_hist)
        input_tensor = tf.convert_to_tensor(seq_input, dtype=tf.float32)
        for j in range(1):
            with tf.GradientTape() as t:
                t.watch(input_tensor)
                output_tensor = process_model(input_tensor)
                gradient = t.gradient(
                    output_tensor[:, j], input_tensor
                ).numpy()[0, :, 0]
                gradient = split_gradient(gradient)
                gradient_process[i, :] = gradient

        y_row = output_tensor.numpy()
        y_process[i] = y_row
        y_hist = update_hist(y_hist, y_row.reshape((1, 1)))

    X_process, Y_process = sequence_data(u_process, 
                                         y_process, 
                                         P, 
                                         Q, 
                                         1)
    N = X_process.shape[0]
    gradient_process = gradient_process[-N: , :]
    X_process = X_process.reshape((X_process.shape[:2]))
    Y_process = Y_process.reshape((Y_process.shape[:2]))

elif source == "experiment":
    u_process, y_process, _, _ = load_experiment(
        data_dir + 'experiment_igor/series/', [1,2,3,4,5,6,7], [7]
        )
    X_process, Y_process = sequence_data(u_process, y_process, P, Q, 1)
    
    X_process = X_process.reshape((X_process.shape[:2]))
    Y_process = Y_process.reshape((Y_process.shape[:2]))

    X_process = normalize_data(X_process)
    Y_process = normalize_data(Y_process)
    input_scaling = "min-max"
    if input_scaling == "mean-std":
        X_process = standardize_data(X_process)

    output_scaling = "min-max"
    if output_scaling == "mean-std":
        Y_process = standardize_data(Y_process)

    elif output_scaling == "min-max":
        Y_process = normalize_data(Y_process)

    N = X_process.shape[0]
    gradient_inputs = P + 3
    gradient_process = np.zeros((N, P))
    for i in tqdm(range(N), desc='Processing', unit='iteration'):
        input_tensor = tf.convert_to_tensor(
            X_process[i, :].reshape((1, P + Q, 1)), 
            dtype=tf.float32
        )
        for j in range(1):
            with tf.GradientTape() as t:
                t.watch(input_tensor)
                output_tensor = process_model(input_tensor)
                gradient = t.gradient(
                    output_tensor[:, j], input_tensor
                ).numpy()[0, :, 0]
                gradient = split_gradient(gradient)
                gradient_process[i, :] = gradient

input_train, input_test, output_train, output_test = build_gradient_dataset(
                                                        X_process, 
                                                        gradient_process,
                                                        gradient_inputs,
                                                        test_split=0.2
                                                        )

np.savetxt(data_dir + f'gradient/{source}/inputs_train.csv', input_train)
np.savetxt(data_dir + f'gradient/{source}/inputs_test.csv', input_test)
np.savetxt(data_dir + f'gradient/{source}/outputs_train.csv', output_train)
np.savetxt(data_dir + f'gradient/{source}/outputs_test.csv', output_test)

import matplotlib.pyplot as plt
plt.plot(u_process, label='u')
plt.plot(y_process, label='y')
plt.legend()
plt.show()