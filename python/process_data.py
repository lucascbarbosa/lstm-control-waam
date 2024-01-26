import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def load_train_data(data_dir):
    input_train = pd.read_csv(data_dir + "inputs_train.csv").to_numpy()
    output_train = pd.read_csv(data_dir + "outputs_train.csv").to_numpy()
    input_test = pd.read_csv(data_dir + "inputs_test.csv").to_numpy()
    output_test = pd.read_csv(data_dir + "outputs_test.csv").to_numpy()
    return input_train, output_train, input_test, output_test

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
