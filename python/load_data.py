import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load data
data_dir = 'C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/database/'


def load_data():
    X_train = pd.read_csv(data_dir + 'train_inputs.csv')
    Y_train = pd.read_csv(data_dir + 'train_outputs.csv')
    return X_train.to_numpy(), Y_train.to_numpy()


def normalize_data(Y_train):
    # Process database
    scaler = StandardScaler()
    Y_train = scaler.fit_transform(Y_train)

    return Y_train


def sequence_data(X, Y, sequence_length, sequence_stride):
    X = X[:-(X.shape[0] % sequence_length)]
    Y = Y[:-(Y.shape[0] % sequence_length)]
    input_sequences = []
    output_sequences = []
    for i in range(0, len(X) - sequence_length + 1, sequence_stride):
        input_seq = X[i: i + sequence_length]
        output_seq = Y[i: i + sequence_length]
        input_sequences.append(input_seq)
        output_sequences.append(output_seq)
    return np.array(input_sequences), np.array(output_sequences)
