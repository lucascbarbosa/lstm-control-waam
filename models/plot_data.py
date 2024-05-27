import pandas as pd
import numpy as np
from models.process_data import (
    load_train_data,
    normalize_data,
)
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data_dir = "database/"
results_dir = "results/"


# Functions
def pow2wfs(power_data):
    """
    Covert power to wfs

    Args:
        power_data (float): power wfs_command

    Returns:
        float: wfs wfs_command
    """
    return (power_data * 9 / 100) + 1.5


def plot_calibration(
    wfs_command_data,
    ts_command,
    w_data,
    fig_filename,
    N
):
    """
    Plot experiment data of specific welded bead

    Args:
        ts_command (int): ts command
        wfs_command_data(np.array): wfs_command data
        w_data(np.array): width data
        fig_filename (str): figure file name
        scale (bool): whether to scale data
        save (bool): whether to save data
        N (int): number of samples of data array

    """
    if N is None:
        N = w_data.shape[0]

    fig, ax = plt.subplots(1)
    fig.set_size_inches(figsize)
    ax.set_xlabel("t")
    ax2 = ax.twinx()
    ax2.set_xlabel("t")
    plt.title(f"TS: {ts_command} (mm/s)")
    if scale:
        ax.step(
            wfs_command_data[:, 0],
            wfs_command_data[:, 1],
            where="post",
            color="b",
            linestyle='--',
            label="Scaled WFS command",
        )
        ax2.plot(w_data[:, 0],
                 w_data[:, 1],
                 color="#006400",
                 label="Scaled Width"
                 )
        ax.set_ylabel("WFS")
        ax2.set_ylabel("W")
    else:
        ax.step(
            wfs_command_data[:, 0],
            wfs_command_data[:, 1],
            where="post",
            color="b",
            linestyle='--',
            label="WFS command",
        )
        ax2.plot(w_data[:, 0],
                 w_data[:, 1],
                 color="#006400",
                 label="Width")
        ax.set_ylabel("WFS (mm/min)")
        ax2.set_ylabel("W (mm)")

    fig.tight_layout()
    fig.legend(bbox_to_anchor=(0.94, 0.92))

    if source == "experiment/calibration" and end_time is not None:
        ax.set_xlim(5.0, end_time)
        ax.set_xticks(np.arange(5.0, end_time+0.1, 0.5))
        # ax2.set_xlim(5.0, end_time)
        # ax2.set_xticks(np.arange(5.0, end_time+0.1, 0.5))

    if source == "simulation/calibration":
        ax.set_xlim(0.2, w_data[-1, 0])
        ax.set_xticks(np.arange(0, w_data[-1, 0]+0.3, 10))
        # ax2.set_xlim(0.2, w_data[-1, 0])
        # ax2.set_ylim(w_data[1:, 1].min(), w_data[1:, 1].max())
        # ax2.set_xticks(np.arange(0, w_data[-1, 0]+0.3, 10))

    if save:
        if scale:
            fig.savefig(
                results_dir + f"plots/{source}/{source.split('/')[0]}_calibration__{fig_filename}.{format}")
        else:
            fig.savefig(
                results_dir + f"plots/{source}/{source.split('/')[0]}_calibration__{fig_filename}__raw.{format}")
        plt.close()
    else:
        fig.show()


def plot_control(
    wfs_command_data,
    ts_command,
    w_data,
    ref_data,
    cost_data,
    fig_filename,
    N
):
    """
    Plot experiment data of specific welded bead

    Args:
        ts_command (int): ts command
        wfs_data(np.array): wfs data
        wfs_command_data(np.array): wfs wfs_command data
        w_data(np.array): width data
        fig_filename (str): figure file name
        scale (bool): whether to scale data
        save (bool): whether to save data
        N (int): number of samples of data array

    """
    def create_control_diff(u):
        u_diff = u.copy()
        u_diff[1:] = u_diff[1:] - u_diff[:-1]
        return u_diff

    if N is None:
        N = w_data.shape[0]

    overshoot = (w_data[:, 1].max() / w_data[-1, 1]) - 1.0

    du = create_control_diff(wfs_command_data[:, 1])
    du_mean = du.mean(axis=0)

    setting_time = w_data[np.where(w_data[:, 1] > 0.95 * w_data[-1, 1])][0, 0]

    error_ss = ref_data[-1, 1] - w_data[-1, 1]
    print(f"Overshoots: {overshoot*100:.2f}%")
    print(f"dU Médio: {du_mean * 100/wfs_command_data[:, 1].max(axis=0):.2f}%")
    print(f"Tempo de assentamento: {setting_time} s")
    print(
        f"Erro estacionário: {error_ss:.2f} mm ({error_ss*100/ref_data[-1,1]:.2f} %)\n")

    fig, axs = plt.subplots(2)
    fig.set_size_inches(figsize)
    axs[0].set_xlabel("t")
    ax2 = axs[0].twinx()
    ax2.set_xlabel("t")
    plt.title(f"TS: {ts_command} (mm/s)")
    axs[0].step(
        wfs_command_data[:, 0],
        wfs_command_data[:, 1],
        where="post",
        color="b",
        linestyle='--',
        label="WFS command",
    )
    ax2.plot(w_data[:, 0],
             w_data[:, 1],
             color="#006400",
             label="Width")
    axs[0].set_ylabel("WFS (mm/min)")
    ax2.set_ylabel("W (mm)")
    ax2.plot(ref_data[:, 0],
             ref_data[:, 1],
             color="#00AA00",
             linestyle='--',
             label="Reference width")
    fig.legend(bbox_to_anchor=(0.94, 0.92))

    # Costs
    axs[1].set_title("Cost")
    axs[1].plot(cost_data[:, 0],
                cost_data[:, 1],
                color="b",
                label='Input Cost')
    # axs[1].fill_between(cost_data[:, 0], 0, cost_data[:, 1],
    #                     color='b', alpha=0.3)
    axs[1].plot(cost_data[:, 0],
                cost_data[:, 2],
                color="#006400",
                label='Output Cost')
    # axs[1].fill_between(cost_data[:, 0], cost_data[:, 1], cost_data[:, 2],
    #                     color='#006400', alpha=0.3)
    axs[1].legend()
    fig.tight_layout()

    if source == "simulation":
        plt.xlim(0, 12)

    if save:
        fig.savefig(
            results_dir + f"plots/{source}/{source.split('/')[0]}_control__{fig_filename}.{format}")
        plt.close()
    else:
        fig.show()


