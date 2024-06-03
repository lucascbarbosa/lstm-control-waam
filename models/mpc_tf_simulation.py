"""MPC Simulation."""
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


def build_input_jacobian():
    input_jacobian = np.eye(M)
    for i in range(M):
        if i < M - 1:
            input_jacobian[i + 1, i] = -1
    return input_jacobian


def create_control_diff(u_forecast):
    u_diff = u_forecast.copy()
    u_diff[1:] = u_diff[1:] - u_diff[:-1]
    return u_diff


def cost_function(u_forecast, y_forecast):
    output_error = y_ref[exp_step:exp_step+N] - y_forecast
    output_cost = np.sum(output_error**2 * weight_output)

    u_diff_forecast = create_control_diff(u_forecast)
    control_cost = np.sum(u_diff_forecast**2 * weight_control)
    return output_cost,  control_cost


def create_control_vector(i):
    control_vector = np.zeros(N-i-1)
    for i in range(control_vector.shape[0]):
        control_vector[i] = np.dot(
            model_ss.C,
            np.dot(
                np.linalg.matrix_power(model_ss.A, i+1),
                model_ss.B
            )
        )
    return control_vector


def compute_step(x_row, u_forecast):
    u_forecast = u_forecast.copy()
    output_jacobian = np.zeros((N, M))
    y_forecast = np.zeros((N, 1))
    for i in range(N):
        if i < M:
            u_row = u_forecast[i, 0]
        if i >= M:
            u_row = u_forecast[-1, 0]
        for j in range(process_outputs):
            x_row, y_row = predict_output(model_ss, x_row, u_row)
            output_jacobian[i, i] = model_ss.D
            output_jacobian[i+1:, i] = create_control_vector(i)
            y_forecast[i, :] = y_row

    input_jacobian = build_input_jacobian()
    steps = np.zeros(u_forecast.shape)
    u_diff_forecast = create_control_diff(u_forecast)
    output_error = y_ref[exp_step:exp_step+N] - y_forecast
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


def optimization_function(x_row, u_forecast, gradient_hist):
    current_time = np.round(time.time(), 1)
    opt_step = 1
    cost = 99999999
    last_cost = cost
    delta_cost = -cost
    initial_cost = cost
    while delta_cost/initial_cost < -cost_tol:
        steps, y_forecast = compute_step(x_row, u_forecast)
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
                u_forecast, a_min=u_min, a_max=u_max)
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

    print(f"U_F: {u_forecast}")
    print(f"Y_F: {y_forecast}")
    print(f"Y_R: {y_ref[exp_step:exp_step+N]}")

    return u_forecast, y_forecast, last_input_cost, last_output_cost


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


def sine_reference(period, mean, amp):
    signal = mean + np.sin((2*np.pi/period) *
                           np.arange(0, (exp_horizon+N)*T, T)) * amp
    signal = signal.reshape((exp_horizon+N, 1))
    return signal


def predict_output(model, x, u):
    u = np.sqrt(u)
    x = np.dot(model.A, x) +\
        np.dot(model.B, u)
    y = list(np.dot(model.C, x) +
             np.dot(model.D, u))[0]
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

u_min = input_train.min(axis=0)[0]
u_max = input_train.max(axis=0)[0]

process_inputs = input_train.shape[1]
process_outputs = output_train.shape[1]

# Define MPC optimization parameters
M = 30  # control horizon
N = 30  # prediction horizon
weight_control = 0.1
weight_output = 100  # 1
lr = 1e0
cost_tol = 1e-3

