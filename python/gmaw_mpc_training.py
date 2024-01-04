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
def scale_input(u):
    if input_scaling == 'min-max':
        return (u - u_min) / (u_max - u_min)
    elif input_scaling == 'mean-std':
        return (u - u_mean) / u_std

def scale_output(y):
    if input_scaling == 'min-max':
        return (y - y_min) / (y_max - y_min)
    elif input_scaling == 'mean-std':
        return (y - y_mean) / y_std

def descale_input(u):
    if input_scaling == 'min-max':
        return u * (u_max - u_min) + u_min
    elif input_scaling == 'mean-std':
        return u * u_std + u_mean

def descale_output(y):
    if input_scaling == 'min-max':
        return y * (y_max - y_min) + y_min
    elif input_scaling == 'mean-std':
        return y * y_std + y_mean

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
    output_error = scale_output(y_ref) - scale_output(y_forecast)
    output_cost = np.sum(output_error**2 * weight_output)
    control_cost = np.sum(u_diff_forecast**2 * weight_control)
    return output_cost + control_cost

def compute_step(u_hist, y_hist, u_forecast):
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
    output_error = scale_output(y_ref) - scale_output(y_forecast)
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
        total_step = output_step + input_step
        steps[j, 0] = total_step

    return steps, y_forecast

# Optimization function method
def optimization_function(u_hist, y_hist, lr, u_forecast=None):
    if u_forecast is None:
        u_forecast = np.random.normal(loc=0.5, scale=0.05, size=(M, 1)) #
    opt_step = 0
    cost = np.inf
    last_cost = cost
    delta_cost = -cost
    gradient_hist = np.zeros((input_test.shape[0],M)) # gradient history for adaptive learning rate algorithm
    # print(f"U_F: \n{u_forecast}")   
    while delta_cost < -cost_tol:
        steps, y_forecast = compute_step(u_hist, y_hist, u_forecast)
        gradient_hist[opt_step, :] = steps[:,0]
        ada_grad = np.sqrt(np.sum(gradient_hist[:opt_step+1,:]**2,axis=0)+1e-10).reshape((M, 1))
        cost = cost_function(u_forecast, y_forecast, y_ref)
        delta_cost = cost - last_cost
        print(f"Opt step: {opt_step+1}")
        print(f"Cost: {cost}\n")
        # print(f"Steps: \n{steps}")
        if delta_cost < 0:
            u_forecast += (-lr/ada_grad)*steps
            u_forecast = np.clip(u_forecast, a_min=0.0, a_max=1.0)
            lr *= (1.0 - alpha)
            last_cost = cost
            opt_step += 1
        else:
            print("Passed optimal solution")
            break

    u_opt = u_forecast[0, :]
    # print(f"U_F: \n{u_forecast}")   
    # print(f"Y_F: \n{descale_output(y_forecast)}")
    # print(f"u_opt: {u_opt}")
    return u_opt, u_forecast, y_forecast, last_cost

# Filepaths
data_dir = "database/"
results_dir = "results/models/"

# ROSPY Parameters
pub_freq = 30  # sampling frequency of published data
step_time = 1 / pub_freq
total_steps = 10

# Load data
input_train, output_train, input_test, output_test = load_experiment(
    data_dir + 'experiment/', [1, 2, 3, 4, 5, 6], [7]
    )

output_test = output_test[:680]
input_test = input_test[:680]

# Scale database
input_scaling = "min-max"
output_scaling = "min-max"
if input_scaling == "mean-std":
    u_mean = input_test.mean(axis=0)
    u_std = input_test.std(axis=0)
elif input_scaling == "min-max":
    u_min = input_test.min(axis=0)
    u_max = input_test.max(axis=0)

if output_scaling == "mean-std":
    y_mean = output_test.mean(axis=0)
    y_std = output_test.std(axis=0)
elif output_scaling == "min-max":
    y_min = output_test.min(axis=0)
    y_max = output_test.max(axis=0)

# Experiment data
u = []
y = []
costs = []
errors = []

# Load metrics
metrics_df = pd.read_csv(results_dir + "experiment/hp_metrics.csv")
best_model_id = 121
best_model_filename = f"run_{best_model_id:03d}.keras"
best_params = metrics_df[metrics_df["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

# Load Keras model
keras_model = load_model(
    results_dir + f"experiment/best/{best_model_filename}"
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
y0_scaled = scale_output(y0)
y_hist = update_hist(y_hist, np.array(y0_scaled).reshape((1, 1)))

# Optimization parameters
lr = 1e-1 #1e-1
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
    u_opt, u_forecast, y_forecast, cost = optimization_function(u_hist, y_hist, lr, u_forecast)
    u_forecast[:-1] = u_forecast[1:]
    u_hist = update_hist(u_hist, u_opt.reshape((1, 1)))
    u_opt_descaled = descale_input(u_opt[0])
    u_opt_descaled = u_opt_descaled[0]
    u.append(u_opt_descaled)
    
    try:
        y_row = output_test[exp_step, 0]
        y.append(y_row) 
        y_row_scaled = scale_output(y_row)
        costs.append(cost)
        y_hist = update_hist(y_hist, np.array(y_row_scaled).reshape((1, 1)))
    except:
        pass
    exp_step += 1

u_array = np.array(u)
y_array = np.array(y)
costs = np.array(costs)
u_real = input_test.ravel()

def moving_avg(arr, k):
    return np.concatenate([u_array[:k-1], np.convolve(arr, np.ones(k)/k, mode='valid')])

k = 5
u_avg = moving_avg(u_array, k)

# plt.plot(u_array, label='original')
# plt.plot(u_avg, label='avg')
# plt.legend()
# plt.show()

# Convert to df
u = pd.DataFrame()
u['f'] = u_avg

y = pd.DataFrame()
y['w'] = y_array

# Split into train and test
test_split = 0.3
test_size = int(len(u)*test_split)

output_train_mpc = u.iloc[:-test_size, :]
output_test_mpc = u.iloc[-test_size:, :]
output_train_mpc.to_csv(data_dir + 'mpc/output_train.csv', index=False)
output_test_mpc.to_csv(data_dir + 'mpc/output_test.csv', index=False)

input_train_mpc = y.iloc[:-test_size, :]
input_test_mpc = y.iloc[-test_size:, :]
input_train_mpc.to_csv(data_dir + 'mpc/input_train.csv', index=False)
input_test_mpc.to_csv(data_dir + 'mpc/input_test.csv', index=False)

# Plot results
fig = plt.figure(figsize=(12, 10))
plt.title('Control comparison MPC x Experiment')
plt.step(x=range(u_real.shape[0]), y=u_real, color='k', label='experiment')
plt.step(x=range(u_array.shape[0]), y=u_array, color='r', label='mpc')
plt.step(x=range(u_avg.shape[0]), y=u_avg, color='b', label='mpc_avg')
plt.legend()
plt.tight_layout()
plt.show()