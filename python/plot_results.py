import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from python.process_data import load_simulation, load_experiment
from scipy.stats import shapiro

# Load data
data_dir = "database/"
results_dir = "results/"
source = "experiment"

Y_real = np.loadtxt(
    results_dir + f"predictions/{source}/y_real.csv", dtype=np.float64
)
Y_pred = np.loadtxt(
    results_dir + f"predictions/{source}/y_pred.csv", dtype=np.float64
)

metrics_df = pd.read_csv(results_dir + f"models/{source}/hp_metrics.csv")
metrics_df["loss"] = metrics_df["loss"].apply(lambda x: np.nan if x > 1 else x)

mpc_u = pd.read_csv(results_dir + "mpc/u.csv")
mpc_u = mpc_u.iloc[:-1, :]
mpc_y = pd.read_csv(results_dir + "mpc/y.csv")

if source == "simulation":
    inputs_train, outputs_train, _, _ = load_simulation(data_dir)
    u_mins = inputs_train.min(axis=0)
    u_maxs = inputs_train.max(axis=0)
    y_means = outputs_train.mean(axis=0)
    y_stds = outputs_train.std(axis=0)

elif source == "experiment":
    input_train, output_train, _, _ = load_experiment(
        data_dir + f"{source}/", 1, 2
    )
    u_min = input_train.min()
    u_max = input_train.max()
    y_mean = output_train.mean()
    y_std = output_train.std()


# Plot prediction
def plot_prediction(source="simulation", save=False):
    if source == "simulation":
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

    elif source == "experiment":
        fig = plt.figure(figsize=(12, 6))
        fig.suptitle("Output prediction")
        plt.plot(Y_real, color="k", label=r"$w_e$")
        plt.plot(Y_pred, color="r", label=r"$\hat{w}_e$")
        plt.legend()

    fig.tight_layout()
    if save:
        plt.savefig(results_dir + f"plots/{source}__lstm_prediction.png")
    plt.show()


def plot_heatmap(batch_size, source="simulation", save=False):
    fig = plt.figure(figsize=(8, 6))

    heatmap_df = metrics_df[metrics_df["batch_size"] == batch_size][
        ["P", "Q", "loss"]
    ].pivot(index="Q", columns="P", values="loss")

    sns.heatmap(heatmap_df, annot=True, cmap="magma", fmt=".3f")
    plt.title(f"Erro de predição para batch_size={batch_size}")
    fig.tight_layout()

    if save:
        plt.savefig(
            results_dir + f"plots/{source}__hp_metrics_{batch_size}.png"
        )
    plt.show()


def histogram_error(bins, save=False):
    error = Y_pred - Y_real
    fig, axs = plt.subplots(2, 1, figsize=(10, 6))
    for i, ax in enumerate(axs):
        _, p_val = shapiro(error[:, i])
        sns.histplot(error[:, i], bins=32, ax=ax)
        avg = np.mean(error[:, i])
        std = np.std(error[:, i])
        ax.axvline(
            avg,
            color="red",
            linestyle="dashed",
            linewidth=2,
            label=f"Mean: {avg*1e6:.1f}e-6. Std: {std*1e5:.1f}e-5 P-valor: {p_val*1e10: .1f}e-10",
        )
        ax.set_title(r"Histograma do erro de previsão de $w_e$")
        ax.set_xlabel(r"k")
        ax.legend()
    plt.subplots_adjust(hspace=0.5)
    if save:
        plt.savefig(results_dir + f"plots/{source}__error_histogram.png")
    plt.show()


def plot_mpc(u, y, y_ref):
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
    fig.set_size_inches(12, 6)
    fig.suptitle("MPC Control Signal")

    for i in range(2):
        axs[i].plot(u[:, i], color="blue")
        axs[i].set_xlabel("t")
        axs[i].set_ylabel(u_labels[i])

    fig, axs = plt.subplots(2, 1)
    fig.set_size_inches(12, 6)
    fig.suptitle("MPC Output")

    for i in range(2):
        axs[i].plot(y[:, i], color="red")
        axs[i].set_xlabel("t")
        axs[i].set_ylabel(y_labels[i])
        axs[i].axhline(y_ref[i], color="black", linestyle="--")

    plt.tight_layout()
    plt.show()


plot_prediction(source=source, save=True)

# batch_size = 16
# plot_heatmap(batch_size, save=True)

# bins = 32
# histogram_error(bins, save=True)

# plot_mpc(mpc_u, mpc_y, y_means)
