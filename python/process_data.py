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


def load_experiment(data_dir, idx_train, idx_test):
    filename_train = f"bead{idx_train}"
    input_train = pd.read_csv(data_dir + filename_train + "_wfs.csv").to_numpy()
    output_train = pd.read_csv(
        data_dir + filename_train + "_w.csv"
    ).to_numpy()

    input_train = resample_data(
        input_train[:, 1], input_train[:, 0], output_train[:, 0]
    )

    filename_test = f"bead{idx_test}"
    input_test = pd.read_csv(data_dir + filename_test + "_wfs.csv").to_numpy()
    output_test = pd.read_csv(data_dir + filename_test + "_w.csv").to_numpy()

    input_test = resample_data(
        input_test[:, 1], input_test[:, 0], output_test[:, 0]
    )

    return (
        input_train[:, 1:],
        output_train[:, 1:],
        input_test[:, 1:],
        output_test[:, 1:],
    )


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
# inputs_train, outputs_train, inputs_test, outputs_test = load_simulation(
#     data_dir + "simulation"/
# )
# input_train, output_train, input_test, output_test = load_experiment(
#     data_dir + "experiment/", 1, 2
# )
# P, Q, H = 5, 5, 1
# X_train, Y_train = sequence_data(input_train, output_train, P, Q, H)
