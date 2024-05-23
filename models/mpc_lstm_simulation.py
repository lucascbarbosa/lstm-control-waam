"""MPC Simulation."""
import tensorflow as tf
from keras.models import load_model
from models.process_data import load_train_data
import pandas as pd
import numpy as np
import control
import time
#############
# Functions #


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
    output_error = (y_ref_scaled[exp_step:exp_step+N] - y_forecast) * \
        (y_max - y_min)

    output_cost = np.sum(output_error**2 * weight_output)
    control_cost = np.sum(u_diff_forecast**2 * weight_control)
    return output_cost,  control_cost


def compute_gradient(input_tensor, j):
    with tf.GradientTape() as t:
        t.watch(input_tensor)
        output_tensor = process_model(input_tensor)
        gradient = t.gradient(
            output_tensor[:, j], input_tensor
        ).numpy()[0, :, 0]
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
            u_row = np.array([[u_forecast[i, 0], ts_scaled]])
        if i >= M:
            u_row = np.array([[u_forecast[-1, 0], ts_scaled]])
        u_hist = update_hist(u_hist, u_row)
        seq_input = build_sequence(u_hist, y_hist)
        input_tensor = tf.convert_to_tensor(seq_input, dtype=tf.float32)
        for j in range(process_outputs):
            output_tensor, gradient = compute_gradient(
                input_tensor, j)
            gradient, _ = split_gradient(gradient)
            if i < P - 1:
                output_jacobian[i, : i + 1] = gradient[-min((i + 1), M):]
            else:
                output_jacobian[i, :] = gradient[-M:]

        y_row = output_tensor.numpy().reshape((1, 1))
        y_forecast[i, :] = y_row
        y_hist = update_hist(y_hist, y_row)

    input_jacobian = build_input_jacobian()
    steps = np.zeros(u_forecast.shape)
    u_diff_forecast = create_control_diff(u_forecast)
    output_error = y_ref_scaled[exp_step:exp_step+N] - y_forecast
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
    cost = 99999999
    last_cost = cost
    delta_cost = -cost
    initial_cost = cost
    # gradient history for adaptive learning rate algorithm
    gradient_hist = np.zeros((M, 1))
    lr = lr
    while delta_cost/initial_cost < -cost_tol and opt_step <= 50:
        steps, y_forecast = compute_step(u_hist, y_hist, u_forecast)
        output_cost, input_cost = cost_function(u_forecast, y_forecast)
        cost = output_cost + input_cost
        delta_cost = cost - last_cost
        gradient_hist += steps ** 2
        ada_grad = np.sqrt(gradient_hist + 1e-10)
        if verbose:
            print(f"Opt step: {opt_step} Cost: {cost}")
        if delta_cost < 0:
            u_forecast += (-lr/ada_grad)*steps
            u_forecast = np.clip(
                u_forecast, a_min=0.0, a_max=1.0)
            last_cost = cost
            last_input_cost = input_cost
            last_output_cost = output_cost
            if opt_step == 1:
                initial_cost = cost
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
        f"Y_R: {y_ref_scaled[exp_step:exp_step+N] * (y_max - y_min) + y_min}")

    return (u_forecast, y_forecast,
            last_input_cost, last_output_cost)


def step_reference(amps):
    if type(amps) is list:
        i = 0
        y_ref = np.zeros((exp_horizon+N, 1))
        for amp in amps:
            y_ref[i*int(exp_horizon/len(amps)):
                  (i+1) * int(exp_horizon/len(amps))] = amp
            i += 1
        y_ref[y_ref == 0.0] = amps[-1]
    else:
        y_ref = np.full(((exp_horizon+N), 1), amps)
    return y_ref


def sine_reference(mean, w, amp):
    y_ref = mean + np.sin(w*np.arange(0, (exp_horizon+N)*T, T)) * amp
    y_ref = y_ref.reshape((exp_horizon+N, 1))
    return y_ref


def predict_output(x, u):
    u = np.sqrt(u)
    x = np.dot(ss_discrete.A, x) + \
        np.dot(ss_discrete.B, u)
    y = list(np.dot(ss_discrete.C, x) +
             np.dot(ss_discrete.D, u))[0]
    return x, y


def name_forecast_cols():
    u_forecast_list = ['t'] + ["u_forecast_" +
                               str(i).zfill(2)
                               for i in range(1, M+1)]
    y_forecast_list = ['t'] + ["y_forecast_" +
                               str(i).zfill(2)
                               for i in range(1, N+1)]
    return u_forecast_list, y_forecast_list


# Paths
data_dir = "database/"
results_dir = "results/"

# Load process data
list_input_train = []
list_input_test = []
list_output_train = []
list_output_test = []
for ts in [4, 8, 12, 16, 20]:
    input_train, output_train, input_test, output_test = load_train_data(
        data_dir + f"simulation/calibration/TS {ts}/"
    )
    list_input_train.append(input_train)
    list_input_test.append(input_test)
    list_output_train.append(output_train)
    list_output_test.append(output_test)

input_train = np.concatenate(list_input_train)
input_test = np.concatenate(list_input_test)
output_train = np.concatenate(list_output_train)
output_test = np.concatenate(list_output_test)

input_train = input_train[:, 1:]
output_train = output_train[:, 1:]

u_min = input_train.min(axis=0)
u_max = input_train.max(axis=0)
y_min = output_train.min(axis=0)
y_max = output_train.max(axis=0)

process_inputs = input_train.shape[1]
process_outputs = output_train.shape[1]

# Load process model
metrics_process = pd.read_csv(
    results_dir + "models/simulation/hp_metrics.csv"
)
best_process_model_id = 21
best_process_model_filename = f"run_{best_process_model_id:03d}.keras"
best_params = metrics_process[
    metrics_process["run_id"] == int(best_process_model_id)
]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

