import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def load_data(data_dir):
    inputs_train = pd.read_csv(data_dir + "inputs_train.csv").to_numpy()
    outputs_train = pd.read_csv(data_dir + "outputs_train.csv").to_numpy()
    inputs_test = pd.read_csv(data_dir + "inputs_test.csv").to_numpy()
    outputs_test = pd.read_csv(data_dir + "outputs_test.csv").to_numpy()
    return inputs_train, outputs_train, inputs_test, outputs_test


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
    X_seq = np.zeros((len(X) - max(P - 1, Q) - H + 1, (P + Q) * 2, 1))
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
