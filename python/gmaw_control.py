import casadi as ca
import numpy as np
import pandas as pd
from keras.models import load_model
import os

#############
# Filepaths #
data_dir = "database/"
results_dir = "results/"

# Load your Keras model
best_model_id = 33
keras_model = load_model(
    results_dir + f"models/best/run_{best_model_id:03d}.keras"
)
# Load metrics
metrics_df = pd.read_csv(results_dir + "models/hp_metrics.csv")
best_model_id = metrics_df.iloc[0, 0]
best_model_filename = os.listdir(results_dir + "models/best/")[0]
best_params = metrics_df.iloc[0, 1:]

# Define inputs
seq_len = int(best_params["P"] + best_params["Q"])
input_vars = ca.MX.sym("input", seq_len, 2)
reshaped_input = ca.reshape(input_vars, -1, 1)  # Reshape to (30, 1)

# Convert reshaped_input to NumPy array
reshaped_input_np = np.zeros((seq_len, 2))

casadi_model = ca.Function(
    "model", [input_vars], [keras_model(reshaped_input_np)]
)

# Define MPC parameters
N = 10  # prediction horizon
M = 10  # control horizon