process_model = load_model(
    results_dir +
    f"models/simulation/best/{best_process_model_filename}"
)

# Define MPC optimization parameters
M = P  # control horizon
N = P  # prediction horizon
weight_control = 1.0
weight_output = 100
lr = 1e-1
cost_tol = 1e-6
alpha = 0.33

# Define TS and width reference
for ts in [4, 8, 12, 16, 20]:
    ts_scaled = (ts - u_min[1]) / \
        (u_max[1] - u_min[1])

    # Historic data
    u_hist = np.zeros((P, process_inputs))
    u_hist[:, :] = [0.0, ts_scaled]
    y_hist = np.zeros((Q, process_outputs))
    y_hist[-1, 0] = -y_min/(y_max - y_min)

    u_forecast = np.full((M, 1), 0.0)

    ts_gain = pd.read_csv(results_dir + "models/plant.csv")
    gain = ts_gain[ts_gain["TS"] == ts].values[0, 1]
    fs = 5.0
    numerator = [0, 0, gain]
    denominator = [0.2, 1.2, 1]
    T = 1 / fs
    G_continuous = control.TransferFunction(numerator, denominator)
    G_discrete = control.sample_system(
        G_continuous, T, method='tustin')
    ss_discrete = control.tf2ss(G_discrete)

    # Data arrays
    wfs_data = []
    ts_data = []
    w_data = []
    cost_data = []
    u_forecast_data = []
    y_forecast_data = []

    verbose = True
    exp_step = 1
    exp_time = 0.2

    # exp_horizon = 340/(ts*0.2)
    exp_horizon = 50
    x_row = np.zeros((2, 1))
    y_row_descaled = np.zeros((1, 1))
    mpc_state = False
    time_array = []

    # Set reference
    ref_min = gain * np.sqrt(u_min[0])
    ref_max = gain * np.sqrt(u_max[0])
    y_ref = (ref_max + ref_min) / 2
    y_ref = step_reference(y_ref)
    y_ref_scaled = (y_ref - y_min) / \
        (y_max - y_min)
    while exp_step <= exp_horizon:
        u_forecast, y_forecast, input_cost, output_cost = optimization_function(
            u_forecast, lr)
        cost = input_cost + output_cost
        u_opt = u_forecast[0, 0]

        # Updates learning rate
        lr = lr * (1.0 - alpha)

        u_opt_descaled = u_opt * \
            (u_max[0] - u_min[0]) + u_min[0]
        x_row, y_row_descaled = predict_output(x_row, u_opt_descaled)
        y_row_scaled = (y_row_descaled - y_min) / \
            (y_max - y_min)
        print(
            f"Experiment step {exp_step}({np.round(exp_time, 2)} s): Control {np.round(u_opt_descaled, 2)} Width {np.round(y_row_descaled[0], 3)} \n\n")

        # Updates hists
        u_hist = update_hist(u_hist, np.array([[u_opt, ts_scaled]]))
        y_hist = update_hist(y_hist, np.array([[y_row_scaled]]))
        exp_time += np.round(T, 1)
        exp_step += 1

        # Save data
        t = np.round(exp_time, 2)
        wfs_data.append({'t': t, 'wfs_command': u_opt_descaled})
        ts_data.append({'t': t, 'ts_command': ts})
        w_data.append({'t': t, 'w': y_row_descaled[0]})
        cost_data.append({'t': t, 'input_cost': input_cost,
                          'output_cost': output_cost})
        u_forecast_data.append(u_forecast.ravel().tolist())
        y_forecast_data.append(y_forecast.ravel().tolist())

        # Updates forecast
        u_forecast[:-1] = u_forecast[1:]

    # Time series data
    wfs_df = pd.DataFrame(wfs_data)
    wfs_df.to_csv(data_dir + f'simulation/control/ts_{ts}__step__wfs_command.csv',
                  index=False)
    ts_df = pd.DataFrame(ts_data)
    ts_df.to_csv(data_dir + f'simulation/control/ts_{ts}__step__ts_command.csv',
                 index=False)
    w_df = pd.DataFrame(w_data)
    w_df.to_csv(data_dir + f'simulation/control/ts_{ts}__step__w.csv',
                index=False)

    ref_df = pd.DataFrame()
    ref_df['t'] = w_df['t']
    ref_df['r'] = y_ref[0, 0]
    ref_df.to_csv(
        data_dir + f'simulation/control/ts_{ts}__step__reference.csv',
        index=False)

    # MPC data
    cost_df = pd.DataFrame(cost_data)
    mpc_time = cost_df['t'].to_numpy().reshape((-1, 1))

    u_forecast_cols, y_forecast_cols = name_forecast_cols()
    u_forecast_array = np.array(u_forecast_data)
    u_forecast_array = u_forecast_array * (
        u_max[0] - u_min[0]) + u_min[0]
    u_forecast_array = np.hstack((mpc_time, u_forecast_array))
    u_forecast_df = pd.DataFrame(u_forecast_array,
                                 columns=u_forecast_cols)
    u_forecast_df.to_csv(
        results_dir +
        f'predictions/simulation/control/ts_{ts}__step__u_forecast.csv',
        index=False)

    y_forecast_array = np.array(y_forecast_data)
    y_forecast_array = y_forecast_array * (
        y_max[0] - y_min[0]) + y_min[0]
    y_forecast_array = np.hstack((mpc_time, y_forecast_array))

    y_forecast_df = pd.DataFrame(y_forecast_array,
                                 columns=y_forecast_cols)
    y_forecast_df.to_csv(
        results_dir +
        f'predictions/simulation/control/ts_{ts}__step__y_forecast.csv',
        index=False)
