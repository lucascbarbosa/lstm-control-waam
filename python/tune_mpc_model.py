from python.process_data import (
    load_mpc,
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
    from python.process_data import sequence_data, denormalize_data
    from python.lstm import create_model, train_model, predict_data

    def compute_metrics(Y_pred, Y_real):
        mses = []
        error = Y_pred - Y_real
        sq_error = error**2
        mses = np.mean(sq_error, axis=0)
        return mses

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
        verbose=verbose_level,
    )

    # Prediction
    Y_pred = predict_data(model, X_test)
    for i in range(num_features_output):
        Y_pred[:, i] = denormalize_data(
            Y_pred[:, i], train_y_mins[i], train_y_maxs[i]
        )  # Denormalize

        Y_test[:, i] = denormalize_data(
            Y_test[:, i], test_y_mins[i], test_y_maxs[i]
        )  # Denormalize

    model.save(
        results_dir
        + f"models/mpc/hyperparams/run_{run_params['run_id']}.keras"
    )
    loss = compute_metrics(Y_test, Y_pred).mean()

    print(f"Run: {run_params['run_id']}. Loss: {loss:.4f}")
    metrics = run_params
    metrics["loss"] = loss
    return metrics


# Load database
input_train, output_train, input_test, output_test = load_mpc(data_dir + "mpc/")

num_features_input = num_features_output = 1

# Output normalization parameters (mins and maxs)
train_y_mins = output_train.min(axis=0)
train_y_maxs = output_train.max(axis=0)

test_y_mins = output_test.min(axis=0)
test_y_maxs = output_test.max(axis=0)

# Scale database
input_train = standardize_data(input_train)
input_test = standardize_data(input_test)
output_train = normalize_data(output_train)
output_test = normalize_data(output_test)

# Remove previous models
delete_models(results_dir + "models/mpc/hyperparams/")

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
verbose_level = 0
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
metrics_df.to_csv(results_dir + "models/mpc/hp_metrics.csv")

best_model_id = metrics_df.index[0]
best_model = load_model(
    results_dir + f"models/mpc/hyperparams/run_{best_model_id}.keras"
)
best_model.save(
    results_dir + f"models/mpc/best/run_{best_model_id}.keras"
)
