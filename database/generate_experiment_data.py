import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

# File paths
data_dir = "database/experiment/"

# Functions
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

# Select train and test beads
beads_train = [1]
beads_test = [1]

# Get train and test data
inputs_train = []
outputs_train = []
inputs_test = []
outputs_test = []
for bead_idx in beads_train:
    filename_train = f"series/bead{bead_idx}"
    input_train = pd.read_csv(data_dir + filename_train + "_wfs.csv").to_numpy()
    output_train = pd.read_csv(
        data_dir + filename_train + "_w.csv"
    ).to_numpy()

    input_train = resample_data(
        input_train[:, 1], input_train[:, 0], output_train[:, 0]
    )
    inputs_train.append(input_train)
    outputs_train.append(output_train)

inputs_train = np.concatenate(inputs_train, axis=0)
inputs_train = pd.DataFrame(inputs_train, columns=['t', 'wfs'])
inputs_train.to_csv(data_dir + "inputs_train.csv", index=False)
outputs_train = np.concatenate(outputs_train, axis=0)
outputs_train = pd.DataFrame(outputs_train, columns=['t', 'w'])
outputs_train.to_csv(data_dir + "outputs_train.csv", index=False)

for bead_idx in beads_test:
    filename_test = f"series/bead{bead_idx}"
    input_test = pd.read_csv(data_dir + filename_test + "_wfs.csv").to_numpy()
    output_test = pd.read_csv(data_dir + filename_test + "_w.csv").to_numpy()

    input_test = resample_data(
        input_test[:, 1], input_test[:, 0], output_test[:, 0]
    )
    
    inputs_test.append(input_test)
    outputs_test.append(output_test)
    
inputs_test = np.concatenate(inputs_test, axis=0)
inputs_test = pd.DataFrame(inputs_test, columns=['t', 'wfs'])
inputs_test.to_csv(data_dir + "inputs_test.csv", index=False)
outputs_test = np.concatenate(outputs_test, axis=0)
outputs_test = pd.DataFrame(outputs_test, columns=['t', 'w'])
outputs_test.to_csv(data_dir + "outputs_test.csv", index=False)