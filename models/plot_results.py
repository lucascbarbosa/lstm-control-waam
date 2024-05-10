import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import shapiro

# Load data
data_dir = "database/"
results_dir = "results/"


# Plot prediction
def plot_prediction(source="simulation", save=False):
    if source == "simulation":
        fig, axs = plt.subplots(2, 1)
        fig.set_size_inches(figsize)

        axs[0].plot(Y_real[:, 0] * 1000, color="k", label="Measured")
        axs[0].plot(Y_pred[:, 0] * 1000, color="r", label="Predicted")
        axs[0].set_xlabel(r"t")
        axs[0].set_title(r"$w_e\;(mm)$")

        axs[1].plot(Y_real[:, 1] * 1000, color="k", label="Measured")
        axs[1].plot(Y_pred[:, 1] * 1000, color="r", label="Predicted")
        axs[1].set_title(r"$h\;(mm)$")

        fig.suptitle("Outputs prediction")
        axs[0].legend()
        axs[1].legend()

    elif source == "experiment":
        fig = plt.figure(figsize=figsize)
        # fig.suptitle("Output prediction", fontsize=fontsize)
        plt.title(r"$W\;(mm)$", fontsize=fontsize)
        plt.plot(Y_real[:, 0], Y_real[:, 1], color="k", label="Measured")
        plt.plot(Y_pred[:, 0], Y_pred[:, 1], color="r", label="Predicted")
        plt.xlabel('t', fontsize=fontsize)
        plt.ylabel('Value', fontsize=fontsize)
        plt.legend(fontsize=fontsize)

    elif source == "mpc":
        fig = plt.figure(figsize=figsize)
        fig.suptitle("MPC control prediction")
        plt.title(r"$WFS\;(mm/s)$")
        plt.step(x=range(len(Y_real)), y=Y_real, color="k", label="Measured")
        plt.step(x=range(len(Y_pred)), y=Y_pred, color="r", label="Predicted")
        plt.legend()

    fig.tight_layout()
    if save:
        if source == "simulation":
            plt.savefig(
                results_dir + f"plots/simulation_lstm_prediction.{format}")
        elif source == "experiment":
            plt.savefig(
                results_dir
                + f"plots/experiment/calibration/calibration_bead{bead_test}_lstm_prediction.{format}"
            )
        elif source == "mpc":
            plt.savefig(results_dir + f"plots/mpc_lstm_prediction.{format}")
    plt.show()


def plot_heatmap(source, save=False):
    fig = plt.figure(figsize=figsize)

    heatmap_df = metrics_df[["P", "Q", "test_loss"]].pivot(
        index="Q", columns="P", values="test_loss")

    sns.heatmap(heatmap_df, annot=True, cmap="magma", fmt=".4f")
    plt.title(f"Hyperparameters heatmap error")
    fig.tight_layout()

    if save:
        plt.savefig(
            results_dir +
            f"plots/{source}/calibration/calibration_heatmap.{format}"
        )

    plt.tight_layout()
    plt.show()


def histogram_error(bins, source="simulation", save=False):
    error = Y_pred[:, 1] - Y_real[:, 1]
    if source == "simulation":
        fig, axs = plt.subplots(2, 1, figsize=figsize)
        for i, ax in enumerate(axs):
            _, p_val = shapiro(error[:, i])
            sns.histplot(error[:, i], bins=bins, ax=ax)
            avg = np.mean(error[:, i])
            std = np.std(error[:, i])
            ax.axvline(
                avg,
                color="red",
                linestyle="dashed",
                linewidth=2,
                label=f"Mean: {avg*1e6:.1f}e-6. Std: {std*1e5:.1f}e-5 P-valor: {p_val*1e10: .1f}e-10",
            )
            ax.set_title(r"Prediction error histogram for $w_e$")
            ax.set_xlabel("Error", fontsize=fontsize)
            ax.legend(fontsize=fontsize)

        plt.subplots_adjust(hspace=0.5)
        if save:
            plt.savefig(
                results_dir + f"plots/{source}_error_histogram.{format}")

    elif source == "experiment":
        fig, ax = plt.subplots(figsize=figsize)
        sns.histplot(error, bins=bins, ax=ax)
        _, p_val = shapiro(error)
        avg = np.mean(error)
        std = np.std(error)
        ax.axvline(
            avg,
            color="red",
            linestyle="dashed",
            linewidth=2,
            label=f"Mean: {avg:.2f} Std: {std:.2f} P-valor: {p_val: .4f}",
        )

        # ax.set_title(r"Prediction error histogram for $w_e$")
        ax.set_xlabel(r"error")
        ax.legend()

        plt.subplots_adjust(hspace=0.5)
        if save:
            plt.savefig(
                results_dir
                + f"plots/experiment/calibration/{source}_bead{bead_test}_error_histogram.{format}"
            )

    plt.tight_layout()
    plt.show()


