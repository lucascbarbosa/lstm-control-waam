from python.gmaw_process import *

import numpy as np
import pandas as pd
import os
import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam


#############
# Filepaths #
data_dir = "database/"
results_dir = "results/"

#########
# Loads #
# Load metrics
metrics_df = pd.read_csv(results_dir + "models/hp_metrics.csv")
best_model_id = metrics_df.iloc[0, 0]
best_model_filename = os.listdir(results_dir + "models/best/")[0]
best_params = metrics_df.iloc[0, 1:]
P = int(best_params["P"])
Q = int(best_params["Q"])

# Load Keras model
best_model_id = 13
keras_model = load_model(
    results_dir + f"models/best/run_{best_model_id:03d}.keras"
)
opt = Adam(learning_rate=best_params["lr"])
keras_model.compile(optimizer=opt, loss=mean_squared_error)

# Define MPC parameters
N = 10  # prediction horizon
M = 10  # control horizon
weight_control = np.array([[1, 1]]).reshape((2, 1))
weight_output = np.array([[1, 1]]).reshape((2, 1))

# Simulation parameters
step = 1e-6
sim_time = 1e-3
total_sim_steps = int(sim_time / step)

# Initial conditions
x0 = [1e-10, 1e-10]
y0 = gmaw_outputs(x0)

x0 = np.array(x0).reshape((1, 2))
y0 = np.array(y0).reshape((1, 2))

# Boundaries and constraints
min_f, max_f = 0.0, 1.0
min_Ir, max_Ir = 0.0, 1.0
min_we, max_we = 0.0, 1.0
min_h, max_h = 0.0, 1.0
control_bounds = np.array([[(min_f, max_f), (min_Ir, max_Ir)]])  # Input bounds
control_bounds = np.repeat(control_bounds, M, axis=0)
output_bounds = np.array([[(min_we, max_we), (min_h, max_h)]])  # Output bounds
output_bounds = np.repeat(output_bounds, N, axis=0)
bounds = control_bounds + output_bounds

# Desired outputs
y_ref = np.array([[weo, ho]])

# Historic data
u_hist = np.zeros((P - 1, 2))
y_hist = np.zeros((Q - 1, 2))


#############
# Functions #
def build_sequence(u_hist, u_last, y_hist, y_last):
    u = np.vstack((u_hist, u_last)).ravel()
    y = np.vstack((y_hist, y_last)).ravel()
    return np.hstack((u, y)).reshape((1, 2 * (P + Q), 1))


def lstm_predict(u_hist, u_last, y_hist, y_last):
    seq_input = build_sequence(u_hist, u_last, y_hist, y_last)
    y_hat = keras_model.predict(seq_input, verbose=0)
    return y_hat


def update_hist(current_hist, last_state):
    new_hist = current_hist.copy()
    new_hist[:-1, :] = current_hist[1:, :]
    new_hist[-1, :] = last_state
    return new_hist


def cost_function(u_forecast, u_hist, y_hist, y_row, y_ref):
    y_forecast = np.zeros((N, 2))
    y_hat = y_row
    for i in range(N):
        u_row = u_forecast[i]
        y_hat = lstm_predict(u_hist, u_row, y_hist, y_hat)
        y_forecast[i] = y_hat
        y_hist = update_hist(y_hist, y_hat)
        u_hist = update_hist(u_hist, u_row)

    u_diff_forecast = create_control_diff(u_forecast)
    return np.sum(np.dot((y_forecast - y_ref) ** 2, weight_output)) + np.sum(
        np.dot(u_diff_forecast, weight_control)
    )


def create_control_diff(u_forecast):
    u_diff = u_forecast.copy()
    u_diff[1:] = u_diff[1:] - u_diff[:-1]
    return u_diff


def compute_gradient(seq_input):
    input_tensor = tf.convert_to_tensor(seq_input, dtype=tf.float32)
    with tf.GradientTape() as t:
        t.watch(input_tensor)
        output = keras_model(input_tensor)
    gradients = t.gradient(output, input_tensor).numpy()[0][: 2 * P]
    return gradients


def optimization_function(u_forecast, y_last):
    cost = cost_function(u_forecast, u_hist, y_hist, y_last, y_ref)
    return cost


y_row = y0
u_row = np.zeros((1, 2))
seq_input = build_sequence(u_hist, u_row, y_hist, y0)
gradients = compute_gradient(seq_input)
u0_forecast = np.zeros((M, 2))
# MPC loop
# for t in range(total_sim_steps):

# u_forecast = np.random.normal(size=(M, 2))
# cost_function(u_forecast, u_hist, y_hist, y_row, y_ref)
