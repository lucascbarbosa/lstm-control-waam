import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def load_data(data_dir):
    X_train = pd.read_csv(data_dir + 'train_inputs.csv').to_numpy()
    Y_train = pd.read_csv(data_dir + 'train_outputs.csv').to_numpy()
    X_test = pd.read_csv(data_dir + 'test_inputs.csv').to_numpy()
    Y_test = pd.read_csv(data_dir + 'test_outputs.csv').to_numpy()
    return X_train, Y_train, X_test, Y_test


def normalize_data(Y_train, Y_test):
    # Process database
    scaler = StandardScaler()
    Y_train = scaler.fit_transform(Y_train)
    Y_test = scaler.fit_transform(Y_test)
    return Y_train, Y_test


def sequence_data(X, Y, inputs_seq_len, outputs_seq_len, forecast_h):
    sequence_length = inputs_seq_len + outputs_seq_len
    input_sequences = []
    output_sequences = []
    for i in range(0, len(X) - sequence_length):
        input_seq = np.vstack((X[i: i + inputs_seq_len, :],
                              Y[i: i + outputs_seq_len, :]))
        output_seq = Y[i + outputs_seq_len + forecast_h - 1]
        input_sequences.append(input_seq)
        output_sequences.append(output_seq)
    return np.array(input_sequences), np.array(output_sequences)