def plot_mpc(u, y, y_ref, save=True):
    def create_control_diff(u):
        u_diff = u.copy()
        u_diff[1:] = u_diff[1:] - u_diff[:-1]
        return u_diff

    u_labels = u.columns
    y_labels = y.columns

    u = u.to_numpy()
    y = y.to_numpy()

    overshoots = (y.max(axis=0) / y[-1, :]) - 1.0
    du = create_control_diff(u)
    du_means = du.mean(axis=0)
    rmses = ((y[2:, :] - y_ref) ** 2).mean(axis=0)

    print(f"Overshoots: {overshoots}")
    print(f"dU Médio: {du_means/u.max(axis=0)}")
    print(f"RMSE: {rmses}")
    # Plot inputs
    fig, axs = plt.subplots(2, 1)
    fig.set_size_inches(figsize)
    fig.suptitle("MPC Control Signal")

    for i in range(2):
        axs[i].plot(u[:, i], color="blue")
        axs[i].set_xlabel("t")
        axs[i].set_ylabel(u_labels[i])

    fig, axs = plt.subplots(2, 1)
    fig.set_size_inches(figsize)
    fig.suptitle("MPC Output")

    for i in range(2):
        axs[i].plot(y[:, i] * 1000, color="red")
        axs[i].set_xlabel("t")
        axs[i].set_ylabel(y_labels[i] + " (mm)")
        axs[i].axhline(y_ref[i] * 1000, color="black", linestyle="--")

    plt.tight_layout()

    if save:
        plt.savefig(results_dir + f"plots/{source}_mpc_outputs.{format}")
    plt.show()


source = "experiment"
save = True
fontsize = 20
figsize = (10, 4)
format = "eps"
metrics_df = pd.read_csv(results_dir + f"models/{source}/hp_metrics.csv")
metrics_df["test_loss"] = metrics_df["test_loss"].apply(
    lambda x: np.nan if x > 1 else x
)

# mpc_u = pd.read_csv(results_dir + f"mpc/{source}/u.csv")
# mpc_u = mpc_u.iloc[:-1, :]
# mpc_y = pd.read_csv(results_dir + f"mpc/{source}/y.csv")

if source == "simulation":
    Y_real = np.loadtxt(
        results_dir + f"predictions/{source}/y_real.csv", dtype=np.float64
    )
    Y_pred = np.loadtxt(
        results_dir + f"predictions/{source}/y_pred.csv", dtype=np.float64
    )

    plot_prediction(source=source, save=True)

    # bins = 32
    # histogram_error(bins, source=source, save=True)

    # batch_sizes = [16, 32, 64]
    # for batch_size in batch_sizes:
    #     plot_heatmap(batch_size, source=source, save=True)

    # plot_mpc(mpc_u, mpc_y, y_means,save=False)

elif source == "experiment":
    beads_test = [3, 6, 10, 15]
    for bead_test in beads_test:
        Y_real = np.loadtxt(
            results_dir + f"predictions/{source}/bead{bead_test}_y_real.csv",
            dtype=np.float64,
        )
        Y_pred = np.loadtxt(
            results_dir + f"predictions/{source}/bead{bead_test}_y_pred.csv",
            dtype=np.float64,
        )

        plot_prediction(source=source, save=save)

        bins = 32
        histogram_error(bins, source=source, save=save)

    # plot_heatmap(source=source, save=True)

    # plot_mpc(mpc_u, mpc_y, y_means,save=False)
