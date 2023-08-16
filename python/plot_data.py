import pandas as pd
import numpy as np
from load_data import load_data, normalize_data, sequence_data
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data_dir = "C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/database/"
results_dir = "C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/results/"
X_train, Y_train, X_test, Y_test = load_data(data_dir)

# Inputs
# Train
N = 100
fig, axs = plt.subplots(2, 1)
fig.set_size_inches(8, 6)
axs[0].step(range(N), X_train[:N, 0])
axs[0].set_title(r"$f$")

axs[1].step(range(N), X_train[:N, 1])
axs[1].set_xlabel(r"k")
axs[1].set_title(r"$Ir$")

fig.suptitle('Entradas de dados de treino')
fig.savefig(results_dir + "train_inputs.png")

# Test
fig, axs = plt.subplots(2, 1)
fig.set_size_inches(8, 6)
axs[0].step(range(N), X_test[:N, 0])
axs[0].set_title(r"$f$")

axs[1].step(range(N), X_test[:N, 1])
axs[1].set_xlabel(r"k")
axs[1].set_title(r"$Ir$")

fig.suptitle('Entradas de dados de teste')
fig.savefig(results_dir + "test_inputs.png")

# Inputs
# Train
fig, axs = plt.subplots(2, 1)
fig.set_size_inches(8, 6)
axs[0].plot(Y_train[:N, 0])
axs[0].set_title(r"$w_e$")

axs[1].plot(Y_train[:N, 1])
axs[1].set_xlabel(r"k")
axs[1].set_title(r"$h$")

fig.suptitle('Saídas de dados de treino')
fig.savefig(results_dir + "train_outputs.png")

# Test
fig, axs = plt.subplots(2, 1)
fig.set_size_inches(8, 6)
axs[0].plot(Y_test[:N, 0])
axs[0].set_title(r"$w_e$")

axs[1].plot(Y_test[:N, 1])
axs[1].set_xlabel(r"k")
axs[1].set_title(r"$k$")

fig.suptitle('Saídas de dados de teste')
fig.savefig(results_dir + "test_outputs.png")


plt.show()