N = None  # Horizon plotted
end_time = None
scale = True
save = True
figsize = (10, 4)
format = "eps"
source = "simulation/control"
if source in ['experiment/control', 'experiment/calibration']:
    experiment_matrix = pd.read_excel(
        data_dir + f'{source}/experiment_matrix.xlsx')
    data_path = data_dir + f"{source}/"

ts_min, ts_max = 4, 20
if source == "simulation/calibration":
    for ts in [4, 8, 12, 16, 20]:
        input_train, output_train, input_test, output_test = load_train_data(
            data_dir + f'simulation/calibration/TS {ts}/')

        fig_filename = f"ts_{ts}__train"

        wfs_command_data = np.vstack((input_train[:, 0], input_train[:, 1])).T

        ts_command_data = np.vstack((input_train[:, 0], input_train[:, 2])).T
        ts_command = int(ts_command_data[0, 1])
        w_data = output_train

        if scale:
            wfs_command_data[:, 1:] = normalize_data(
                wfs_command_data[:, 1:])
            w_data[:, 1:] = normalize_data(w_data[:, 1:])
            ts_command_data[:, 1:] = normalize_data(
                ts_command_data[:, 1:], ts_min, ts_max)

        plot_calibration(
            wfs_command_data,
            ts_command,
            w_data,
            fig_filename,
            N
        )

        fig_filename = f"ts_{ts}__test"
        wfs_command_data = np.vstack((input_test[:, 0], input_test[:, 1])).T

        ts_command_data = np.vstack((input_test[:, 0], input_test[:, 2])).T
        ts_command = int(ts_command_data[0, 1])

        w_data = output_test
        if scale:
            wfs_command_data[:, 1:] = normalize_data(
                wfs_command_data[:, 1:])
            w_data[:, 1:] = normalize_data(w_data[:, 1:])
            ts_command_data[:, 1:] = normalize_data(
                ts_command_data[:, 1:], ts_min, ts_max)

        plot_calibration(
            wfs_command_data,
            ts_command,
            w_data,
            fig_filename,
            N
        )

if source == "experiment/calibration":
    bead_idxs = list(range(1, 16))
    for bead_idx in bead_idxs:
        bead_filename = data_path + f"series/bead{bead_idx}"

        wfs_command_data = pd.read_csv(
            bead_filename + "_wfs_command.csv").to_numpy()

        w_data = pd.read_csv(bead_filename + "_w.csv").to_numpy()

        ts_command_data = pd.read_csv(
            bead_filename + "_ts_command.csv").to_numpy()
        ts_command = int(ts_command_data[0, 1])

        fig_filename = f"bead{bead_idx}"

        if scale:
            wfs_command_data[:, 1:] = normalize_data(
                wfs_command_data[:, 1:])
            w_data[:, 1:] = normalize_data(w_data[:, 1:])
            ts_command_data[:, 1:] = normalize_data(
                ts_command_data[:, 1:], ts_min, ts_max)

        plot_calibration(
            wfs_command_data,
            ts_command,
            w_data,
            fig_filename,
            N
        )


if source == "experiment/control":
    bead_idxs = list(range(1, 3))
    for bead_idx in bead_idxs:
        bead_filename = data_path + f"series/bead{bead_idx}"

        wfs_command_data = pd.read_csv(
            bead_filename + "_wfs_command.csv").to_numpy()

        w_data = pd.read_csv(bead_filename + "_w.csv").to_numpy()

        ts_command_data = pd.read_csv(
            bead_filename + "_ts_command.csv").to_numpy()
        ts_command = int(ts_command_data[0, 1])

        ref_data = np.zeros(w_data.shape)
        ref_data[:, 0] = w_data[:, 0]
        ref_data[:, 1] = 9.0

        fig_filename = f"bead{bead_idx}"

        plot_control(
            wfs_command_data,
            ts_command,
            w_data,
            ref_data,
            fig_filename,
            N
        )

if source == "simulation/control":
    for model in ['lstm', 'tf']:
        for ts in [4, 8, 12, 16, 20]:
            wfs_command_data = pd.read_csv(
                data_dir +
                f"simulation/control/{model}__ts_{ts}__step__wfs_command.csv"
            ).to_numpy()
            ts_command_data = pd.read_csv(
                data_dir +
                f"simulation/control/{model}__ts_{ts}__step__ts_command.csv"
            ).to_numpy()
            w_data = pd.read_csv(
                data_dir + f"simulation/control/{model}__ts_{ts}__step__w.csv"
            ).to_numpy()
            cost_data = pd.read_csv(
                data_dir +
                f"simulation/control/{model}__ts_{ts}__step__cost.csv"
            ).to_numpy()
            ref_data = pd.read_csv(
                data_dir +
                f"simulation/control/{model}__ts_{ts}__step__reference.csv"
            ).to_numpy()
            fig_filename = f"{model}__ts_{ts}__step"
            plot_control(
                wfs_command_data,
                ts,
                w_data,
                ref_data,
                cost_data,
                fig_filename,
                N
            )
