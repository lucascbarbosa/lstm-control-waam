from python.gmaw_process import *
from python.process_data import load_experiment, load_simulation

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
data_dir = f"database/simulation/"
results_dir = "results/"

#########
# Loads #
# Load data
inputs_train, outputs_train, _, _ = load_simulation(data_dir)

u_mins = inputs_train.min(axis=0)
u_maxs = inputs_train.max(axis=0)
y_means = outputs_train.mean(axis=0)
y_stds = outputs_train.std(axis=0)

# Load metrics
metrics_df = pd.read_csv(results_dir + f"models/simulation/hp_metrics.csv")
best_model_id = 10
best_model_filename = f"run_{best_model_id:03d}.keras"
best_params = metrics_df[metrics_df["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

# Load Keras model
keras_model = load_model(
    results_dir + f"models/simulation/best/{best_model_filename}"
)

opt = Adam(learning_rate=best_params["lr"])
keras_model.compile(optimizer=opt, loss=mean_squared_error)

# Define MPC parameters
M = P  # control horizon
N = Q  # prediction horizon
weights_control = 0.1 * np.ones((2, 1))  #
weights_output = 10 * np.ones((2, 1))  #

# Simulation parameters
step = 1e-5
sim_time = 1e-2
num_time_steps = 40

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

# # Boundaries
# min_f, max_f = 0.0, 1.0
# min_Ir, max_Ir = 0.0, 1.0
# min_we, max_we = 0.0, 1.0
# min_h, max_h = 0.0, 1.0

# Desired outputs
y_ref = np.zeros(2)

# Historic data
u_hist = np.zeros((P, 2))
y_hist = np.zeros((Q, 2))
y_hist[-1, :] = (y0.ravel() - y_means) / y_stds  # Standardize

#############
# Functions #
def callback(data):
    rospy.loginfo("Received output y: %f", data.data)

def build_sequence(u_hist, y_hist):
    u = u_hist.ravel()
    y = y_hist.ravel()
    return np.hstack((u, y)).reshape((1, 2 * (P + Q), 1))


def split_sequence(seq):
    seq = seq.reshape((2 * (P + Q),))
    u = seq[: 2 * P].reshape((P, 2))
    y = seq[2 * P :].reshape((Q, 2))
    return u, y


def update_hist(current_hist, new_states):
    new_hist = current_hist.copy()
    len_new = new_states.shape[0]
    new_hist[:-len_new, :] = current_hist[len_new:, :]
    new_hist[-len_new:, :] = new_states
    return new_hist


def create_control_diff(u_forecast):
    u_diff = u_forecast.copy()
    u_diff[1:] = u_diff[1:] - u_diff[:-1]
    return u_diff


def build_input_jacobian():
    input_jacobian = np.eye(M)
    for i in range(M):
        if i < M - 1:
            input_jacobian[i + 1, i] = -1
    return input_jacobian


def cost_function(u_forecast, y_forecast, y_ref):
    u_diff_forecast = create_control_diff(u_forecast)
    output_error = (y_ref - y_forecast) * y_stds
    output_cost = np.sum(output_error**2 @ weights_output)
    control_cost = np.sum(u_diff_forecast**2 @ weights_control)
    return output_cost + control_cost


def compute_step(u_hist, y_hist, u_forecast, lr):
    if 2 == 2:
        output_jacobian = np.zeros((N, M, 2, 2))
    elif 2 == 1:
        output_jacobian = np.zeros((N, M))
    y_forecast = np.zeros((N, 2))
    # gradients = np.zeros((N, P + Q, 2, 2))
    for i in range(N):
        if i < M:
            u_row = u_forecast[i].reshape((1, 2))
        if i >= M:
            u_row = u_forecast[-1].reshape((1, 2))
        u_hist = update_hist(u_hist, u_row)
        seq_input = build_sequence(u_hist, y_hist)
        input_tensor = tf.convert_to_tensor(seq_input, dtype=tf.float32)
        for j in range(2):
            with tf.GradientTape() as t:
                t.watch(input_tensor)
                output_tensor = keras_model(input_tensor)
                gradient = t.gradient(
                    output_tensor[:, j], input_tensor
                ).numpy()[0, :, 0]

            # gradients[i, :, j, :] = gradient.reshape((P + Q, 2))
            input_gradient, output_gradient = split_sequence(gradient)
            if i < P - 1:
                output_jacobian[i, : i + 1, :, j] = input_gradient[
                    -(i + 1) :, :
                ]
            else:
                output_jacobian[i, :, :, j] = input_gradient[:, :]

        y_row = output_tensor.numpy().reshape((1, 2))
        y_forecast[i, :] = y_row
        y_hist = update_hist(y_hist, y_row)

    input_jacobian = build_input_jacobian()
    steps = np.zeros(u_forecast.shape)
    # u_forecast = u_forecast * (u_maxs - u_mins) + u_mins
    u_diff_forecast = create_control_diff(u_forecast)
    output_error = (y_ref - y_forecast) * y_stds
    for i in range(2):
        weight_control = weights_control[i]
        input_diff = u_diff_forecast[:, i]
        for j in range(M):
            output_gradient = (
                -2
                * np.diag(output_error.T @ output_jacobian[:, j, :, i])
                @ weights_output
            )

            input_gradient = (
                2 * input_jacobian[:, j].T @ input_diff * weight_control
            )

            steps[j, i] = -lr * (output_gradient + input_gradient)

    return steps, y_forecast


def optimization_function(u_hist, y_hist, lr):
    # u_forecast = np.random.uniform(size=(M, 2))  #
    u_forecast = np.ones((M, 2)) * 0.5  #
    s = 0
    cost = np.inf
    last_cost = cost
    delta_cost = -cost
    while delta_cost < -cost_tol:
        print(f"Opt step: {s+1}")
        steps, y_forecast = compute_step(u_hist, y_hist, u_forecast, lr)
        cost = cost_function(u_forecast, y_forecast, y_ref)
        delta_cost = cost - last_cost
        print(f"Cost: {cost}\n ")
        # print(f"Steps: \n{steps}")
        # print(f"Error: {(y_forecast-y_ref)*y_stds}")
        if delta_cost < 0:
            u_forecast += steps
            lr = lr * (1.0 - alpha)
            last_cost = cost
            s += 1
        else:
            print("Passed optimal solution")
            break
    u_opt = u_forecast[0, :]
    return u_opt, u_forecast, y_forecast


x_row = x0
y_row = y0

# Optimization parameters
lr = 1e-1  #
alpha = 1e-3  #
cost_tol = 1e-3  #

# MPC loop
for t in range(1, num_time_steps):
    print(f"Time step: {t}")
    u_opt, u_forecast, y_forecast = optimization_function(u_hist, y_hist, lr)
    u_hist = update_hist(u_hist, u_opt.reshape((1, 2)))
    u_row = u_opt * (u_maxs - u_mins) + u_mins  # Denormalize
    print(f"u_opt: {u_row}")
    u[t - 1, :] = u_row
    # Propagate dynamics using simulation
    x_row = solve_rk4(gmaw_states, x_row, step, u_row.tolist())
    x[t, :] = x_row
    y_row = np.array(gmaw_outputs(x_row)).reshape((1, 2))

    y[t, :] = y_row
    y_row_scaled = (y_row - y_means) / y_stds  # Standardize
    y_hist = update_hist(y_hist, y_row_scaled)
    print(f"y: {y_row}")

u = u[:-1, :]

u = pd.DataFrame(u, columns=["f", "Ir"])
y = pd.DataFrame(y, columns=["we", "h"])

u.to_csv(results_dir + "mpc/simulation/u.csv", index=False)
y.to_csv(results_dir + "mpc/simulation/y.csv", index=False)