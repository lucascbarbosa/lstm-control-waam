import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import shapiro

# Load data
data_dir = "database/"
results_dir = "results/"


#############
# Functions #
def plot_prediction():
    fig = plt.figure(figsize=figsize)
    # fig.suptitle("Output prediction", fontsize=fontsize)
    plt.plot(Y_real[:, 0], Y_real[:, 1], color="k", label="Measured")
    plt.plot(Y_pred[:, 0], Y_pred[:, 1], color="r", label="Predicted")
    plt.xlabel('t (s)', fontsize=fontsize)
    plt.ylabel("W (mm)", fontsize=fontsize)
    plt.legend(fontsize=fontsize)

    fig.tight_layout()
    if save:
        if source == "simulation":
            plt.savefig(
                results_dir
                + f"plots/simulation/calibration/simulation_calibration__ts_{ts}__prediction.{format}"
            )
        elif source == "experiment":
            plt.savefig(
                results_dir
                + f"plots/experiment/calibration/experiment_calibration__ bead{bead_test}__prediction.{format}"
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


def histogram_error():
    error = Y_pred[:, 1] - Y_real[:, 1]
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
        label=f"Mean: {avg:.2f} Std: {std:.2f} P-valor: {p_val: .3e}",
    )

    # ax.set_title(r"Prediction error histogram for $w_e$")
    ax.set_xlabel(r"error")
    ax.legend()

    plt.subplots_adjust(hspace=0.5)
    if save:
        if source == "experiment":
            plt.savefig(
                results_dir
                + f"plots/experiment/calibration/experiment_calibration__bead{bead_test}__error_histogram.{format}"
            )
        elif source == "simulation":
            plt.savefig(
                results_dir
                + f"plots/simulation/calibration/simulation_calibraation__ts_{ts}__error_histogram.{format}"
            )
    plt.tight_layout()
    plt.show()


def plot_horizon_metrics(t, y_forecast, y, y_ref):
    def colors_from_values(values, palette_name):
        # normalize the values to range [0, 1]
        normalized = (values - min(values)) / (max(values) - min(values))
        # convert to indices
        indices = np.round(normalized * (len(values) - 1)).astype(np.int32)
        # use the indices to get the colors
        palette = sns.color_palette(palette_name, len(values))
        return np.array(palette).take(indices, axis=0)

    forecast_df = []
    for i in range(len(t)):
        ref_time = t[i]
        forecast = y_forecast[i, :]
        for j in range(min(len(forecast), len(t)-i)):
            time = t[i+j]
            y_hat = forecast[j]
            y_real = y[i+j]
            forecast_df.append(
                {'ref_time': ref_time,
                 'time': time,
                 'h': j+1,
                 'forecast': y_hat,
                 'value': y_real})
    forecast_df = pd.DataFrame(forecast_df)
    horizon_metrics = []
    for fh_index, fh_group in forecast_df.groupby('h'):
        y_hat = fh_group['forecast']
        y_real = fh_group['value']
        error = np.abs((y_hat - y_real) / y_real)
        error_mean = error.mean()
        error_std = error.std()
        horizon_metrics.append(
            {'h': fh_index, 'mean': error_mean, 'std': error_std})
    horizon_metrics = pd.DataFrame(horizon_metrics)
    horizon_metrics['h'] = horizon_metrics['h'] / len(horizon_metrics)
    horizons = np.arange(0.1, 1.1, 0.1)
    horizon_metrics = horizon_metrics[horizon_metrics['h'].isin(horizons)]
    horizon_metrics['std'] = horizon_metrics['std'].fillna(1.0)
    plt.figure(figsize=figsize)
    sns.barplot(data=horizon_metrics, x='h', y='mean',
                # errorbar=(horizon_metrics['mean']-3*horizon_metrics['std'],
                #           horizon_metrics['mean']+3*horizon_metrics['std']),
                palette=colors_from_values(horizon_metrics['mean'], "rocket"))
    plt.xlabel('Horizonte de previsão (N)', fontsize=fontsize)
    plt.ylabel('MAPE', fontsize=fontsize)
    if save:
        plt.savefig(results_dir + f"plots/mpc/mpc_horizons.{format}")
    plt.show()

    return forecast_df, horizon_metrics


source = "simulation/calibration"
save = True
fontsize = 16
figsize = (10, 4)
format = "eps"
weight_control = 1.0
weight_output = 1.0
if source == "experiment" or source == "simulation":
    metrics_df = pd.read_csv(results_dir + f"models/{source}/hp_metrics.csv")
    metrics_df["test_loss"] = metrics_df["test_loss"].apply(
        lambda x: np.nan if x > 1 else x
    )

if source == "simulation/calibration":
    for ts in [4, 8, 12, 16, 20]:
        Y_real = np.loadtxt(
            results_dir +
            f"predictions/{source.split('/')[0]}/calibration/ts__{ts}__y_real.csv",
            dtype=np.float64
        )
        Y_pred = np.loadtxt(
            results_dir +
            f"predictions/{source.split('/')[0]}/calibration/ts__{ts}__y_pred.csv",
            dtype=np.float64
        )

        plot_prediction()

        bins = 128
        histogram_error()

        # batch_sizes = [16, 32, 64]
        # for batch_size in batch_sizes:
        #     plot_heatmap(batch_size, source=source, save=True)

        # plot_mpc(mpc_u, mpc_y, y_means,save=False)

elif source == "experiment":
    beads_test = [3, 6, 10, 15]
    for bead_test in beads_test:
        Y_real = np.loadtxt(
            results_dir +
            f"predictions/{source.split('/')[0]}/calibration/bead{bead_test}__y_real.csv",
            dtype=np.float64,
        )
        Y_pred = np.loadtxt(
            results_dir +
            f"predictions/{source.split('/')[0]}/calibration/bead{bead_test}__y_pred.csv",
            dtype=np.float64,
        )

        plot_prediction()

        bins = 32
        histogram_error()

    # plot_heatmap(source=source, save=True)

    # plot_mpc(mpc_u, mpc_y, y_means,save=False)

elif source == "mpc":
    pass
