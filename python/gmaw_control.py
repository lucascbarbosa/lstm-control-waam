from python.gmaw_process import *

import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
from tensorflow.python.ops import array_ops

import numpy as np
import pandas as pd
import os
import time
from multiprocessing import Pool, cpu_count

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
weights_control = np.array([[1, 1]]).reshape((2, 1))
weights_output = np.array([[1, 1]]).reshape((2, 1))

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
u_hist = np.zeros((P, 2))
y_hist = np.zeros((Q, 2))


#############
# Functions #
def build_sequence(u_hist, y_hist):
    u = u_hist.ravel()
    y = y_hist.ravel()
    return np.hstack((u, y)).reshape((1, 2 * (P + Q), 1))


def lstm_predict(u_hist, y_hist):
    seq_input = build_sequence(u_hist, y_hist)
    y_hat = keras_model.predict(seq_input, verbose=0)
    return y_hat


def update_hist(current_hist, new_states):
    new_hist = current_hist.copy()
    len_new = new_states.shape[0]
    new_hist[:-len_new, :] = current_hist[len_new:, :]
    new_hist[-len_new:, :] = new_states
    return new_hist


def forecast_output(u_forecast, u_hist, y_hist, y_row):
    y_forecast = np.zeros((N, 2))
    y_hist = update_hist(y_hist, y_row)
    for i in range(N):
        u_row = u_forecast[i]
        u_hist = update_hist(u_hist, u_row)
        y_hat = lstm_predict(u_hist, y_hist)
        y_forecast[i] = y_hat
        y_hist = update_hist(y_hist, y_hat)
    return y_forecast


def create_control_diff(u_forecast):
    u_diff = u_forecast.copy()
    u_diff[1:] = u_diff[1:] - u_diff[:-1]
    return u_diff


def cost_function(u_forecast, y_forecast, y_ref):
    u_diff_forecast = create_control_diff(u_forecast)
    return np.sum((y_forecast - y_ref) ** 2 @ weights_output) + np.sum(
        np.abs(u_diff_forecast) @ weights_control
    )


def compute_gradient(seq_input):
    input_tensor = tf.convert_to_tensor(seq_input, dtype=tf.float32)
    gradient = np.zeros((2, 2))
    for i in range(2):
        with tf.GradientTape() as t:
            t.watch(input_tensor)
            output_tensor = keras_model(input_tensor)
            gradient[i, :] = (
                t.gradient(output_tensor[:, i], input_tensor)
                .numpy()
                .ravel()[2 * (P - 1) : 2 * P]
            )
    return gradient


def compute_step(u_hist, y_hist, u_forecast, y_forecast, lr):
    jacobian = np.zeros((u_forecast.shape[0], 2, 2))

    for i in range(u_forecast.shape[0]):
        u_row = u_forecast[i].reshape((1, 2))
        y_row = y_forecast[i].reshape((1, 2))
        u_hist = update_hist(u_hist, u_row)
        y_hist = update_hist(y_hist, y_row)
        seq_input = build_sequence(u_hist, y_hist)
        gradient = compute_gradient(seq_input)
        jacobian[i, :, :] = gradient

    u_diff_forecast = create_control_diff(u_forecast)
    steps = np.zeros(u_forecast.shape)
    for i in range(u_forecast.shape[1]):
        jacobian_input = jacobian[:, :, i]
        weight_control = weights_control[i]
        u_diff = u_diff_forecast[:, i].reshape((u_diff_forecast.shape[0], 1))
        output_gradient = np.diag(jacobian_input.T @ (y_forecast - y_ref))
        output_gradient = (-weights_output.T @ output_gradient)[0]
        control_gradient = weight_control * u_diff
        step = -lr * (output_gradient + control_gradient)
        steps[:, i] = step.ravel()

    return steps, u_hist, y_hist


def optimization_function(u_hist, y_hist, num_time_steps, num_opt_steps, lr):
    u_forecast = np.random.normal(size=(M, 2))
    y_forecast = forecast_output(u_forecast, u_hist, y_hist, y_row)
    u_opts = np.zeros((num_opt_steps, 2))
    for t in range(num_time_steps):
        for s in range(num_opt_steps):
            print(f"Time step: {t+1} \nOpt step: {s+1}")
            cost = cost_function(u_forecast, y_forecast, y_ref)
            steps, u_hist, y_hist = compute_step(
                u_hist, y_hist, u_forecast, y_forecast, lr
            )
            u_forecast += steps
            print(f"Cost: {cost}\n")
            # print(f"Steps: \n{steps}")
            # print(f"U: \n{u_forecast}")

        u_opt = u_forecast[0, :]


y_row = y0
u_row = np.zeros((1, 2))
lr = 1e0
num_time_steps = 10
num_opt_steps = 10
optimization_function(u_hist, y_hist, num_time_steps, num_opt_steps, lr)

# MPC loop
# for t in range(total_sim_steps):

# cost_function(u_hist, y_hist, y_row, y_ref)
