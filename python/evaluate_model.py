import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
# data_dir = "C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/database/"
# results_dir = "C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/results/"

# Y_real = np.loadtxt(results_dir + "y_real.csv", dtype=np.float64)
# Y_pred = np.loadtxt(results_dir + "y_pred.csv", dtype=np.float64)


def compute_metrics(Y_pred, Y_real):
    mses = []
    error = Y_pred - Y_real
    sq_error = error**2
    mses = np.mean(sq_error, axis=0)
    return mses


def histogram_error(Y_pred, Y_real, bins):
    error = Y_pred - Y_real
    fig, axs = plt.subplots(2, 1, figsize=(10, 6))
    for i, ax in enumerate(axs):
        sns.histplot(error[:, i], bins=32, ax=ax)
        avg = np.mean(error[:, i])
        std = np.std(error[:, i])
        ax.axvline(avg, color='red', linestyle='dashed',
                   linewidth=2, label=f'Mean: {avg:.2f}. Std: {std:.2f}')
        ax.set_title(r'Histograma do erro de previsão de $w_e$')
        ax.set_xlabel(r'k')
        ax.legend()
    plt.subplots_adjust(hspace=0.5)
    plt.show()


# mses = compute_metrics(Y_pred, Y_real)

# bins = 32
# histogram_error(Y_pred, Y_real, 32)
