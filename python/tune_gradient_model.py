from python.process_data import (
    load_gradient, 
    standardize_data, 
    destandardize_data, 
    normalize_data, 
    denormalize_data)
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
    X_train,
    Y_train,
    X_test,
    Y_test,
    run_params,
):
    from python.gradient_model import create_model, train_model, predict_data

    def compute_metrics(Y_pred, Y_real):
        mses = []
        error = Y_pred - Y_real
        sq_error = error**2
        mses = np.mean(sq_error, axis=0)
        return mses.mean()

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
    if output_scaling == "mean-std":
        Y_pred = destandardize_data(
            Y_pred, train_y_mean, train_y_std
        )  # Destandardize

        Y_test = destandardize_data(
            Y_test, test_y_mean, test_y_std
        )  # Destandardize
    elif output_scaling == "min-max":
        Y_pred = denormalize_data(
            Y_pred, train_y_min, train_y_max
        )  # Denormalize

        Y_test = denormalize_data(
            Y_test, test_y_min, test_y_max
        )  # Denormalize

    model.save(
        results_dir
        + f"models/gradient_model/hyperparams/run_{run_params['run_id']}.keras"
    )
    
    train_loss = history.history['loss'][-1]
    val_loss = history.history['val_loss'][-1]
    test_loss = compute_metrics(Y_test, Y_pred)
    print(f"Run: {run_params['run_id']}. " +
          f"Epochs: {run_params['num_epochs']} " +
          f"train_loss: {train_loss:.6f} " +
          f"val_loss {val_loss:.6f} " +
          f"test_loss: {test_loss:.6f}")
    
    metrics = run_params
    metrics["train_loss"] = train_loss
    metrics["val_loss"] = val_loss
    metrics["test_loss"] = test_loss
    return metrics

# Load database
X_train, Y_train, X_test, Y_test = load_gradient(
    data_dir + "gradient/"
)

X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1)) 
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1)) 

# Scaling
output_scaling = "mean-std"
if output_scaling == "mean-std":
    train_y_mean = np.mean(Y_train, axis=0)
    train_y_std = np.std(Y_train, axis=0)
    test_y_mean = np.mean(Y_test, axis=0)
    test_y_std = np.std(Y_test, axis=0)
    Y_train = standardize_data(Y_train)
elif output_scaling == "min-max":
    train_y_min = np.min(Y_train, axis=0)
    train_y_max = np.max(Y_train, axis=0)
    test_y_min = np.min(Y_test, axis=0)
    test_y_max = np.max(Y_test, axis=0)
    Y_train = normalize_data(Y_train)

# Get process model parameters
metrics_process = pd.read_csv(results_dir + f"models/experiment_igor/hp_metrics.csv")
best_model_id = 121
best_model_filename = f"run_{best_model_id:03d}.keras"
best_params = metrics_process[metrics_process["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

# Num features
num_features_input = P + Q
num_features_output = 1

# Remove previous models
delete_models(results_dir + "models/gradient_model/hyperparams/")

# set search space for hp's
hp_search_space = {
    "batch_size": [16, 32, 64],
    "num_epochs": [200, 300, 400, 500],
    "validation_split": [0.1, 0.2, 0.3],
    "lr": [1e-4, 1e-3, 1e-2],
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

metrics_df.to_csv(results_dir + "models/gradient_model/hp_metrics.csv")
print(metrics_df)

best_model_id = input('Best model id: ')
best_model = load_model(
    results_dir + f"models/gradient_model/hyperparams/run_{best_model_id}.keras"
)
best_model.save(
    results_dir + f"models/gradient_model/best/run_{best_model_id}.keras"
)
