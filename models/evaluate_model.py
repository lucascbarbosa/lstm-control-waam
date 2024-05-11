from models.process_data import (
    load_train_data,
    sequence_data,
    resample_data,
    normalize_data,
    denormalize_data,
)
from models.process_model import predict_data
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load data
data_dir = "database/"
results_dir = "results/"


# Functions
def compute_metrics(Y_pred, Y_real):
    """
    Compute prediction metrics

    Args:
        Y_pred (np.array): predicted output
        Y_real (np.array): measured output

    Returns:
        mses (np.array): mean squared error for each predicted output
    """
    mses = []
    error = Y_pred - Y_real
    sq_error = error**2
    mses = np.mean(sq_error, axis=0)
    return mses


def gradient_angle(Y_pred, Y_real):
    """
    Compute angle between predicted and real gradients
    Args:
        Y_pred (np.array): predicted gradient
        Y_real (np.array): real gradient

    Returns:
        angles (np.array): array of angles between each pair of real and predicted gradient
    """

    angles = np.zeros(Y_real.shape[0])
    for i in range(Y_real.shape[0]):
        vec_real = Y_real[i, :]
        vec_pred = Y_pred[i, :]
        dot_product = np.dot(vec_real, vec_pred)
        norm_vec_real = np.linalg.norm(vec_real)
        norm_vec_pred = np.linalg.norm(vec_pred)
        angle = np.degrees(
            np.arccos(dot_product / (norm_vec_real * norm_vec_pred))
        )
        angles[i] = angle
    return angles


def update_hist(current_hist, new_states):
    """
    Updates history array

    Args:
        current_hist (np.array): current history array
        new_states (np.array): new elements to be added in the file

    Returns
        new_hist (np.array): updated history array
    """
    new_hist = current_hist.copy()
    len_new = new_states.shape[0]
    new_hist[:-len_new, :] = current_hist[len_new:, :]
    new_hist[-len_new:, :] = new_states
    return new_hist


def build_sequence(u_hist, y_hist):
    """
    Build sequence input from history arrays

    Args:
        u (np.array): historical inputs
        y (np.array): historical outputs

    Returns:
        np.array: sequence input
    """
    u = u_hist.ravel()
    y = y_hist.ravel()
    P = u_hist.shape[0]
    Q = y_hist.shape[0]
    return np.hstack((u, y)).reshape((1, 1 * (P + Q), 1))


def pow2wfs(power_data):
    """
    Covert power to wfs

    Args:
        power_data (float): power command

    Returns:
        float: wfs command
    """
    return (power_data * 9 / 100) + 1.5


source = "gradient"
# Load metrics
best_model_id = 16
metrics_df = pd.read_csv(results_dir + f"models/{source}/hp_metrics.csv")
best_params = metrics_df[metrics_df["run_id"] == int(best_model_id)]
if source in ["simulation", "experiment"]:
    best_model_filename = f"run_{best_model_id:03d}.keras"
    P = int(best_params["P"].iloc[0])
    Q = int(best_params["Q"].iloc[0])
    H = int(best_params["H"].iloc[0])
    # Load best model
    model = load_model(
        results_dir + f"models/{source}/best/{best_model_filename}")
    model.compile(
        optimizer=Adam(learning_rate=best_params["lr"]), loss=mean_squared_error
    )

# Load and sequence data accordingly
if source == "simulation":
    _, _, inputs_test, outputs_test = load_simulation(data_dir + f"{source}/")
    y_means = outputs_test.mean(axis=0)
    y_stds = outputs_test.std(axis=0)

    # Scale database
    inputs_test = normalize_data(inputs_test)
    outputs_test = standardize_data(outputs_test)
    num_features_input = inputs_test.shape[1]
    num_features_output = outputs_test.shape[1]

    # Slice to fit sequencing
    inputs_test = inputs_test[:1000, :]
    outputs_test = outputs_test[:1000, :]

    # Sequence data
    X_real, Y_real = sequence_data(
        inputs_test,
        outputs_test,
        P,
        Q,
        H,
    )

    # Prediction
    Y_pred = predict_data(model, X_real)
    for i in range(num_features_output):
        Y_pred[:, i] = destandardize_data(
            Y_pred[:, i], y_means[i], y_stds[i]
        )  # Destandardize

        Y_real[:, i] = destandardize_data(
            Y_real[:, i], y_means[i], y_stds[i]
        )  # Destandardize

    np.savetxt(results_dir + "predictions/simulation/y_real.csv", Y_real)
    np.savetxt(results_dir + "predictions/simulation/y_pred.csv", Y_pred)

    mses = compute_metrics(Y_pred, Y_real)
    print(f"MSE: we={mses[0]:.3f} h={mses[1]:.3f}")

