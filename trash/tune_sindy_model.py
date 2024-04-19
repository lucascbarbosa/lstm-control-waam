"""SINDY model script."""
import matplotlib.pyplot as plt
from models.process_data import (
    build_train_data,
    load_train_data,
    normalize_data,
    standardize_data,
)
import pandas as pd
import numpy as np
import os
import pysindy as ps

#############
# Filepaths #
data_dir = "database/"
results_dir = "results/"

# Load database
beads_train = [1]
beads_test = [1]

build_train_data(data_dir + "experiment/", beads_train, beads_test)
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
    # test_y_stds = output_test.std(axis=0)
    # test_y_means = output_test.mean(axis=0)
    output_train = standardize_data(output_train)

elif output_scaling == "min-max":
    train_y_mins = output_train.min(axis=0)
    train_y_maxs = output_train.max(axis=0)
    # test_y_mins = output_test.min(axis=0)
    # test_y_maxs = output_test.max(axis=0)
    output_train = normalize_data(output_train)

# Add noise
input_train += np.random.normal(loc=2e-1, scale=1e-2, size=input_train.shape)
output_train += np.random.normal(loc=2e-1, scale=1e-2, size=output_train.shape)

#########
# Sindy #
sparse_regression_optimizer = ps.STLSQ(threshold=1e-3)
model = ps.SINDy(optimizer=sparse_regression_optimizer, discrete_time=True)

# Fit
model.fit(output_train, u=input_train, t=1)

# Simulate
output_pred = model.simulate(
    normalize_data(output_test)[0], t=input_test.shape[0], u=input_test)
output_pred = output_pred * (train_y_maxs - train_y_mins) + train_y_mins
print(f"MSE: {np.sum(output_pred**2 - output_test**2).round(5)}")

# Plot
plt.plot(output_test, label='measured')
plt.plot(output_pred, label='predicted')
plt.legend()
plt.show()
