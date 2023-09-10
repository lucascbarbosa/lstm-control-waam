from python.gmaw_process import *

import numpy as np
import pandas as pd
from scipy.optimize import minimize
import os
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam


#############
# Filepaths #
data_dir = "database/"
results_dir = "results/"

# Load metrics
metrics_df = pd.read_csv(results_dir + "models/hp_metrics.csv")
best_model_id = metrics_df.iloc[0, 0]
best_model_filename = os.listdir(results_dir + "models/best/")[0]
best_params = metrics_df.iloc[0, 1:]
P = int(best_params["P"])
Q = int(best_params["Q"])

# Load Keras model
best_model_id = 13
keras_model = load_model(
    results_dir + f"models/best/run_{best_model_id:03d}.keras"
)
opt = Adam(learning_rate=best_params["lr"])
keras_model.compile(optimizer=opt, loss=mean_squared_error)

# Define MPC parameters
N = 10  # prediction horizon
M = 10  # control horizon
control_forecast = np.zeros((M, 2))
output_forecast = np.zeros((N, 2))

# Simulation parameters
step = 1e-6
sim_time = 1e-3
total_sim_steps = int(sim_time / step)

# Initial conditions
x0 = [1e-10, 1e-10]
y0 = gmaw_outputs(x0)
x0 = np.array(x0).reshape((1, 2))
y0 = np.array(y0).reshape((1, 2))
u0 = np.zeros((1, 2))

x = x0
y_row = y0
u_row = u0

# Boundaries and constraints
min_f, max_f = 0.0, 1.0
min_Ir, max_Ir = 0.0, 1.0
min_we, max_we = 0.0, 1.0
min_h, max_h = 0.0, 1.0
control_bounds = [(min_f, max_f), (min_Ir, max_Ir)]  # Control input bounds
output_bounds = [(min_we, max_we), (min_h, max_h)]  # Output bounds
bounds = control_bounds * M + output_bounds * N

# Historic data
u_hist = np.zeros((P - 1, 2))
y_hist = np.zeros((Q - 1, 2))


#############
# Functions #
def build_sequence(u_hist, u_last, y_hist, y_last):
    u = np.vstack((u_hist, u_last)).ravel()
    y = np.vstack((y_hist, y_last)).ravel()
    return np.hstack((u, y)).reshape((1, 2 * (P + Q), 1))


def lstm_predict(u_last, y_last):
    seq_input = build_sequence(u_hist, u_last, y_hist, y_last)
    y_hat = keras_model.predict(seq_input)
    return y_hat


def update_hist(current_hist):
    new_hist = current_hist.copy()
    new_hist[:-1, :] = current_hist[1:, :]
    new_hist[-1, :] = np.nan
    return new_hist


def cost_function(u):
    return 0


def optimization_function(u):
    return 0


# MPC loop
for t in range(total_sim_steps):
    pass
