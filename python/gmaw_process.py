import numpy as np
from keras.models import load_model
import casadi as ca
from python.process_data import (
    load_data,
    normalize_data,
    standardize_data,
)
from scipy.integrate import odeint

#############
# Filepaths #
data_dir = "database/"
results_dir = "results/"

##############
# Parameters #
n = 0.655
nd = 0.958
Ea = 723.2561
Vo = 5.1782
Ra = 0.0201
Rs = 0.004
Ls = 0.00014
Voc = 31
kv = 10  # 10, 0.0001
lc = 0.01
v = 0.12
DeltaT = 1300
rho = 0.1319
k = 24
alpha = 7.79 * 10 ** (-6)
C1 = 3.2634 * 10 ** (-10)
C2 = 1.1836 * 10 ** (-9)
rw = 0.0006

lso = 0.0041
Io = 147.79
fo = 0.055
Ir = 146
weo = 0.0041
ho = 0.0012

kw = np.sqrt((2 - nd) / nd)
Aw = np.pi * rw**2

#################
# Load database #
inputs_train, outputs_train, inputs_test, outputs_test = load_data(data_dir)
num_features_input = inputs_train.shape[1]
num_features_output = outputs_train.shape[1]

# Slice database to fit sequencing
inputs_train = inputs_train[:1000, :]
outputs_train = outputs_train[:1000, :]
inputs_test = inputs_test[:1000, :]
outputs_test = outputs_test[:1000, :]

# # Scale database
# inputs_train = normalize_data(inputs_train)
# inputs_test = normalize_data(inputs_test)
# outputs_train = standardize_data(outputs_train)
# outputs_test = standardize_data(outputs_test)


def gmaw(u, x):
    ls = x[0]
    I = x[1]

    f = u[0]
    Ir = u[1]

    x1_dot = f - (C2 * rho * ls * I**2 + C1 * I) / Aw
    x2_dot = (
        kv * Ir - (Ra + Rs + rho * ls + kv) * I + (Voc - Vo) - Ea * (lc - ls)
    ) / Ls

    x_dot = np.array([x1_dot, x2_dot])

    Q = n * (Ra * I**2 + (Ea * (lc - ls) + Vo) * I)
    Ac = (C2 * rho * ls * I**2 + C1 * I) / v

    we = np.sqrt(
        (0.4 * alpha / (kw * v)) ** 2
        - (2 * Ac / (kw**2 + 1) - Q * alpha / (k * DeltaT * v)) / kw
    ) - 0.4 * alpha / (kw * v)

    h = nd * Ac / we

    return x_dot, Q, Ac, we, h


# Load keras model
best_model_id = 33
best_model = load_model(
    results_dir + f"models/best/run_{best_model_id:03d}.keras"
)

outputs_gmaw = np.zeros(outputs_train.shape)
outputs_gmaw[0, :] = outputs_train[0, :]
x = [0.0, 0.0]  # initial state
step = 1e-5

for i in range(inputs_train.shape[0] - 1):
    u = inputs_train[i, :]
    t_span = [0, step]
    x_dot, Q, Ac, we, h = gmaw(u, x)
    x = x_dot * step + x
    outputs_gmaw[i + 1, :] = [we, h]