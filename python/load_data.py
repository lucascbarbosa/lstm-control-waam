import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def load_data(data_dir):
    X_train = pd.read_csv(data_dir + 'train_inputs.csv').to_numpy()
    Y_train = pd.read_csv(data_dir + 'train_outputs.csv').to_numpy()
    X_test = pd.read_csv(data_dir + 'test_inputs.csv').to_numpy()
    Y_test = pd.read_csv(data_dir + 'test_outputs.csv').to_numpy()
    return X_train, Y_train, X_test, Y_test


def normalize_data(x):
    # Process database
    scaler = StandardScaler()
    x = scaler.fit_transform(x)
    return x


def denormalize_data(x, mean, std):
    return (x * std) + mean


def sequence_data(X, Y, inputs_seq_len, outputs_seq_len, forecast_h):
    sequence_length = inputs_seq_len + outputs_seq_len
    X_seq = np.zeros((len(X) - sequence_length, sequence_length, X.shape[1]))
    Y_seq = np.zeros((len(X) - sequence_length - forecast_h + 1, X.shape[1]))
    for i in range(0, len(X) - sequence_length):
        input_seq = np.vstack((X[i: i + inputs_seq_len, :],
                              Y[i: i + outputs_seq_len, :]))
        output_seq = Y[i + outputs_seq_len + forecast_h - 1, :]
        X_seq[i, :, :] = input_seq
        Y_seq[i, :] = output_seq
    return X_seq, Y_seq
