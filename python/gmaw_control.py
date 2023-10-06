from python.gmaw_process import *
from python.process_data import load_data

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
# Load data
inputs_train, outputs_train, _, _ = load_data(data_dir)
u_mins = inputs_train.min(axis=0)
u_maxs = inputs_train.max(axis=0)
y_means = outputs_train.mean(axis=0)
y_stds = outputs_train.std(axis=0)

# Load metrics
metrics_df = pd.read_csv(results_dir + "models/hp_metrics.csv")
best_model_id = "010"
best_model_filename = f"run_{best_model_id}.keras"
best_params = metrics_df[metrics_df["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

# Load Keras model
keras_model = load_model(
    results_dir + f"models/best/run_{best_model_id}.keras"
)

opt = Adam(learning_rate=best_params["lr"])
keras_model.compile(optimizer=opt, loss=mean_squared_error)

# Define MPC parameters
N = 10  # prediction horizon
M = 10  # control horizon
weights_control = np.array([[1, 1]]).reshape((2, 1))
weights_output = np.array([[1, 1]]).reshape((2, 1))

# Simulation parameters
step = 1e-5
sim_time = 1e-2
num_time_steps = int(sim_time / step)

# Initial conditions
x0 = [1e-10, 1e-10]
y0 = gmaw_outputs(x0)
y0 = np.array(y0).reshape((1, 2))

# Simulation data
x = np.zeros((num_time_steps, 2))
x[0, :] = x0
y = np.zeros((num_time_steps, 2))
y[0, :] = y0
u = np.zeros((num_time_steps, 2))

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
y_ref = np.zeros(2)

# Historic data
u_hist = np.zeros((P, 2))
y_hist = np.zeros((Q, 2))
y_hist[-1, :] = (y0.ravel() - y_means) / y_stds  # Standardize


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


def forecast_output(u_forecast, u_hist, y_hist):
    y_forecast = np.zeros((N, 2))
    for i in range(M):
        u_row = u_forecast[i, :].reshape((1, 2))
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
    u_diff_forecast = (
        create_control_diff(u_forecast) * (u_maxs - u_mins) + u_mins
    )
    output_error = (y_ref - y_forecast) * y_stds + y_means
    output_cost = np.sum(output_error**2 @ weights_output)
    control_cost = np.sum(u_diff_forecast**2 @ weights_control)
    return output_cost + control_cost


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
    jacobian = np.zeros((M, 2, 2))
    for i in range(M):
        u_row = u_forecast[i].reshape((1, 2))
        u_hist = update_hist(u_hist, u_row)
        seq_input = build_sequence(u_hist, y_hist)
        gradient = compute_gradient(seq_input)
        jacobian[i, :, :] = gradient
        y_row = y_forecast[i].reshape((1, 2))
        y_hist = update_hist(y_hist, y_row)

    steps = np.zeros(u_forecast.shape)
    # u_diff_forecast = create_control_diff(u_forecast)
    # print(f"dU: \n{u_diff_forecast}")
    # for i in range(2):
    #     jacobian_input = jacobian[:, :, i]
    #     weight_control = weights_control[i]
    #     u_diff = u_diff_forecast[:, i].reshape((u_diff_forecast.shape[0], 1))
    #     output_error = (y_ref - y_forecast) * y_stds + y_means
    #     output_gradient = np.diag(jacobian_input.T @ output_error)
    #     output_gradient = (-weights_output.T @ output_gradient)[0]
    #     control_gradient = weight_control * u_diff
    #     step = -lr * (output_gradient + control_gradient)
    #     steps[:, i] = step.ravel()
    return steps


def optimization_function(u_hist, y_hist, num_opt_steps, lr):
    u_forecast = np.random.uniform(size=(M, 2))  # Initialize control forecast
    y_forecast = forecast_output(
        u_forecast, u_hist, y_hist
    )  # Estimate output forecast based on control forecast

    for s in range(num_opt_steps):
        print(f"Time step: {t} \nOpt step: {s+1}")
        cost = cost_function(u_forecast, y_forecast, y_ref)
        steps = compute_step(u_hist, y_hist, u_forecast, y_forecast, lr)
        # print(f"U_f: \n{u_forecast}")
        # print(f"Y_f: \n{y_forecast}")
        u_forecast += steps
        y_forecast = forecast_output(u_forecast, u_hist, y_hist)
        print(f"Cost: {cost}\n ")
        print(f"Steps: \n{steps}")

    u_opt = u_forecast[0, :]
    return u_opt


x_row = x0
y_row = y0
lr = 1e0
num_opt_steps = 50

u_forecast = np.random.uniform(size=(M, 2))  # Initialize control forecast
y_forecast = forecast_output(u_forecast, u_hist, y_hist)
step = compute_step(u_hist, y_hist, u_forecast, y_forecast, lr)

# # MPC loop
# for t in range(1, 100):
#     u_opt = optimization_function(u_hist, y_hist, num_opt_steps, lr)
#     u[t - 1, :] = u_opt
#     u_hist = update_hist(u_hist, u_opt.reshape((1, 2)))
#     u_row = u_opt * (u_maxs - u_mins) + u_mins  # Denormalize
#     x_row = solve_rk4(gmaw_states, x_row, step, u_row.tolist())
#     x[t, :] = x_row

#     # Estimate using Dynamics
#     y_row = np.array(gmaw_outputs(x_row)).reshape((1, 2))
#     print(f"y: {y_row}")
#     y[t, :] = y_row
#     y_row_scaled = (y_row - y_means) / y_stds  # Standardize
#     y_hist = update_hist(y_hist, y_row_scaled)
#     # print(f"u_opt: {u_opt}")
#     # print(f"x_row: {x_row}")