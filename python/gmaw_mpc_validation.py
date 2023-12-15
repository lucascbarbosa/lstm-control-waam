from python.process_data import load_experiment

import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

import time

import matplotlib.pyplot as plt

# Load experiment method
def update_hist(current_hist, new_states):
    new_hist = current_hist.copy()
    len_new = new_states.shape[0]
    new_hist[:-len_new, :] = current_hist[len_new:, :]
    new_hist[-len_new:, :] = new_states
    return new_hist

def build_sequence(u_hist, y_hist):
    u = u_hist.ravel()
    y = y_hist.ravel()
    return np.hstack((u, y)).reshape((1, 1 * (P + Q), 1))

def split_sequence(seq):
    seq = seq.reshape((1 * (P + Q),))
    u = seq[: 1 * P].reshape((P, 1))
    y = seq[1 * P :].reshape((Q, 1))
    return u, y

# Create control diff method
def create_control_diff(u_forecast):
    u_diff = u_forecast.copy()
    u_diff[1:] = u_diff[1:] - u_diff[:-1]
    return u_diff

# Build input jacobian method
def build_input_jacobian():
    input_jacobian = np.eye(M)
    for i in range(M):
        if i < M - 1:
            input_jacobian[i + 1, i] = -1
    return input_jacobian

# Cost function method
def cost_function(u_forecast, y_forecast, y_ref):
    u_diff_forecast = create_control_diff(u_forecast)
    output_error = (y_ref - y_forecast) * y_std
    output_cost = np.sum(output_error**2 * weight_output)
    control_cost = np.sum(u_diff_forecast**2 * weight_control)
    return output_cost + control_cost

def compute_step(u_hist, y_hist, u_forecast, lr):
    output_jacobian = np.zeros((N, M))
    y_forecast = np.zeros((N, 1))
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

            input_gradient, _ = split_sequence(gradient)
            if i < P - 1:
                output_jacobian[i, : i + 1] = input_gradient[
                    -(i + 1) :, :
                ].ravel()
            else:
                output_jacobian[i, :] = input_gradient[:, :].ravel()

        y_row = output_tensor.numpy().reshape((1, 1))
        y_forecast[i, :] = y_row
        y_hist = update_hist(y_hist, y_row)
    # ---------

    input_jacobian = build_input_jacobian()
    steps = np.zeros(u_forecast.shape)
    u_diff_forecast = create_control_diff(u_forecast)
    output_error = (y_ref - y_forecast) * y_std
    input_diff = u_diff_forecast
    # print(f"output_error: \n{output_error}")
    # print(f"output_jacobian: \n{output_jacobian}")

    for j in range(M):
        input_step = (
            2 * input_jacobian[:, j].T @ input_diff * weight_control
        )

        output_step = (
            -2
            * output_error.T @ output_jacobian[:, j]
            * weight_output
        )
        # print(f"output_step: \n{output_step}")
        steps[j, 0] = -lr * (output_step + input_step)

    return steps, y_forecast

# Optimization function method
def optimization_function(u_hist, y_hist, lr, u_forecast=None):
    if u_forecast is None:
        u_forecast = np.random.normal(loc=0.5, scale=0.05, size=(M, 1)) #
    s = 0
    cost = np.inf
    last_cost = cost
    delta_cost = -cost
    # print(f"U_F: \n{u_forecast}")   
    while delta_cost < -cost_tol:
        steps, y_forecast = compute_step(u_hist, y_hist, u_forecast, lr)
        cost = cost_function(u_forecast, y_forecast, y_ref)
        delta_cost = cost - last_cost
        print(f"Opt step: {s+1}")
        print(f"Cost: {cost}\n")
        # print(f"Steps: \n{steps}")
        if delta_cost < 0:
            u_forecast += steps
            lr = lr * (1.0 - alpha)
            last_cost = cost
            s += 1
        else:
            print("Passed optimal solution")
            break

    u_opt = u_forecast[0, :]
    # print(f"U_F: \n{u_forecast}")   
    print(f"Y_F: \n{y_forecast * y_std + y_mean}")
    # print(f"u_opt: {u_opt}")
    return u_opt, u_forecast, y_forecast, last_cost

# Filepaths
data_dir = "database/experiment/"
results_dir = "results/models/experiment/"

