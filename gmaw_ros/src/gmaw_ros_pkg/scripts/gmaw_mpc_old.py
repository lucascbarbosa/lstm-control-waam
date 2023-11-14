import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
from tensorflow.python.ops import array_ops
from sklearn.preprocessing import StandardScaler, MinMaxScaler

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

import rospy
from std_msgs.msg import Float32

import os
import time
from multiprocessing import Pool, cpu_count

#############
# Filepaths #
data_dir = f"/home/lbarbosa/Documents/Github/lstm-control-waam/database/experiment/"
results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"

#############
# Functions #
# rospy
def callback(data):
    rospy.loginfo("Received output y: %f", data.data)
    # Extract y_row from cell
    y_row = data.data
    y.append(y_row)
    # print(f"y: {y_row}")
    y_row_scaled = (y_row - y_mean) / y_std  # Standardize
    y_hist = update_hist(y_hist, y_row_scaled.reshape((1,1)))

# process_data
def resample_data(original_data, original_time, new_time):
    interp_func = interp1d(
        original_time,
        original_data,
        kind="linear",
        fill_value="extrapolate",
    )

    resampled_data = np.zeros((new_time.shape[0], 2))
    resampled_data[:, 0] = new_time
    resampled_data[:, 1] = interp_func(new_time)
    return resampled_data


def load_experiment(data_dir, idx_train, idx_test):
    filename_train = f"bead{idx_train}"
    input_train = pd.read_csv(data_dir + filename_train + "_w.csv").to_numpy()
    output_train = pd.read_csv(
        data_dir + filename_train + "_wfs.csv"
    ).to_numpy()

    output_train = resample_data(
        output_train[:, 1], output_train[:, 0], input_train[:, 0]
    )

    filename_test = f"bead{idx_test}"
    input_test = pd.read_csv(data_dir + filename_test + "_w.csv").to_numpy()
    output_test = pd.read_csv(data_dir + filename_test + "_wfs.csv").to_numpy()

    output_test = resample_data(
        output_test[:, 1], output_test[:, 0], input_test[:, 0]
    )

    return (
        input_train[:, 1:],
        output_train[:, 1:],
        input_test[:, 1:],
        output_test[:, 1:],
    )

# mpc
def build_sequence(u_hist, y_hist):
    u = u_hist.ravel()
    y = y_hist.ravel()
    return np.hstack((u, y)).reshape((1, 1 * (P + Q), 1))


def split_sequence(seq):
    seq = seq.reshape((1 * (P + Q),))
    u = seq[: 1 * P].reshape((P, 1))
    y = seq[1 * P :].reshape((Q, 1))
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
    output_error = (y_ref - y_forecast) * y_std
    output_cost = np.sum(output_error**2 @ weights_output)
    control_cost = np.sum(u_diff_forecast**2 @ weights_control)
    return output_cost + control_cost


def compute_step(u_hist, y_hist, u_forecast, lr):
    if 1 == 2:
        output_jacobian = np.zeros((N, M, 2, 2))
    elif 1 == 1:
        output_jacobian = np.zeros((N, M))
    y_forecast = np.zeros((N, 1))
    # gradients = np.zeros((N, P + Q, 2, 2))
    for i in range(N):
        if i < M:
            u_row = u_forecast[i].reshape((1, 1))
        if i >= M:
            u_row = u_forecast[-1].reshape((1, 1))
        u_hist = update_hist(u_hist, u_row)
        seq_input = build_sequence(u_hist, y_hist)
        input_tensor = tf.convert_to_tensor(seq_input, dtype=tf.float32)
        for j in range(1):
            with tf.GradientTape() as t:
                t.watch(input_tensor)
                output_tensor = keras_model(input_tensor)
                gradient = t.gradient(
                    output_tensor[:, j], input_tensor
                ).numpy()[0, :, 0]

            # gradients[i, :, j, :] = gradient.reshape((P + Q, 2))
            input_gradient, output_gradient = split_sequence(gradient)
            if i < P - 1:
                output_jacobian[i, : i + 1] = input_gradient[
                    -(i + 1) :, :
                ].ravel()
            else:
                output_jacobian[i, :] = input_gradient[:, :].ravel()

        y_row = output_tensor.numpy().reshape((1, 1))
        y_forecast[i, :] = y_row
        y_hist = update_hist(y_hist, y_row)

    input_jacobian = build_input_jacobian()
    steps = np.zeros(u_forecast.shape)
    # u_forecast = u_forecast * (u_max - u_min) + u_min
    u_diff_forecast = create_control_diff(u_forecast)
    output_error = (y_ref - y_forecast) * y_std
    weight_control = weights_control[0]
    input_diff = u_diff_forecast
    for j in range(M):
        output_gradient = (
            -2
            * np.diag(output_error.T @ output_jacobian[:, j])
            @ weights_output
        )

        input_gradient = (
            2 * input_jacobian[:, j].T @ input_diff * weight_control
        )

        steps[j, 0] = -lr * (output_gradient + input_gradient)

    return steps, y_forecast


