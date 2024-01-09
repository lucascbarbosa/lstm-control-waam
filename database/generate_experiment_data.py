import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

# Paths
data_dir = "database/"

# Experiment parameters
step = 1
traj_length = 300 # total length
travel_speed = 10 # travel speed (mm/s)
exp_time = traj_length / travel_speed  # Total experiment time

# Generate time vectors
time = np.arange(0, exp_time + step, step).tolist()

# Dataset size
n_inputs = 1
n_outputs = 1
N = len(time)

# Input bounds
f_lv = 5.1  # 40% (m/min)
f_uv = 8.7 # 80% (m/min)
input_bounds = (f_lv, f_uv)

def generate_wfs(N, input_bounds, n_classes):
    f_lv, f_uv = input_bounds
    f_binary_signal = np.random.randint(0, n_classes+1, size=N) / n_classes
    f_signal = f_lv + (f_uv - f_lv) * f_binary_signal
    return f_signal.tolist()

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

# initial state
inputs_train = generate_wfs(N, input_bounds, 10)
inputs_test = generate_wfs(N, input_bounds, 10)

inputs_train = pd.DataFrame({'t': time, 'f': inputs_train})
inputs_test = pd.DataFrame({'t': time, 'f': inputs_test})

inputs_train.to_csv(data_dir + f"experiment/inputs_train.csv", index=False)
inputs_test.to_csv(data_dir + f"experiment/inputs_test.csv", index=False)