reference = "step"
for ts in [4, 8, 12, 16, 20]:
    # Forecast
    u_forecast = np.full((M, 1), 0.5)
    # u_forecast = np.linspace(1.0, 0.0, M).reshape((M, 1))

    # Define plant model
    ts_gain = pd.read_csv(results_dir + "models/plant.csv")
    gain = ts_gain[ts_gain["TS"] == ts].values[0, 1]
    fs = 5.0
    numerator = [0, 0, gain]
    denominator = [0.2, 1.2, 1]
    T = 1 / fs
    plant_continuous = control.TransferFunction(numerator, denominator)
    plant_discrete = control.sample_system(
        plant_continuous, T, method='tustin')
    plant_ss = control.tf2ss(plant_discrete)

    # Define MPC model
    desvio = 0.95
    numerator = [0, 0, gain*desvio]
    denominator = [0.2, 1.2, 1]
    model_continuous = control.TransferFunction(numerator, denominator)
    model_discrete = control.sample_system(
        model_continuous, T, method='tustin')
    model_ss = control.tf2ss(model_discrete)

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
    exp_horizon = 60
    x_row = np.zeros((2, 1))
    y_row = np.zeros((1, 1))
    mpc_state = False
    time_array = []

    # Historic gradient for adagrad
    gradient_hist = np.zeros((M, 1))

    # Set reference
    ref_min = gain * np.sqrt(u_min)
    ref_max = gain * np.sqrt(u_max)
    ref_mean = (ref_max + ref_min) / 2

    if reference == "sine":
        y_ref = sine_reference(20*T, ref_mean, ref_mean*0.1)
    elif reference == "step":
        y_ref = step_reference(ref_mean)

    x_row = np.zeros((2, 1))
    while exp_step <= exp_horizon:
        (u_forecast, y_forecast, input_cost,
         output_cost) = optimization_function(x_row, u_forecast, gradient_hist)
        cost = input_cost + output_cost
        u_opt = u_forecast[0, 0]

        x_row, y_row = predict_output(plant_ss, x_row, u_opt)
        print(
            f"Experiment step {exp_step}({np.round(exp_time, 2)} s): Control {np.round(u_opt, 2)} Width {np.round(y_row[0], 3)} \n\n")

        # Save data
        t = np.round(exp_time, 2)
        wfs_data.append({'t': t, 'wfs_command': u_opt})
        ts_data.append({'t': t, 'ts_command': ts})
        w_data.append({'t': t, 'w': y_row[0]})
        cost_data.append({'t': t, 'input_cost': input_cost,
                          'output_cost': output_cost})
        u_forecast_data.append(u_forecast.ravel().tolist())
        y_forecast_data.append(y_forecast.ravel().tolist())

        # Updates forecast
        u_forecast[:-1] = u_forecast[1:]

        # Iterate time
        exp_time += np.round(T, 1)
        exp_step += 1

    # Time series data
    wfs_df = pd.DataFrame(wfs_data)
    wfs_df.to_csv(data_dir + f'simulation/control/tf__ts_{ts}__{reference}__wfs_command.csv',
                  index=False)
    ts_df = pd.DataFrame(ts_data)
    ts_df.to_csv(data_dir + f'simulation/control/tf__ts_{ts}__{reference}__ts_command.csv',
                 index=False)
    w_df = pd.DataFrame(w_data)
    w_df.to_csv(data_dir + f'simulation/control/tf__ts_{ts}__{reference}__w.csv',
                index=False)

    ref_df = pd.DataFrame()
    ref_df['t'] = w_df['t']
    ref_df['r'] = y_ref[:len(w_data)]
    ref_df.to_csv(
        data_dir +
        f'simulation/control/tf__ts_{ts}__{reference}__reference.csv',
        index=False)

    # MPC data
    cost_df = pd.DataFrame(cost_data)
    cost_df.to_csv(data_dir + f'simulation/control/tf__ts_{ts}__{reference}__cost.csv',
                   index=False)
    mpc_time = cost_df['t'].to_numpy().reshape((-1, 1))

    u_forecast_cols, y_forecast_cols = name_forecast_cols()
    u_forecast_array = np.array(u_forecast_data)
    u_forecast_array = np.hstack((mpc_time, u_forecast_array))
    u_forecast_df = pd.DataFrame(u_forecast_array,
                                 columns=u_forecast_cols)
    u_forecast_df.to_csv(
        results_dir +
        f'predictions/simulation/control/tf__ts_{ts}__{reference}__u_forecast.csv',
        index=False)

    y_forecast_array = np.array(y_forecast_data)
    y_forecast_array = np.hstack((mpc_time, y_forecast_array))

    y_forecast_df = pd.DataFrame(y_forecast_array,
                                 columns=y_forecast_cols)
    y_forecast_df.to_csv(
        results_dir +
        f'predictions/simulation/control/tf__ts_{ts}__{reference}__y_forecast.csv',
        index=False)
