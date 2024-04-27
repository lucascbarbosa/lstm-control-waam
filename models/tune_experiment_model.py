from models.process_data import build_train_data, load_train_data, normalize_data
import tensorflow as tf
from tensorflow.keras.models import load_model
import itertools
import pandas as pd
import numpy as np
import os
from multiprocess import Pool, cpu_count
import logging

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

#############
# Filepaths #
data_dir = "database/"
results_dir = "results/"

############
# Function #


def split_train_test(beads, k):
    idxs = np.random.choice(len(beads), k, replace=False)
    beads_test = beads[idxs]
    beads_train = np.delete(beads, idxs)
    return beads_train, beads_test


def delete_models(models_path):
    """
    Delete all saved models

    Args:
        models_path (str): Path of saved models directory

    """
    for item in os.listdir(models_path):
        item_path = os.path.join(models_path, item)
        os.remove(item_path)


def run_training(
    input_train,
    output_train,
    input_test,
    output_test,
    run_params,
):
    """
    Train a model with a specific set of parameters

    Args:
        input_train (np.array): train input data
        output_train (np.array): train output data
        input_test (np.array): test input data
        output_test (np.array): test output data
        run_params (dict): training parameters

    Returns:
        model (tf.Sequential): trained model
        history (dict): history of training

    """
    from models.process_data import (
        sequence_data,
        denormalize_data,
    )
    from models.process_model import create_model, train_model, predict_data

    def compute_metrics(Y_pred, Y_real):
        mses = []
        error = Y_pred - Y_real
        sq_error = error**2
        mses = np.mean(sq_error, axis=0)
        return mses.mean()

    # Sequencing
    X_train, Y_train = sequence_data(
        input_train,
        output_train,
        run_params["P"],
        run_params["Q"],
        run_params["H"],
    )
    X_test, Y_test = sequence_data(
        input_test,
        output_test,
        run_params["P"],
        run_params["Q"],
        run_params["H"],
    )

    # Define model
    model = create_model(
        run_params["P"],
        run_params["Q"],
        num_features_input,
        num_features_output,
        run_params["lr"],
        random_seed=42,
        summary=False,
    )

    # Training
    model, history = train_model(
        model,
        X_train,
        Y_train,
        run_params["batch_size"],
        run_params["num_epochs"],
        run_params["validation_split"],
        verbose=verbose_level,
    )

    # Prediction
    Y_pred = predict_data(model, X_test)
    for i in range(num_features_output):
        Y_pred[:, i] = denormalize_data(
            Y_pred[:, i], train_y_min[i], train_y_max[i]
        )  # Denormalize
        Y_test[:, i] = denormalize_data(
            Y_test[:, i], train_y_min[i], train_y_max[i]
        )  # Denormalize

    model.save(
        results_dir
        + f"models/experiment/hyperparams/run_{run_params['run_id']}.keras"
    )

    training_loss = history.history["loss"][-1]
    validation_loss = history.history["val_loss"][-1]
    test_loss = compute_metrics(Y_test, Y_pred)
    print(f"Run: {run_params['run_id']}. Loss: {test_loss:.4f}.")

    metrics = run_params
    metrics["train_loss"] = training_loss
    metrics["val_loss"] = validation_loss
    metrics["test_loss"] = test_loss
    return metrics


# Load database
# beads = np.arange(1, 16)
# beads_train, beads_test = split_train_test(beads, 4)
beads_test = [3, 6, 10, 15]
beads_train = [1, 2, 4, 5, 7, 8, 9, 11, 12, 13, 14]

build_train_data(data_dir + "experiment/calibration/", beads_train, beads_test)
input_train, output_train, input_test, output_test = load_train_data(
    data_dir + "experiment/calibration/"
)

input_train = input_train[:, 1:]
input_test = input_test[:, 1:]
output_train = output_train[:, 1:]
output_test = output_test[:, 1:]

num_features_input = input_train.shape[1]
num_features_output = output_train.shape[1]

# Scale database
train_u_min = input_train.min(axis=0)
train_u_max = input_train.max(axis=0)
train_y_min = output_train.min(axis=0)
train_y_max = output_train.max(axis=0)
input_train = normalize_data(input_train)
input_test = normalize_data(input_test, train_u_min, train_u_max)
output_train = normalize_data(output_train)
output_test = normalize_data(output_test, train_y_min, train_y_max)

# Remove previous models
delete_models(results_dir + "models/experiment/hyperparams/")

# set search space for hp's
hp_search_space = {
    "P": np.arange(5, 51, 5),
    "Q": np.arange(0, 51, 5),  # np.arange(0, 51, 5)
    "H": [1],
    "batch_size": [16, 32, 64],
    "num_epochs": [10],
    "validation_split": [0.1],
    "lr": [1e-3],
}

hp_combinations = list(itertools.product(*hp_search_space.values()))

# iterate every combination
list_run_params = []
verbose_level = 0
i = 1
for hp_comb in hp_combinations:
    run_params = {
        param_name: param_value
        for param_name, param_value in zip(hp_search_space.keys(), hp_comb)
    }
    run_params["run_id"] = "%03d" % i
    list_run_params.append(run_params)
    i += 1

# Run all experiments
num_processes = cpu_count()
with Pool(processes=num_processes) as pool:
    results = pool.starmap(
        run_training,
        [
            (
                input_train,
                output_train,
                input_test,
                output_test,
                run_params,
            )
            for run_params in list_run_params
        ],
    )

metrics_df = (
    pd.DataFrame.from_dict(results)
    .set_index("run_id")
    .sort_values(by="test_loss")
)
metrics_df.to_csv(results_dir + "models/experiment/hp_metrics.csv")
print(metrics_df.head(10))

best_model_id = input("Best model id: ")
best_model = load_model(
    results_dir + f"models/experiment/hyperparams/run_{best_model_id}.keras"
)
best_model.save(
    results_dir + f"models/experiment/best/run_{best_model_id}.keras"
)
