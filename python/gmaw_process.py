import numpy as np
from keras.models import load_model
import casadi as ca

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
Aw = np.pi * rw ** 2


def gmaw(f, Ir, lc, v, x, C1, C2, DeltaT, rho, Aw, kv, Ra, Rs, Voc, Vo, Ea, Ls, n, nd, k, alpha):
    ls = x[0]
    I = x[1]

    x1_dot = f - (C2 * rho * ls * I ** 2 + C1 * I) / Aw
    x2_dot = (kv * Ir - (Ra + Rs + rho * ls + kv) * I + (Voc - Vo) - Ea * (lc - ls)) / Ls

    x_dot = np.array([x1_dot, x2_dot])

    Q = n * (Ra * I ** 2 + (Ea * (lc - ls) + Vo) * I)
    Ac = (C2 * rho * ls * I ** 2 + C1 * I) / v

    kw = np.sqrt((2 - nd) / nd)

    we = np.sqrt((0.4 * alpha / (kw * v)) ** 2 - (2 * Ac / (kw ** 2 + 1) - Q * alpha / (k * DeltaT * v)) / kw) - 0.4 * alpha / (kw * v)
    h = nd * Ac / we

    return x_dot, Q, Ac, we, h