def optimization_function(u_hist, y_hist, lr):
    # u_forecast = np.random.uniform(size=(M, 2))  #
    u_forecast = np.ones((M, 1)) * 0.5  #
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
        # print(f"Error: {(y_forecast-y_ref)*y_std}")
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

#########
# Loads #
# Load data
inputs_train, outputs_train, _, _ = load_experiment(data_dir, 1, 2)

u_min = inputs_train.min(axis=0)
u_max = inputs_train.max(axis=0)
y_mean = outputs_train.mean(axis=0)
y_std = outputs_train.std(axis=0)

# Load metrics
metrics_df = pd.read_csv(results_dir + f"models/experiment/hp_metrics.csv")
best_model_id = 85
best_model_filename = f"run_{best_model_id:03d}.keras"
best_params = metrics_df[metrics_df["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

# Load Keras model
keras_model = load_model(
    results_dir + f"models/experiment/best/{best_model_filename}"
)

opt = Adam(learning_rate=best_params["lr"])
keras_model.compile(optimizer=opt, loss=mean_squared_error)

# Define MPC parameters
M = P  # control horizon
N = Q  # prediction horizon
weights_control = 0.1 * np.ones((1, 1))  #
weights_output = 10 * np.ones((1, 1))  #

# # Boundaries
# min_f, max_f = 0.0, 1.0
# min_Ir, max_Ir = 0.0, 1.0
# min_we, max_we = 0.0, 1.0
# min_h, max_h = 0.0, 1.0

# Desired outputs
y_ref = np.zeros(1)

# Initial conditions
y0 = 1e-10 * np.ones((1, 1))

# Historic data
u_hist = np.zeros((P, 1))
y_hist = np.zeros((Q, 1))
y_hist[-1, :] = (y0.ravel() - y_mean) / y_std  # Standardize

# ROSPY Parameters
rospy.init_node("mpc_node", anonymous=True)
# Create a subscriber to receive the "y_row" variable
rospy.Subscriber("y", Float32, callback)
pub = rospy.Publisher("u", Float32, queue_size=10)
pub_freq = 1 # sampling frequency of published data
step_time = 1 / pub_freq
total_steps = 10
rate = rospy.Rate(pub_freq)

# Experiment data
y = []
y.append(y0)
u = []

# Optimization parameters
lr = 1e-1  #
alpha = 1e-3  #
cost_tol = 1e-3  #

# MPC loop
y_row = y0
exp_time = 0
exp_step = 0
while not rospy.is_shutdown():
    print(f"Time step: {exp_step}")
    u_opt, u_forecast, y_forecast = optimization_function(u_hist, y_hist, lr)
    u_hist = update_hist(u_hist, u_opt.reshape((1, 1)))
    u_opt = u_opt[0, 0]
    u_row = u_opt * (u_max - u_min) + u_min  # Denormalize
    print(f"u_opt: {u_row}")
    u.append(u_row)
    
    # Send the "u_row" variable
    pub.publish(u_row)
    rospy.loginfo("Sending control u: %f", u_row)
    rate.sleep()
    exp_step += 1
    exp_time = step_time
    
rospy.spin()

# u = u[:-1, :]

# u = pd.DataFrame(u, columns=["f", "Ir"])
# y = pd.DataFrame(y, columns=["we", "h"])

# u.to_csv(results_dir + "mpc/u.csv", index=False)
# y.to_csv(results_dir + "mpc/y.csv", index=False)
