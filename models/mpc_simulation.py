import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam

from models.process_data import load_train_data
import pandas as pd
import numpy as np
import time
import control

# Paths
data_dir = "database/"
results_dir = "results/"

# Load data
(process_input_train,
 process_output_train,
 process_input_test,
 _) = load_train_data(data_dir + "experiment/calibration/")

process_input_train = process_input_train[:, 1:]
process_output_train = process_output_train[:, 1:]

u_min = process_input_train.min(axis=0)
u_max = process_input_train.max(axis=0)
y_min = process_output_train.min(axis=0)
y_max = process_output_train.max(axis=0)

process_inputs = process_input_train.shape[1]
process_outputs = process_output_train.shape[1]

# Load model
metrics_process = pd.read_csv(results_dir +
                              f"models/experiment/hp_metrics.csv"
                              )
process_best_model_id = 26
process_best_model_filename = f"run_{process_best_model_id:03d}.keras"
process_best_params = metrics_process[
    metrics_process["run_id"] == int(process_best_model_id)
]
P = process_best_params.iloc[0, 1]
Q = process_best_params.iloc[0, 2]

# Load process model
model = load_model(
    results_dir +
    f"models/experiment/best/{process_best_model_filename}"
)

opt = Adam(learning_rate=process_best_params["lr"])
model.compile(optimizer=opt, loss=mean_squared_error)

# Define MPC optimization parameters
M = P   # control horizon
N = Q  # prediction horizon
weight_control = 1.0
weight_output = 10.0
lr = 1e-1
alpha_time = 1e-2
alpha_opt = 1e-2
cost_tol = 1e-3

# Define TS and width reference
ts = 8
ts_scaled = (ts - u_min[1]) / \
    (u_max[1] - u_min[1])
y_ref = 9.0
y_ref_scaled = (y_ref - y_min) / \
    (y_max - y_min)

# Historic data
u_hist = np.zeros((P, process_inputs))
u_hist[:, :] = [0.0, ts_scaled]
y_hist = np.zeros((Q, process_outputs))

u_forecast = np.full((M, 1), 0.0)
u_forecast_data = []
y_forecast_data = []

# Define plant model
with open(results_dir + f'models/tf/ts_{ts}.txt', 'r') as f:
    gain = float(f.read())
fs = 5.0
numerator = [0, 0, gain]
denominator = [0.2, 1.2, 1]
T = 1 / fs
G_continuous = control.TransferFunction(numerator, denominator)
G_discrete = control.sample_system(
    G_continuous, T, method='tustin')
ss_discrete = control.tf2ss(G_discrete)


def pow2wfs(self, p):
    return np.round((p*9/100)+1.5, 3)


def wfs2pow(self, f):
    return np.round((f-1.5)*100/9)


def update_hist(current_hist, new_states):
    new_hist = current_hist.copy()
    len_new = new_states.shape[0]
    new_hist[:-len_new, :] = current_hist[len_new:, :]
    new_hist[-len_new:, :] = new_states
    return new_hist


def build_sequence(u_hist, y_hist):
    u = u_hist.ravel()
    y = y_hist.ravel()
    P = u_hist.shape[0]
    Q = y_hist.shape[0]
    sequence = np.hstack((u, y)).reshape(
        (1, P * process_inputs + Q * process_outputs, 1))
    return sequence


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


def cost_function(u_forecast, y_forecast):
    u_diff_forecast = create_control_diff(u_forecast)
    output_error = (y_ref_scaled - y_forecast) * \
        (y_max-y_min)

    output_cost = np.sum(output_error**2 * weight_output)
    control_cost = np.sum(u_diff_forecast**2 * weight_control)
    return output_cost + control_cost


def compute_gradient(input_tensor, j):
    # start_time = time.time()
    with tf.GradientTape() as t:
        t.watch(input_tensor)
        output_tensor = model(input_tensor)
        gradient = t.gradient(
            output_tensor[:, j], input_tensor
        ).numpy()[0, :, 0]
    # print(time.time() - start_time)
    return output_tensor, gradient


def split_gradient(grad):
    grad = grad.reshape(
        (P * process_inputs + Q * process_outputs,))
    u = grad[: process_inputs *
             P].reshape((P, process_inputs))
    y = grad[process_inputs *
             P:].reshape((Q, process_outputs))
    return u[:, 0], y


