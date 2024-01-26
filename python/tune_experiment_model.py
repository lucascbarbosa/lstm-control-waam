from python.process_data import (
    load_train_data,
    normalize_data,
    standardize_data,
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
    from python.process_data import sequence_data, destandardize_data, denormalize_data
    from python.process_model import create_model, train_model, predict_data

    def compute_metrics(Y_pred, Y_real):
        mses = []
        error = Y_pred - Y_real
        sq_error = error**2
        mses = np.mean(sq_error, axis=0)
        return mses.mean()

    # Sequencing
    sequence_length = run_params["P"] + run_params["Q"]
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
        sequence_length,
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
        if output_scaling == "mean-std":
            Y_pred[:, i] = destandardize_data(
                Y_pred[:, i], train_y_means[i], train_y_stds[i]
            )  # Destandardize

        elif output_scaling == "min-max":
            Y_pred[:, i] = denormalize_data(
                Y_pred[:, i], train_y_mins[i], train_y_maxs[i]
            )  # Denormalize

    model.save(
        results_dir
        + f"models/experiment/hyperparams/run_{run_params['run_id']}.keras"
    )
    
    training_loss = history.history['loss'][-1]
    validation_loss = history.history['val_loss'][-1]
    test_loss = compute_metrics(Y_test, Y_pred)
    print(f"Run: {run_params['run_id']}. Loss: {test_loss:.4f}.")
    
    metrics = run_params
    metrics["train_loss"] = training_loss
    metrics["val_loss"] = validation_loss
    metrics["test_loss"] = test_loss
    return metrics


# Load database
input_train, output_train, input_test, output_test = load_train_data(
    data_dir + "experiment/"
    )

input_train = input_train[:, 1:]
input_test = input_test[:, 1:]
output_train = output_train[:, 1:]
output_test = output_test[:, 1:]

num_features_input = num_features_output = 1

# Scale database
input_scaling = "min-max"
output_scaling = "min-max"
if input_scaling == "mean-std":
    input_train = standardize_data(input_train)
    input_test = standardize_data(input_test)
elif input_scaling == "min-max":
    input_train = normalize_data(input_train)
    input_test = normalize_data(input_test)

if output_scaling == "mean-std":
    train_y_stds = output_train.std(axis=0)
    train_y_means = output_train.mean(axis=0)
    test_y_stds = output_test.std(axis=0)
    test_y_means = output_test.mean(axis=0)
    output_train = standardize_data(output_train)

elif output_scaling == "min-max":
    train_y_mins = output_train.min(axis=0)
    train_y_maxs = output_train.max(axis=0)
    test_y_mins = output_test.min(axis=0)
    test_y_maxs = output_test.max(axis=0)
    output_train = normalize_data(output_train)

# Remove previous models
delete_models(results_dir + "models/experiment/hyperparams/")

# set search space for hp's
hp_search_space = {
    "P": np.arange(5, 51, 5),
    "Q": np.arange(5, 51, 5),
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

num_processes = cpu_count()
# Run all experiments
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
print(metrics_df)

best_model_id = input('Best model id: ')
best_model = load_model(
    results_dir + f"models/experiment/hyperparams/run_{best_model_id}.keras"
)
best_model.save(
    results_dir + f"models/experiment/best/run_{best_model_id}.keras"
)
