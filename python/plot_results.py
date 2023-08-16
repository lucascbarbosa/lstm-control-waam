import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data_dir = "C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/database/"
results_dir = "C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/results/"

Y_test_seq = np.loadtxt(results_dir + "y_test_seq.csv", dtype=np.float64)
Y_pred_seq = np.loadtxt(results_dir + "y_pred_seq.csv", dtype=np.float64)

fig, axs = plt.subplots(2, 1)
fig.set_size_inches(15, 6)

axs[0].plot(Y_test_seq[:, 0], color="k", label=r"$w_e$")
axs[0].plot(Y_pred_seq[:, 0], color="r", label=r"$\hat{w}_e$")
axs[0].set_xlabel(r"t")

axs[1].plot(Y_test_seq[:, 1], color="k", label=r"$h$")
axs[1].plot(Y_pred_seq[:, 1], color="r", label=r"$\hat{h}$")

fig.suptitle('Outputs prediction')
axs[0].legend()
axs[1].legend()
fig.tight_layout()

plt.show()
