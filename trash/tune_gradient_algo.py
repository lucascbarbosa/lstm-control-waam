from python.process_data import (
    load_gradient, 
    standardize_data, 
    destandardize_data, 
    normalize_data, 
    denormalize_data)
from sklearn.metrics import mean_squared_error
import joblib
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
    X_train,
    Y_train,
    X_test,
    Y_test,
    run_params,
):
    from python.gradient_algo import create_model, train_model, predict_data
    import joblib

    def compute_metrics(Y_pred, Y_real):
        return mean_squared_error(Y_real, Y_pred)

    # Define model
    model = create_model(
        run_params['n_neighbors'],
        run_params['weights'],
        run_params['algorithm'],
        run_params['leaf_size'],
        run_params['p']
    )

    # Training
    model = train_model(
        model,
        X_train,
        Y_train,
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

    joblib.dump(
        model,
        results_dir
        + f"models/gradient_algo/hyperparams/run_{run_params['run_id']}.pkl"
    )
    
    test_loss = compute_metrics(Y_test, Y_pred)
    print(f"Run: {run_params['run_id']}. Loss: {test_loss:.6f}.")
    
    metrics = run_params
    metrics["test_loss"] = test_loss
    return metrics


# Load database
X_train, Y_train, X_test, Y_test = load_gradient(
    data_dir + "gradient/"
)

N = 5000
X_train = X_train[: N]
X_test = X_test[: N]
Y_train = Y_train[: N]
Y_test = Y_test[: N]

# Scaling
input_scaling = "min-max"
output_scaling = "min-max"

if input_scaling == "mean-std":
    train_x_mean = np.mean(X_train, axis=0)
    train_x_std = np.std(X_train, axis=0)
    test_x_mean = np.mean(X_test, axis=0)
    test_x_std = np.std(X_test, axis=0)
    X_train = standardize_data(X_train)
    X_test = standardize_data(X_test)

elif input_scaling == "min-max":
    train_x_min = np.min(X_train, axis=0)
    train_x_max = np.max(X_train, axis=0)
    test_x_min = np.min(X_test, axis=0)
    test_x_max = np.max(X_test, axis=0)
    X_train = normalize_data(X_train)
    X_test = normalize_data(X_test)

if output_scaling == "mean-std":
    train_y_mean = np.mean(Y_train, axis=0)
    train_y_std = np.std(Y_train, axis=0)
    test_y_mean = np.mean(Y_test, axis=0)
    test_y_std = np.std(Y_test, axis=0)
    Y_train = standardize_data(Y_train)
    Y_test = standardize_data(Y_test)

elif output_scaling == "min-max":
    train_y_min = np.min(Y_train, axis=0)
    train_y_max = np.max(Y_train, axis=0)
    test_y_min = np.min(Y_test, axis=0)
    test_y_max = np.max(Y_test, axis=0)
    Y_train = normalize_data(Y_train)
    Y_test = normalize_data(Y_test)

# Get process model parameters
metrics_process = pd.read_csv(
    results_dir + \
    f"models/experiment_igor/hp_metrics.csv"
    )
best_model_id = 121
best_model_filename = f"run_{best_model_id:03d}.keras"
best_params = metrics_process[metrics_process["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

# Num features
num_features_input = P + Q + 1
num_features_output = P

# Remove previous models
delete_models(results_dir + "models/gradient_algo/hyperparams/")

# set search space for hp's
hp_search_space = {
    "n_neighbors": [2, 5, 7, 10],
    "weights": ['uniform', 'distance'],
    "algorithm": ['auto', 'ball_tree', 'kd_tree', 'brute'],
    "leaf_size": [10, 20, 30],
    'p': [1.0, 2.0, 1.5, 2.5]
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
    .sort_values(by="test_loss")
)

metrics_df.to_csv(results_dir + "models/gradient_algo/hp_metrics.csv")
print(metrics_df)

best_model_id = input('Best model id: ')
best_model = joblib.load(
    results_dir + f"models/gradient_algo/hyperparams/run_{best_model_id}.pkl"
)
joblib.dump(
    best_model,
    results_dir + f"models/gradient_algo/best/run_{best_model_id}.pkl"
)