def compute_step(u_hist, y_hist, u_forecast):
    u_forecast = u_forecast.copy()
    u_hist = u_hist.copy()
    y_hist = y_hist.copy()
    output_jacobian = np.zeros((N, M))
    y_forecast = np.zeros((N, 1))
    for i in range(N):
        if i < M:
            u_row = np.array([[u_forecast[i, 0], ts]])
        if i >= M:
            u_row = np.array([[u_forecast[-1, 0], ts]])
        u_hist = update_hist(u_hist, u_row)
        seq_input = build_sequence(u_hist, y_hist)
        input_tensor = tf.convert_to_tensor(seq_input, dtype=tf.float32)
        for j in range(process_outputs):
            output_tensor, gradient = compute_gradient(
                input_tensor, j)
            input_gradient, _ = split_gradient(gradient)

            if i < P - 1:
                output_jacobian[i, : i + 1] = input_gradient[-(i + 1):]
            else:
                output_jacobian[i, :] = input_gradient[:]

        y_row = output_tensor.numpy().reshape((1, 1))
        y_forecast[i, :] = y_row
        y_hist = update_hist(y_hist, y_row)

    input_jacobian = build_input_jacobian()
    steps = np.zeros(u_forecast.shape)
    u_diff_forecast = create_control_diff(u_forecast)
    output_error = (y_ref_scaled - y_forecast)
    input_diff = u_diff_forecast

    for j in range(M):
        output_step = (
            -2
            * np.diag(output_error.T @ output_jacobian[:, j])
            * weight_output
        )
        input_step = (
            2 * input_jacobian[:, j].T @ input_diff * weight_control
        )

        total_step = output_step + input_step
        steps[j, 0] = total_step

    return steps, y_forecast


def optimization_function(u_forecast, lr):
    current_time = np.round(time.time(), 1)
    opt_step = 1
    cost = np.inf
    last_cost = cost
    delta_cost = -cost
    # gradient history for adaptive learning rate algorithm
    gradient_hist = np.zeros((process_input_test.shape[0], M))
    gradient_hist = []
    lr = lr
    while delta_cost < -cost_tol and opt_step < 15:
        steps, y_forecast = compute_step(u_hist, y_hist, u_forecast)
        cost = cost_function(u_forecast, y_forecast)
        delta_cost = cost - last_cost
        gradient_hist.append(steps[:, 0].ravel().tolist())
        ada_grad = np.sqrt(np.sum(np.array(gradient_hist)[
            :opt_step, :]**2, axis=0)+1e-10).reshape((M, 1))
        if verbose:
            print(f"Opt step: {opt_step} Cost: {cost}")
        if delta_cost < 0:
            u_forecast += (-lr/ada_grad)*steps
            u_forecast = np.clip(
                u_forecast, a_min=0.0, a_max=1.0)
            lr = lr * (1.0 - alpha_opt)
            last_cost = cost
        else:
            if verbose:
                print("Passed optimal solution")
            break
        opt_step += 1

    opt_time = time.time() - current_time
    print(f"Steps: {opt_step} Time: {opt_time:.2f} " +
          f"Time per step: {opt_time/opt_step:.2f} " +
          f"Time per grad: {opt_time/(opt_step*N):.3f}")

    print(
        f"U_F: {u_forecast * (u_max[0] - u_min[0]) + u_min[0]}")
    print(
        f"Y_F: {y_forecast * (y_max - y_min) + y_min}")
    print(
        f"Y_R: {y_ref_scaled * (y_max - y_min) + y_min}")

    # Save forecast
    u_forecast_data.append(u_forecast.ravel().tolist())
    y_forecast_data.append(y_forecast.ravel().tolist())

    return u_forecast, y_forecast


def predict_output(x, u):
    x = np.dot(ss_discrete.A, x) + \
        np.dot(ss_discrete.B, u)
    y = list(np.dot(ss_discrete.C, x) +
             np.dot(ss_discrete.D, u))[0]
    return x, y


verbose = True
exp_step = 0
exp_time = 0.0
exp_horizon = 100
x_row = np.zeros((2, 1))
y_row = np.zeros((1, 1))
while exp_step < exp_horizon:
    u_forecast, y_forecast = optimization_function(u_forecast, lr)
    u_opt = u_forecast[0, 0]
    u_opt_descaled = u_opt * \
        (u_max[0] - u_min[0]) + u_min[0]
    x_row, y_row = predict_output(x_row, u_opt_descaled)
    y_row_scaled = (y_row - y_min) / (y_max - y_min)
    print(
        f"Experiment step {exp_step} ({np.round(exp_time, 2)} s): Control {np.round(u_opt_descaled, 2)} Width {np.round(y_row, 2)}")

    # Updates
    u_forecast[:-1] = u_forecast[1:]

    # Updates learning rate
    lr = lr * (1.0 - alpha_time)

    # Updates hists
    u_hist = update_hist(u_hist, np.array([[u_opt, ts_scaled]]))
    y_hist = update_hist(y_hist, np.array([[y_row_scaled]]))
    exp_time += np.round(T, 1)
    exp_step += 1
