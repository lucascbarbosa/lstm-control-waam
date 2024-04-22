import numpy as np
import pandas as pd
import control

# Paths
data_dir = "database/"


def generate_wfs(time, N, input_bounds, n_amps, min_diff=3):
    """
    Compute wfs commands.

    Args:
        N (int): number of commands
        input_bounds (tuple): lower and upper bounds of command
        n_amps (int): number of possible amplitudes for command
        min_diff (int): number of minimal change in amplitude of command

    Returns:
        np.array: wfs commands
    """
    f_lv, f_uv = input_bounds
    amps = np.arange(n_amps)
    f_step_signal = np.zeros(
        N,
    )
    f_step_signal[0] = amps[len(amps) // 2]
    for i in range(1, N):
        current_step = f_step_signal[i - 1]
        valid_amps = amps[
            np.where(
                (amps >= current_step + min_diff)
                | (amps <= current_step - min_diff)
            )
        ]
        f_step_signal[i] = np.random.choice(valid_amps)

    f_signal = f_lv + (f_uv - f_lv) * f_step_signal / (n_amps - 1)
    f_array = np.zeros((f_signal.shape[0], 2))
    f_array[:, 0] = time
    f_array[:, 1] = np.round(f_signal, 2)
    return f_array


def resample_wfs():
    resample_arrays = []
    for j in range(2):
        wfs_array = arrays[j]
        resample_wfs = np.zeros((sizes[j], 2))
        resample_wfs[:, 0] = sampling_times[j]
        for i in range(len(step_times[j])-1):
            start_index = int(step_times[j][i] / sampling_time)
            end_index = int(step_times[j][i+1] / sampling_time)
            resample_wfs[start_index:end_index,
                         1] = wfs_array[i, 1]
        resample_arrays.append(resample_wfs[:-1, :])
    return resample_arrays


def generate_w():
    w_arrays = []
    for j in range(2):
        wfs_array = resampled_arrays[j]
        x_k = np.zeros((2, 1))
        y = np.zeros(wfs_array.shape)
        y[:, 0] = wfs_array[:, 0]
        for i in range(1, len(wfs_array)):
            # WFS value
            u_k = wfs_array[i, 1]
            x_k = np.dot(ss_discrete.A, x_k) + np.dot(ss_discrete.B, u_k)
            y[i, 1] = np.dot(ss_discrete.C, x_k) + \
                np.dot(ss_discrete.D, u_k)
        w_arrays.append(y)
    return w_arrays


# Simulation parameters
sampling_time = 1e-02  # Simulation step time
step_time = 5
sim_time = 100  # Simulation time in seconds

# Generate time array
step_time_train = np.arange(0, sim_time + step_time, step_time).round(
    int(np.log10(1 / step_time))
)
train_size = len(step_time_train)
step_time_test = np.arange(0, sim_time + step_time, step_time).round(
    int(np.log10(1 / step_time))
)
test_size = len(step_time_test)

# Input bounds
f_lv = 5.1  # Lower value for the binary signal
f_uv = 8.7  # Upper value for the binary signal
input_bounds = (f_lv, f_uv)

# Generate input datasets
input_train = generate_wfs(step_time_train, train_size, input_bounds, 11)
input_test = generate_wfs(step_time_test, test_size, input_bounds, 11)

# Resample to sampling_time
sampling_time_train = np.arange(0, sim_time + sampling_time, sampling_time).round(
    int(np.log10(1 / sampling_time))
)
train_size = len(sampling_time_train)
sampling_time_test = np.arange(0, sim_time + sampling_time, sampling_time).round(
    int(np.log10(1 / sampling_time))
)
test_size = len(sampling_time_test)


# Train/test sets
sizes = [train_size, test_size]
arrays = [input_train, input_test]
step_times = [step_time_train, step_time_test]
sampling_times = [sampling_time_train, sampling_time_test]
# Resample inputs
input_train, input_test = resample_wfs()
resampled_arrays = [input_train, input_test]

# Create tf
numerator = [0, 0, 0.8]
denominator = [0.2, 1.2, 1]
G_continuous = control.TransferFunction(numerator, denominator)

# Discretize the transfer function using Tustin's method
G_discrete = control.sample_system(G_continuous, step_time, method='tustin')

# Convert to ss
ss_discrete = control.tf2ss(G_discrete)

# Generate outputs
output_train, output_test = generate_w()


# Random noise
output_train[:, 1] += np.random.normal(loc=0,
                                       scale=output_train[-1, 1]/100,
                                       size=output_train.shape[0])

output_test[:, 1] += np.random.normal(loc=0,
                                      scale=output_test[-1, 1]/100,
                                      size=output_test.shape[0])

# Generate datafranes
input_train = pd.DataFrame(input_train, columns=['t', 'f'])
output_train = pd.DataFrame(output_train, columns=['t', 'w'])
input_test = pd.DataFrame(input_test, columns=['t', 'f'])
output_test = pd.DataFrame(output_test, columns=['t', 'w'])

input_train.to_csv(data_dir + f"simulation/input_train.csv", index=False)
input_test.to_csv(data_dir + f"simulation/input_test.csv", index=False)
output_train.to_csv(data_dir + f"simulation/output_train.csv", index=False)
output_test.to_csv(data_dir + f"simulation/output_test.csv", index=False)
