from python.gmaw_process import *
import numpy as np
import pandas as pd

# Paths
data_dir = "database/"

# Simulation parameters
step_time = 1e-05  # Simulation step time
sim_time = 1e-02  # Simulation time in seconds

# Generate time vectors
time = np.arange(0, sim_time + step_time, step_time).round(
    int(np.log10(1 / step_time))
)

# Dataset size
n_inputs = 2
n_outputs = 2
N = len(time)

# Input bounds
f_lv = 0  # Lower value for the binary signal
f_uv = fo  # Upper value for the binary signal
Ir_lv = 0.6 * Ir  # Lower value for the binary signal
Ir_uv = Ir  # Upper value for the binary signal
input_bounds = (f_lv, f_uv, Ir_lv, Ir_uv)


def generate_dataset(N, input_bounds, n_classes, x0):
    inputs = np.zeros((N, n_inputs))
    outputs = np.zeros((N, n_outputs))

    f_lv, f_uv, Ir_lv, Ir_uv = input_bounds
    # Generate a pseudo-random binary signal using the parameters
    f_binary_signal = np.random.randint(0, n_classes, size=N)
    Ir_binary_signal = np.random.randint(0, n_classes, size=N)
    f_signal = f_lv + (f_uv - f_lv) * f_binary_signal
    Ir_signal = Ir_lv + (Ir_uv - Ir_lv) * Ir_binary_signal
    inputs[:, 0] = f_signal
    inputs[:, 1] = Ir_signal

    outputs[0, :] = gmaw_outputs(x0)
    x = x0
    for i in range(1, time.shape[0]):
        u = inputs[i - 1, :]
        x = solve_rk4(gmaw_states, x, step_time, u)
        y = gmaw_outputs(x)
        outputs[i, :] = y
    return inputs, outputs


# initial state
x0 = [1e-10, 1e-10]
inputs_train, outputs_train = generate_dataset(N, input_bounds, 2, x0)
inputs_test, outputs_test = generate_dataset(N, input_bounds, 10, x0)

inputs_train = pd.DataFrame(inputs_train, columns=["f", "Ir"])
inputs_test = pd.DataFrame(inputs_test, columns=["f", "Ir"])
outputs_train = pd.DataFrame(outputs_train, columns=["we", "h"])
outputs_test = pd.DataFrame(outputs_test, columns=["we", "h"])

inputs_train.to_csv(data_dir + "inputs_train.csv", index=False)
inputs_test.to_csv(data_dir + "inputs_test.csv", index=False)
outputs_train.to_csv(data_dir + "outputs_train.csv", index=False)
outputs_test.to_csv(data_dir + "outputs_test.csv", index=False)
