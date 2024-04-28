from models.process_data import (
    load_train_data,
    normalize_data,
    denormalize_data,
)
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
    X_train,
    Y_train,
    X_test,
    Y_test,
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
    from models.gradient_model import create_model, train_model, predict_data

    def gradient_angle(Y_real, Y_pred):
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
        return angles.mean()

    # Define model
    model = create_model(
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
    Y_pred = denormalize_data(
        Y_pred, train_y_min, train_y_max
    )  # Denormalize

    model.save(
        results_dir
        + f"models/gradient/hyperparams/run_{run_params['run_id']}.keras"
    )

    # Losses
    train_loss = history.history["loss"][-1]
    val_loss = history.history["val_loss"][-1]
    test_loss = gradient_angle(Y_test, Y_pred)
    print(
        f"Run: {run_params['run_id']}. "
        +
        #   f"Epochs: {run_params['num_epochs']} " +
        #   f"Batch size: {run_params['batch_size']} " +
        f"train_loss: {train_loss:.6f} "
        + f"val_loss {val_loss:.6f} "
        + f"test_loss: {test_loss:.2f}"
    )

    # Metrics
    metrics = run_params
    metrics["train_loss"] = train_loss
    metrics["val_loss"] = val_loss
    metrics["test_loss"] = test_loss
    return metrics


# Get process model parameters
metrics_process = pd.read_csv(
    results_dir + f"models/experiment/hp_metrics.csv"
)
best_model_id = 169
best_model_filename = f"run_{best_model_id:03d}.keras"
best_params = metrics_process[metrics_process["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

# Load database
source = "experiment"
X_train, Y_train, X_test, Y_test = load_train_data(
    data_dir + f"gradient/{source}/"
)

# Scaling
train_x_min = np.min(X_train, axis=0)
train_x_max = np.max(X_train, axis=0)
train_y_min = np.min(Y_train, axis=0)
train_y_max = np.max(Y_train, axis=0)
X_train = normalize_data(X_train)
X_test = normalize_data(X_test, train_x_min, train_x_max)
Y_train = normalize_data(Y_train)

# Reshape to fit model input
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

# Num features
num_features_input = X_train.shape[1]
num_features_output = Y_train.shape[1]

# Remove previous models
delete_models(results_dir + "models/gradient/hyperparams/")

# set search space for hp's
hp_search_space = {
    "batch_size": [16, 32, 64],
    # "batch_size": [16],
    "num_epochs": [100],
    "validation_split": [0.1, 0.2, 0.3],
    # "validation_split": [0.1],
    "lr": [1e-3, 1e-2],
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

num_processes = cpu_count()
# Run all experiments
with Pool(processes=num_processes) as pool:
    results = pool.starmap(
        run_training,
        [
            (
                X_train,
                Y_train,
                X_test,
                Y_test,
                run_params,
            )
            for run_params in list_run_params
        ],
    )

metrics_df = (
    pd.DataFrame.from_dict(results)
    .set_index("run_id")
    .sort_values(by="train_loss")
)

metrics_df.to_csv(results_dir + "models/gradient/hp_metrics.csv")
print(metrics_df)

best_model_id = input("Best model id: ")
best_model = load_model(
    results_dir + f"models/gradient/hyperparams/run_{best_model_id}.keras"
)
best_model.save(
    results_dir + f"models/gradient/best/run_{best_model_id}.keras"
)
