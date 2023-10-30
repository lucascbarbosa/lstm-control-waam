from python.gmaw_process import *
from python.process_data import load_data

import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
from tensorflow.python.ops import array_ops

import numpy as np
import pandas as pd
import os
import time
from multiprocessing import Pool, cpu_count

#############
# Filepaths #
data_dir = "database/"
results_dir = "results/"

#########
# Loads #
# Load data
inputs_train, outputs_train, _, _ = load_data(data_dir)
u_mins = inputs_train.min(axis=0)
u_maxs = inputs_train.max(axis=0)
y_means = outputs_train.mean(axis=0)
y_stds = outputs_train.std(axis=0)

# Initial conditions
x0 = [1e-5, 1e-5]
y0 = gmaw_outputs(x0)
y0 = np.array(y0).reshape((1, 2))

# Simulation parameters
step = 1e-5
sim_time = 1e-2
num_time_steps = 50

# Simulation data
x = np.zeros((num_time_steps, 2))
x[0, :] = x0
y = np.zeros((num_time_steps, 2))
y[0, :] = y0
u = np.zeros((num_time_steps, 2))

# Desired outputs
y_ref = y_means


#############
# Functions #
def pi_control(K, x, z):
    x = np.hstack((np.array(x).reshape((1, 2)), z.reshape((1, 2)))).reshape(
        (4, 1)
    )
    return (K @ x).T


# Controler
K = np.array(
    [[15.19, 7.7e-8, 297.75, -954.65], [-5.5e3, 0.41, -9.55e5, -2.98e5]]
)
# Simulate
x_row = x0
y_row = y0
error = y_ref - y_row
sum_error = error

for t in range(1, num_time_steps):
    u_row = pi_control(K, x_row, sum_error)
    u[t - 1, :] = u_row
    print(f"u_row: {u_row}")
    print(f"sum_error: {sum_error}")
    x_row = solve_rk4(gmaw_states, x_row, step, u_row.ravel().tolist())
    print(f"x_row: {x_row}")
    x[t, :] = x_row

    # Estimate using Dynamics
    y_row = np.array(gmaw_outputs(x_row))
    error = y_ref - y_row
    sum_error += error
    y[t, :] = y_row

u = u[:-1, :]

u = pd.DataFrame(u, columns=["f", "Ir"])
y = pd.DataFrame(y, columns=["we", "h"])


mpc_u = u
mpc_y = y
# u.to_csv(results_dir + "mpc/u.csv", index=False)
# y.to_csv(results_dir + "mpc/y.csv", index=False)
