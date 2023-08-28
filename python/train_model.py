from python.process_data import (
    load_data,
    normalize_data,
    standardize_data,
)
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import Adam
import itertools
import shutil
import datetime
import pandas as pd
import numpy as np
import os
from multiprocess import Pool, cpu_count

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
#############
# Filepaths #
data_dir = "database/"
results_dir = "results/"


############
# Function #
def delete_models(models_path):
    for item in os.listdir(models_path):
        item_path = os.path.join(models_path, item)
        shutil.rmtree(item_path)


def run_training(
    inputs_train, outputs_train, inputs_test, outputs_test, run_params
):
    from python.process_data import sequence_data, destandardize_data
    from python.lstm import create_model, train_model, predict_data, plot_loss
    from python.evaluate_model import compute_metrics

    # Sequencing
    sequence_length = run_params["P"] + run_params["Q"]
    X_train, Y_train = sequence_data(
        inputs_train,
        outputs_train,
        run_params["P"],
        run_params["Q"],
        run_params["H"],
    )
    X_test, Y_test = sequence_data(
        inputs_test,
        outputs_test,
        run_params["P"],
        run_params["Q"],
        run_params["H"],
    )
    y_means = Y_test.mean(axis=0)
    y_stds = Y_test.std(axis=0)

    # Define model
    model = create_model(
        sequence_length,
        run_params["num_features_input"],
        run_params["num_features_output"],
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
    )

    # Prediction
    Y_pred = predict_data(model, X_test)
    for i in range(num_features_output):
        Y_pred[:, i] = destandardize_data(
            Y_pred[:, i], y_means[i], y_stds[i]
        )  # Destandardize

        Y_test[:, i] = destandardize_data(
            Y_test[:, i], y_means[i], y_stds[i]
        )  # Destandardize

    model.save(
        results_dir + f"models/hyperparams/run_{run_params['run_id']}.keras"
    )
    loss = compute_metrics(Y_test, Y_pred).mean()

    metrics = run_params
    metrics["loss"] = loss

    return metrics


# Load database
inputs_train, outputs_train, inputs_test, outputs_test = load_data(data_dir)
num_features_input = inputs_train.shape[1]
num_features_output = outputs_train.shape[1]

# Slice database to fit sequencing
inputs_train = inputs_train[:1000, :]
outputs_train = outputs_train[:1000, :]
inputs_test = inputs_test[:1000, :]
outputs_test = outputs_test[:1000, :]

# Scale database
inputs_train = normalize_data(inputs_train)
inputs_test = normalize_data(inputs_test)
outputs_train = standardize_data(outputs_train)
outputs_test = standardize_data(outputs_test)

# Remove previous models
delete_models(results_dir + "models/hyperparams")

# set search space for hp's
hp_search_space = {
    "P": np.arange(5, 51, 5),
    "Q": np.arange(5, 51, 5),
    "H": [1],
    "batch_size": [16, 32, 64],
    "num_epochs": [100],
    "validation_split": [0.1],
    "lr": [1e-4],
}

hp_combinations = list(itertools.product(*hp_search_space.values()))

# iterate every combination
list_run_params = []
i = 1
for hp_comb in hp_combinations:
    run_params = {
        param_name: param_value
        for param_name, param_value in zip(hp_search_space.keys(), hp_comb)
    }
    run_params["num_features_input"] = num_features_input
    run_params["num_features_output"] = num_features_output
    run_params["run_id"] = "%03d" % i
    list_run_params.append(run_params)
    i += 1

num_processes = 8
with Pool(processes=num_processes) as pool:
    results = pool.starmap(
        run_training,
        [
            (
                inputs_train,
                outputs_train,
                inputs_test,
                outputs_test,
                run_params,
            )
            for run_params in list_run_params
        ],
    )

metrics_df = (
    pd.DataFrame.from_dict(results)
    .drop(
        [
            "num_features_output",
            "num_features_input",
        ],
        axis=1,
    )
    .set_index("run_id")
    .sort_values(by="loss")
)
metrics_df.to_csv(results_dir + "models/hp_metrics.csv")

best_model_id = metrics_df.index[0]
best_model = load_model(
    results_dir + f"models/hyperparams/run_{best_model_id}.keras"
)
best_model.save(results_dir + f"models/best/run_{best_model_id}.keras")