elif source == "experiment":
    input_train, output_train, _, _ = load_train_data(
        data_dir + f"{source}/calibration/")

    # Remove time
    input_train = input_train[:, 1:]
    output_train = output_train[:, 1:]
    train_u_min = input_train.min(axis=0)
    train_u_max = input_train.max(axis=0)
    train_y_min = output_train.min(axis=0)
    train_y_max = output_train.max(axis=0)
    input_train = normalize_data(input_train)
    output_train = normalize_data(output_train)
    beads_test = [3, 6, 10, 15]
    for bead_idx in beads_test:
        bead_filename = data_dir + \
            f"{source}/calibration/series/bead{bead_idx}"
        wfs_test = pd.read_csv(
            bead_filename + "_wfs.csv"
        ).to_numpy()
        ts_test = pd.read_csv(
            bead_filename + "_ts.csv"
        ).to_numpy()
        output_test = pd.read_csv(
            bead_filename + "_w.csv"
        ).to_numpy()

        time_array = output_test[:, 0]

        wfs_test = resample_data(
            wfs_test[:, 1], wfs_test[:, 0], time_array
        )
        ts_test = resample_data(
            ts_test[:, 1], ts_test[:, 0], time_array
        )
        input_test = np.concatenate(
            (wfs_test, ts_test[:, 1].reshape((len(ts_test), 1))),
            axis=1)

        # Remove time
        input_test = input_test[:, 1:]
        output_test = output_test[:, 1:]

        # Number of features
        num_features_input = input_test.shape[1]
        num_features_output = output_test.shape[1]

        # Scale database
        input_test = normalize_data(input_test, train_u_min, train_u_max)
        output_test = normalize_data(output_test, train_y_min, train_y_max)

        # Sequence data
        X_real, Y_real = sequence_data(
            input_test,
            output_test,
            P,
            Q,
            H,
        )

        # Prediction
        Y_pred = predict_data(model, X_real)
        for i in range(num_features_output):
            Y_pred[:, i] = denormalize_data(
                Y_pred[:, i], train_y_min[i], train_y_max[i]
            )  # Denormalize

            Y_real[:, i] = denormalize_data(
                Y_real[:, i], train_y_min[i], train_y_max[i]
            )  # Denormalize

        # Save real and predicted data
        time_array = time_array.reshape((time_array.shape[0], 1))
        np.savetxt(
            results_dir + f"predictions/experiment/bead{bead_idx}_y_real.csv",
            np.concatenate((time_array, Y_real), axis=1),
        )
        np.savetxt(
            results_dir + f"predictions/experiment/bead{bead_idx}_y_pred.csv",
            np.concatenate((time_array, Y_pred), axis=1),
        )

        mse = compute_metrics(Y_pred, Y_real)
        print(f"MSE for bead {bead_idx}: we={mse[0]}")

elif source == "gradient":

    # Load  model
    weights = np.loadtxt(
        results_dir + f"models/gradient/best/run_{best_model_id:03d}.txt")

    A = weights[:-1, :]
    b = weights[-1, :]

    # Load database
    X_train, Y_train, X_test, Y_test = load_train_data(
        data_dir + "gradient/"
    )

    # Scaling
    train_x_max = X_train.max(axis=0)
    train_x_min = X_train.min(axis=0)
    train_y_max = Y_train.max(axis=0)
    train_y_min = Y_train.min(axis=0)
    X_test = normalize_data(X_test, train_x_min, train_x_max)

    # Predict data
    Y_pred = X_test @ A + b
    Y_pred = denormalize_data(
        Y_pred, train_y_min, train_y_max
    )  # Denormalize

    Y_real = Y_test
    np.savetxt(
        results_dir + f"predictions/gradient/y_real.csv",
        Y_real)
    np.savetxt(
        results_dir + f"predictions/gradient/y_pred.csv",
        Y_pred)

    angles = gradient_angle(Y_pred, Y_real)
    print(f"Angular error: {angles.mean():.2f}")

    # num_outputs = Y_real.shape[1]
    # # Angles error
    # angles = gradient_angle(Y_real, Y_pred)
    # print(f"Angular error: {angles.mean():.2f}")
    # fig = plt.figure(figsize=(20, 9))
    # avg = np.mean(angles)
    # plt.title("Angular error between real and predicted gradients")
    # sns.histplot(angles, bins=128)
    # plt.axvline(90, linestyle="--", color="black", label="90 deg")
    # plt.axvline(avg, linestyle="--", color="red", label=f"Mean: {avg:.2f}")
    # plt.legend()
    # plt.tight_layout()
    # plt.show()