# ROSPY Parameters
pub_freq = 30  # sampling frequency of published data
step_time = 1 / pub_freq
total_steps = 10

# Load data
input_train, output_train, input_test, output_test = load_experiment(
    data_dir, [1, 2, 3, 4, 5, 6], [7]
    )

output_test = output_test[:680]
input_test = input_test[:680]

u_min = input_test.min(axis=0)
u_max = input_test.max(axis=0)
y_mean = output_test.mean(axis=0)
y_std = output_test.std(axis=0)

# Experiment data
u = []
y = []
costs = []
errors = []

# Load metrics
metrics_df = pd.read_csv(results_dir + f"hp_metrics.csv")
best_model_id = 282 #
best_model_filename = f"run_{best_model_id:03d}.keras"
best_params = metrics_df[metrics_df["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

# Load Keras model
keras_model = load_model(
    results_dir + f"best/{best_model_filename}"
)

opt = Adam(learning_rate=best_params["lr"])
keras_model.compile(optimizer=opt, loss=mean_squared_error)

# Weights
weight_control = 1.0
weight_output = 1.0

# Desired outputs
y_ref = np.ones((1,)) * 0

# Historic data
u_hist = np.zeros((P, 1))
y_hist = np.zeros((Q, 1))

# Initial condition
y0 = output_test[0,0]
y0_scaled = (y0 - y_mean) / y_std
y_hist = update_hist(y_hist, np.array(y0_scaled).reshape((1, 1)))

# Optimization parameters
lr = 1e-2 #1e-1
alpha = 1e-3 #1e-3
cost_tol = 1e-2 #1e-1

# MPC loop
M = P # control horizon
N = Q # prediction horizon
u_forecast = np.random.normal(loc=0.5, scale=0.05, size=(M, 1)) #

exp_step = 0 
while exp_step < input_test.shape[0]:
    print(f"Time step: {exp_step}")
    mpc_period = np.where(input_test == input_test[exp_step])[0].shape[0]
    if exp_step > 100:
        u_opt, u_forecast, y_forecast, cost = optimization_function(u_hist, y_hist, lr, u_forecast)
    else: 
        u_row = input_test[exp_step]
        u_opt = (u_row - u_min) / (u_max - u_min)
    u_hist = update_hist(u_hist, u_opt.reshape((1, 1)))
    u_opt_descaled = u_opt[0] * (u_max - u_min) + u_min  # Denormalize
    u_opt_descaled = u_opt_descaled[0]
    
    d = 0
    while d < mpc_period and exp_step + d < input_test.shape[0]:

        u_hist = update_hist(u_hist, u_opt.reshape((1, 1)))
        u.append(u_opt_descaled)
        
        # Extract y_row from test data
        if exp_step + d < 100:
            y_row = output_test[exp_step + d, 0]
            y_row_scaled = (y_row - y_mean) / y_std
        else:
            seq_input = build_sequence(u_hist, y_hist)
            input_tensor = tf.convert_to_tensor(seq_input, dtype=tf.float32)
            output_tensor = keras_model(input_tensor)
            y_row_scaled = output_tensor.numpy().reshape((1, 1))
            y_row = y_row_scaled * y_std + y_mean
            y_row = y_row[0,0]

        y.append(y_row) 
        error = (y_ref[0] - y_row_scaled) * y_std
        costs.append(cost)
        errors.append(error[0])
        y_hist = update_hist(y_hist, np.array(y_row_scaled).reshape((1, 1)))

        d += 1

    exp_step += mpc_period

u = np.array(u)
u_real = input_test[:len(u)].ravel()
costs = np.array(costs)
errors = np.array(errors)

# Plot results
# fig, axs = plt.subplots(2, 1)
# fig.set_size_inches((12,10))

# axs[0].step(range(u.shape[0]), u_real, color='k', label='experiment')
# axs[0].step(range(u.shape[0]), u, color='r', label='mpc')
# axs[0].legend()

# axs[1].plot(errors, color='k', label='experiment error')
# axs[1].plot(costs, color='r', label='mpc cost')
# axs[1].legend()

# plt.tight_layout()
# plt.show()

plt.plot(output_test, color='k', label='experiment')
plt.plot(y, color='r', label='forecast')
plt.title(r'$w_e$ (mm)')
plt.tight_layout()
plt.legend()
plt.show()