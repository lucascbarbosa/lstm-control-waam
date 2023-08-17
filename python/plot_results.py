import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data_dir = "C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/database/"
results_dir = "C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/results/"

Y_real = np.loadtxt(results_dir + "y_real.csv", dtype=np.float64)
Y_pred = np.loadtxt(results_dir + "y_pred.csv", dtype=np.float64)

fig, axs = plt.subplots(2, 1)
fig.set_size_inches(12, 6)

axs[0].plot(Y_real[:, 0], color="k", label=r"$w_e$")
axs[0].plot(Y_pred[:, 0], color="r", label=r"$\hat{w}_e$")
axs[0].set_xlabel(r"t")

axs[1].plot(Y_real[:, 1], color="k", label=r"$h$")
axs[1].plot(Y_pred[:, 1], color="r", label=r"$\hat{h}$")

fig.suptitle('Outputs prediction')
axs[0].legend()
axs[1].legend()
fig.tight_layout()

plt.show()
