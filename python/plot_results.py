import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
results_dir = "results/"

Y_real = np.loadtxt(results_dir + "predictions/y_real.csv", dtype=np.float64)
Y_pred = np.loadtxt(results_dir + "predictions/y_pred.csv", dtype=np.float64)

metrics_df = pd.read_csv(results_dir + "models/hp_metrics.csv")


# Plot prediction
def plot_pred(save=False):
    fig, axs = plt.subplots(2, 1)
    fig.set_size_inches(12, 6)

    axs[0].plot(Y_real[:, 0], color="k", label=r"$w_e$")
    axs[0].plot(Y_pred[:, 0], color="r", label=r"$\hat{w}_e$")
    axs[0].set_xlabel(r"t")

    axs[1].plot(Y_real[:, 1], color="k", label=r"$h$")
    axs[1].plot(Y_pred[:, 1], color="r", label=r"$\hat{h}$")

    fig.suptitle("Outputs prediction")
    axs[0].legend()
    axs[1].legend()
    fig.tight_layout()

    plt.show()


def plot_heatmap(batch_size, save=False):
    fig = plt.figure(figsize=(8, 6))

    heatmap_df = metrics_df[metrics_df["batch_size"] == batch_size][
        ["P", "Q", "loss"]
    ].pivot(index="Q", columns="P", values="loss")

    sns.heatmap(heatmap_df, annot=True, cmap="magma", fmt=".3f")
    plt.title(f"Erro de predição para batch_size={batch_size}")
    fig.tight_layout()

    if save:
        plt.savefig(results_dir + f"plots/hp_metrics_{batch_size}.png")
    plt.show()


def histogram_error(bins, save=False):
    error = Y_pred - Y_real
    fig, axs = plt.subplots(2, 1, figsize=(10, 6))
    for i, ax in enumerate(axs):
        sns.histplot(error[:, i], bins=32, ax=ax)
        avg = np.mean(error[:, i])
        std = np.std(error[:, i])
        ax.axvline(
            avg,
            color="red",
            linestyle="dashed",
            linewidth=2,
            label=f"Mean: {avg:.2f}. Std: {std:.2f}",
        )
        ax.set_title(r"Histograma do erro de previsão de $w_e$")
        ax.set_xlabel(r"k")
        ax.legend()
    plt.subplots_adjust(hspace=0.5)
    plt.show()


batch_size = 16
plot_heatmap(batch_size, save=True)

bins = 32
histogram_error(bins)
