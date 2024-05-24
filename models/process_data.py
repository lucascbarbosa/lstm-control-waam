import pandas as pd
import numpy as np
from scipy.interpolate import interp1d


def build_train_data(data_dir, beads_train, beads_test):
    """
    Build train dataset from experimental dataset (beads welding)

    Args:
        data_dir (str): data directory path
        beads_train (list): beads used for train dataset
        beads_test (list): beads used for test dataset

    Returns:

    """
    inputs_train = []
    outputs_train = []
    inputs_test = []
    outputs_test = []
    for bead_idx in beads_train:
        filename_train = f"series/bead{bead_idx}"
        wfs_train = pd.read_csv(
            data_dir + filename_train + "_wfs_command.csv"
        ).to_numpy()
        ts_train = pd.read_csv(
            data_dir + filename_train + "_ts_command.csv"
        ).to_numpy()
        output_train = pd.read_csv(
            data_dir + filename_train + "_w.csv"
        ).to_numpy()

        input_train = np.concatenate(
            (wfs_train, ts_train[:, 1].reshape((len(ts_train), 1))),
            axis=1)
        inputs_train.append(input_train)
        outputs_train.append(output_train)

    inputs_train = np.concatenate(inputs_train, axis=0)
    inputs_train = pd.DataFrame(inputs_train, columns=["t", "wfs", "ts"])
    inputs_train.to_csv(data_dir + "input_train.csv", index=False)
    outputs_train = np.concatenate(outputs_train, axis=0)
    outputs_train = pd.DataFrame(outputs_train, columns=["t", "w"])
    outputs_train.to_csv(data_dir + "output_train.csv", index=False)

    for bead_idx in beads_test:
        filename_test = f"series/bead{bead_idx}"
        wfs_test = pd.read_csv(
            data_dir + filename_test + "_wfs.csv"
        ).to_numpy()
        ts_test = pd.read_csv(
            data_dir + filename_test + "_ts.csv"
        ).to_numpy()
        output_test = pd.read_csv(
            data_dir + filename_test + "_w.csv"
        ).to_numpy()

        wfs_test = resample_data(
            wfs_test[:, 1], wfs_test[:, 0], output_test[:, 0]
        )
        ts_test = resample_data(
            ts_test[:, 1], ts_test[:, 0], output_test[:, 0]
        )
        input_test = np.concatenate(
            (wfs_test, ts_test[:, 1].reshape((len(ts_test), 1))),
            axis=1)
        inputs_test.append(input_test)
        outputs_test.append(output_test)

    inputs_test = np.concatenate(inputs_test, axis=0)
    inputs_test = pd.DataFrame(inputs_test, columns=["t", "wfs", "ts"])
    inputs_test.to_csv(data_dir + "input_test.csv", index=False)
    outputs_test = np.concatenate(outputs_test, axis=0)
    outputs_test = pd.DataFrame(outputs_test, columns=["t", "w"])
    outputs_test.to_csv(data_dir + "output_test.csv", index=False)


def load_train_data(data_dir):
    """
    Load train dataset

    Args:
        data_dir (str): data directory path

    Returns:
        input_train (np.array): inputs of train data
        output_train (np.array): outputs of train data
        input_test (np.array): inputs of test data
        output_test (np.array): outputs of test data
    """
    input_train = pd.read_csv(
        data_dir + "input_train.csv").to_numpy().astype(np.float32)
    output_train = pd.read_csv(
        data_dir + "output_train.csv").to_numpy().astype(np.float32)
    input_test = pd.read_csv(
        data_dir + "input_test.csv").to_numpy().astype(np.float32)
    output_test = pd.read_csv(
        data_dir + "output_test.csv").to_numpy().astype(np.float32)
    return input_train, output_train, input_test, output_test


def normalize_data(x, min_val=None, max_val=None):
    """
    Normalize dataset

    Args:
        x (np.array): denormalized dataset
        min_val (float): minimum value used in normalization
        max_val (float): maximum value used in normalization

    Returns:
        np.array: normalized dataset
    """
    if min_val is None and max_val is None:
        return (x-x.min(axis=0))/(x.max(axis=0)-x.min(axis=0))
    else:
        return (x-min_val)/(max_val-min_val)


def denormalize_data(x, min_val, max_val):
    """
    Denormalize dataset

    Args:
        x (np.array): normalized dataset
        min_val (float): minimum value of dataset
        max_val (float): maximum value of dataset

    Returns:
        np.array: denormalized dataset
    """
    return x * (max_val - min_val) + min_val


def resample_data(original_data, original_time, new_time):
    """
    Resample dataset given the original and resampled time points

    Args:
        original_data (np.array): original dataset
        original_time (np.array): original dataset time points
        new_time (np.array): resampled time points

    Returns:
        resampled_data (np.array): resampled dataset
    """
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


def sequence_data(X, Y, P, Q, H):
    """
    Sequence dataset

    Args:
        X (np.array): input dataset
        Y (np.array): output dataset
        P (int): Inputs sequence length
        Q (int): Outputs sequence length
        H (int): Forecast horizon

    Returns:
        X_seq (np.array): sequenced input dataset
        Y_seq (np.array): sequenced output dataset
    """

    num_features_input = X.shape[1]
    num_features_output = Y.shape[1]

    # Zero padding
    X = np.vstack(
        (np.zeros((max(P - 1, Q), num_features_input)), X))
    Y = np.concatenate(
        (np.zeros((max(P - 1, Q), num_features_output)), Y))
    X_seq = np.zeros((len(X) - max(P - 1, Q) - H + 1,
                     P * num_features_input + Q * num_features_output, 1))
    Y_seq = np.zeros((len(X) - max(P - 1, Q) - H + 1, num_features_output))

    for i in range(0, len(X) - max(P - 1, Q) - H + 1):
        X_seq[i, :, 0] = np.hstack(
            (
                X[i + max(0, Q - P + 1): i + max(Q + 1, P), :].ravel(),
                Y[i + max(0, P - Q - 1): i + max(P - 1, Q), :].ravel(),
            )
        )
        Y_seq[i, :] = Y[i + max(P - 1, Q) + H - 1, :]
    return X_seq, Y_seq
