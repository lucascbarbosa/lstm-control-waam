import numpy as np
import pandas as pd
from itertools import product
from tqdm import tqdm

import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
from python.process_data import sequence_data

# Data paths
data_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/database/gradient/"
results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"

# Functions
def build_sequence(u, y):
    u = u.ravel()
    y = y.ravel()
    return np.hstack((u, y)).reshape((1, P + Q, 1))

def build_gradient_dataset(X_process, gradient_process, gradient_inputs, test_split):
    input_gradient = X_process[:, :gradient_inputs, 0]
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

def cartesian2spherical(grad):
    grad_spherical = np.zeros(P, )
    grad_spherical[0] = np.sqrt(np.sum(grad **2))
    for i in range(1, P):
        grad_spherical[i] = np.arccos(grad[i-1]/grad_spherical[0])
    return grad_spherical

def spherical2cartesian(grad_spherical):
    grad = np.zeros(P, )
    for i in range(P-1):
        grad[i] = grad_spherical[0] * np.cos(grad_spherical[i+1])

    grad[-1] = np.sqrt(
        grad_spherical[0] ** 2 * (1- np.sum(np.cos(grad_spherical[1:])**2))
        )
    return grad

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

# Create input data
N = 20_000
process_inputs = 1
process_outputs = 1
u_process = np.random.uniform(size=(N, process_inputs))
y_process = np.random.uniform(size=(N, process_outputs))
X_process, Y_process = sequence_data(u_process, y_process, P, Q, 1)
N = X_process.shape[0]
gradient_inputs = P
gradient_process = np.zeros((N, P))
for i in tqdm(range(X_process.shape[0]), desc='Processing', unit='iteration'):
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
#             # gradient = cartesian2spherical(gradient)
            gradient_process[i, :] = gradient

input_train, input_test, output_train, output_test = build_gradient_dataset(
                                                        X_process, 
                                                        gradient_process,
                                                        gradient_inputs,
                                                        test_split=0.2
                                                        )

np.savetxt(data_dir + 'input_train.csv', input_train)
np.savetxt(data_dir + 'input_test.csv', input_test)
np.savetxt(data_dir + 'output_train.csv', output_train)
np.savetxt(data_dir + 'output_test.csv', output_test)
