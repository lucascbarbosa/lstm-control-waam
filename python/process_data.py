import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import os
from scipy.interpolate import interp1d


def load_simulation(data_dir):
    inputs_train = pd.read_csv(data_dir + "inputs_train.csv").to_numpy()
    outputs_train = pd.read_csv(data_dir + "outputs_train.csv").to_numpy()
    inputs_test = pd.read_csv(data_dir + "inputs_test.csv").to_numpy()
    outputs_test = pd.read_csv(data_dir + "outputs_test.csv").to_numpy()
    return inputs_train, outputs_train, inputs_test, outputs_test

def load_experiment(data_dir, idxs_train, idxs_test):
    inputs_train = []
    outputs_train = []
    inputs_test = []
    outputs_test = []
    
    for idx_train in idxs_train:
        filename_train = f"bead{idx_train}"
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
    outputs_train = np.concatenate(outputs_train, axis=0)
    
    for idx_test in idxs_test:
        filename_test = f"bead{idx_test}"
        input_test = pd.read_csv(data_dir + filename_test + "_wfs.csv").to_numpy()
        output_test = pd.read_csv(data_dir + filename_test + "_w.csv").to_numpy()

        input_test = resample_data(
            input_test[:, 1], input_test[:, 0], output_test[:, 0]
        )
        
        inputs_test.append(input_test)
        outputs_test.append(output_test)
        
    inputs_test = np.concatenate(inputs_test, axis=0)
    outputs_test = np.concatenate(outputs_test, axis=0)

    return (
        inputs_train[:, 1:],
        outputs_train[:, 1:],
        inputs_test[:, 1:],
        outputs_test[:, 1:],
    )

def load_mpc(data_dir):
    input_train = pd.read_csv(data_dir + "input_train.csv").to_numpy()
    output_train = pd.read_csv(data_dir + "output_train.csv").to_numpy()
    input_test = pd.read_csv(data_dir + "input_test.csv").to_numpy()
    output_test = pd.read_csv(data_dir + "output_test.csv").to_numpy()
    return input_train, output_train, input_test, output_test

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

def standardize_data(x):
    # Process database
    scaler = StandardScaler()
    x = scaler.fit_transform(x)
    return x


def normalize_data(x):
    scaler = MinMaxScaler()
    x = scaler.fit_transform(x)
    return x


def destandardize_data(x, mean, std):
    return (x * std) + mean


def denormalize_data(x, min_val, max_val):
    return x * (max_val - min_val) + min_val


def sequence_data(X, Y, P, Q, H):
    """
    P: Inputs sequence length
    Q: Outputs sequence length
    H: Forecast horizon
    """
    X_seq = np.zeros((len(X) - max(P - 1, Q) - H + 1, (P + Q) * X.shape[1], 1))
    Y_seq = np.zeros((len(X) - max(P - 1, Q) - H + 1, X.shape[1]))
    for i in range(0, len(X) - max(P - 1, Q) - H + 1):
        X_seq[i, :, 0] = np.hstack(
            (
                X[i : i + P, :].ravel(),
                Y[i : i + Q, :].ravel(),
            )
        )
        Y_seq[i, :] = Y[i + Q + H - 1, :]

    return X_seq, Y_seq


# def sequence_data(X, Y, P, Q, H):
#     """
#     P: Inputs sequence length
#     Q: Outputs sequence length
#     H: Forecast horizon
#     """
#     X_seq = np.zeros((len(X) - max(P - 1, Q) - H + 1, P + Q, X.shape))
#     Y_seq = np.zeros((len(X) - max(P - 1, Q) - H + 1, X.shape[1]))
#     for i in range(0, len(X) - max(P - 1, Q) - H + 1):
#         X_seq[i, :, :] = np.vstack(
#             (X[i : i + P, :], Y[i : i + Q, :])
#         )
#         Y_seq[i, :] = Y[i + Q + H - 1, :]

#     return X_seq, Y_seq

# data_dir = "database/"
# input_train, output_train, input_test, output_test = load_experiment(data_dir + "experiment/", [1,2,3,4,5,6], [7])
# P, Q, H = 5, 5, 1
# X_train, Y_train = sequence_data(input_train, output_train, P, Q, H)
