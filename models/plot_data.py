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


def plot_simulation(
    wfs_data,
    w_data,
    fig_filename,
    N
):
    """
    Plot experiment data of specific welded bead

    Args:
        bead_idx (int): index of welded bead
        wfs_data(np.array): wfs data
        wfs_command_data(np.array): wfs wfs_command data
        w_data(np.array): width data
        fig_filename (str): figure file name
        scale (bool): whether to scale data
        save (bool): whether to save data
        N (int): number of samples of data array

    """
    if N == None:
        N = w_data.shape[0]

    fig, ax1 = plt.subplots()
    fig.set_size_inches((10, 6))
    ax1.set_xlabel("t")

    ax2 = ax1.twinx()
    if scale:
        ax1.step(
            wfs_data[:, 0],
            wfs_data[:, 1],
            where="post",
            linestyle="--",
            color="#6B66EC",
            label="Scaled WFS wfs_command",
        )
        ax2.plot(w_data[:, 0], w_data[:, 1],
                 color="#006400", label="Scaled width")
        ax1.set_ylabel("WFS")
        ax2.set_ylabel("W")
    else:
        ax1.step(
            wfs_data[:, 0],
            wfs_data[:, 1],
            where="post",
            linestyle="--",
            color="#6B66EC",
            label="WFS wfs_command",
        )
        ax2.plot(w_data[:, 0], w_data[:, 1],
                 color="#006400", label="Width")
        ax1.set_ylabel("WFS (m/min)")
        ax2.set_ylabel("W (mm)")

    fig.tight_layout()
    fig.legend(bbox_to_anchor=(0.94, 0.92))
    fig.show()

    if save:
        if scale:
            fig.savefig(results_dir + f"plots/{source}_{fig_filename}.png")
        else:
            fig.savefig(results_dir + f"plots/{source}_{fig_filename}_raw.png")


# def plot_experiment(
#     bead_idx,
#     wfs_data,
#     wfs_command_data,
#     w_data,
#     fig_filename,
#     N
# ):
#     """
#     Plot experiment data of specific welded bead
#
#     Args:
#         bead_idx (int): index of welded bead
#         wfs_data(np.array): wfs data
#         wfs_command_data(np.array): wfs wfs_command data
#         w_data(np.array): width data
#         fig_filename (str): figure file name
#         scale (bool): whether to scale data
#         save (bool): whether to save data
#         N (int): number of samples of data array
#
#     """
#     if N == None:
#         N = w_data.shape[0]
#
#     fig, ax1 = plt.subplots()
#     fig.set_size_inches((10, 6))
#     ax1.set_xlabel("t")
#
#     ax2 = ax1.twinx()
#
#     if scale:
#         ax1.step(
#             wfs_data[:, 0],
#             wfs_data[:, 1],
#             where="post",
#             color="#000080",
#             label="Scaled WFS value",
#         )
#         ax1.step(
#             wfs_command_data[:, 0],
#             wfs_command_data[:, 1],
#             where="post",
#             linestyle="--",
#             color="#6B66EC",
#             label="Scaled WFS wfs_command",
#         )
#         ax1.set_ylabel("WFS")
#         ax2.plot(w_data[:, 0], w_data[:, 1],
#                  color="#006400", label="Scaled width")
#         ax2.set_ylabel("W")
#     else:
#         ax1.step(
#             wfs_data[:, 0],
#             wfs_data[:, 1],
#             where="post",
#             color="#000080",
#             label="WFS value",
#         )
#         ax1.step(
#             wfs_command_data[:, 0],
#             wfs_command_data[:, 1],
#             where="post",
#             linestyle="--",
#             color="#6B66EC",
#             label="WFS wfs_command",
#         )
#         ax2.plot(w_data[:, 0], w_data[:, 1] * 1000,
#                  color="#006400", label="Width")
#         ax2.set_ylabel("W (mm)")
#         ax1.set_ylabel("WFS (m/min)")
#
#     fig.tight_layout()
#     fig.legend(bbox_to_anchor=(0.94, 0.92))
#     fig.show()
#
#     if save:
#         if scale:
#             fig.savefig(results_dir + f"plots/{source}_{fig_filename}.png")
#         else:
#             fig.savefig(results_dir + f"plots/{source}_{fig_filename}_raw.png")

def plot_calibration(
    bead_idx,
    wfs_command_data,
    wfs_data,
    ts_command_data,
    ts_data,
    w_data,
    fig_filename,
    N
):
    """
    Plot experiment data of specific welded bead

    Args:
        bead_idx (int): index of welded bead
        wfs_data(np.array): wfs data
        wfs_command_data(np.array): wfs wfs_command data
        w_data(np.array): width data
        fig_filename (str): figure file name
        scale (bool): whether to scale data
        save (bool): whether to save data
        N (int): number of samples of data array

    """
    if N is None:
        N = w_data.shape[0]

    fig, axs = plt.subplots(2)
    fig.set_size_inches((10, 6))
    axs[0].set_xlabel("t")
    ax2 = axs[0].twinx()
    axs[1].set_xlabel("t")

    if scale:
        ax2.plot(ts_data[:, 0], ts_data[:, 1],
                 color='#CC5500', label=' Scaled TS')
        ax2.plot(ts_command_data[:, 0], ts_command_data[:, 1],
                 color='#FFA500', linestyle='--', label='Scaled TS command')
        axs[0].step(
            wfs_data[:, 0],
            wfs_data[:, 1],
            where="post",
            color="#000080",
            label="Scaled WFS",
        )
        axs[0].step(
            wfs_command_data[:, 0],
            wfs_command_data[:, 1],
            where="post",
            linestyle="--",
            color="#6B66EC",
            label="Scaled WFS command",
        )
        axs[1].plot(w_data[:, 0], w_data[:, 1],
                    color="#006400")
        axs[0].set_ylabel("WFS")
        ax2.set_ylabel("TS")
        axs[1].set_ylabel("W")
    else:
        ax2.plot(ts_data[:, 0], ts_data[:, 1],
                 color='#CC5500', label='TS')
        ax2.plot(ts_command_data[:, 0], ts_command_data[:, 1],
                 color='#FFA500', linestyle='--', label='TS command')
        axs[0].step(
            wfs_data[:, 0],
            wfs_data[:, 1],
            where="post",
            color="#000080",
            label="WFS",
        )
        axs[0].step(
            wfs_command_data[:, 0],
            wfs_command_data[:, 1],
            where="post",
            linestyle="--",
            color="#6B66EC",
            label="WFS command",
        )
        axs[1].plot(w_data[:, 0], w_data[:, 1],
                    color="#006400")
        axs[0].set_ylabel("WFS (m/min)")
        ax2.set_ylabel("TS (mm/s)")
        axs[1].set_ylabel("W (mm)")

    fig.tight_layout()
    fig.legend(bbox_to_anchor=(0.94, 0.92))

    if end_time is not None:
        axs[0].set_xlim(5.0, end_time)
        axs[0].set_xticks(np.arange(5.0, end_time+0.1, 0.5))
        axs[1].set_xlim(5.0, end_time)
        axs[1].set_xticks(np.arange(5.0, end_time+0.1, 0.5))

    if save:
        if scale:
            fig.savefig(
                results_dir + f"plots/experiment/{source}/calibration_{fig_filename}.{format}")
        else:
            fig.savefig(
                results_dir + f"plots/experiment/{source}/calibration_{fig_filename}_raw.{format}")
        plt.close()
    else:
        fig.show()


def plot_control(
    bead_idx,
    wfs_command_data,
    ts_command_data,
    w_data,
    ref_data,
    fig_filename,
    N
):
    """
    Plot experiment data of specific welded bead

    Args:
        bead_idx (int): index of welded bead
        wfs_data(np.array): wfs data
        wfs_command_data(np.array): wfs wfs_command data
        w_data(np.array): width data
        fig_filename (str): figure file name
        scale (bool): whether to scale data
        save (bool): whether to save data
        N (int): number of samples of data array

    """
    if N is None:
        N = w_data.shape[0]

    fig, axs = plt.subplots(2)
    fig.set_size_inches((10, 6))
    axs[0].set_xlabel("t")
    ax2 = axs[0].twinx()
    axs[1].set_xlabel("t")

    ax2.plot(ts_command_data[:, 0], ts_command_data[:, 1],
             color='#FFA500', label='TS command')
    axs[0].step(
        wfs_command_data[:, 0],
        wfs_command_data[:, 1],
        where="post",
        color="#6B66EC",
        label="WFS command",
    )
    axs[1].plot(w_data[:, 0], w_data[:, 1],
                color="#006400", label='Measured Width')
    axs[1].plot(ref_data[:, 0], ref_data[:, 1], color="#00AA00",
                linestyle='--', label='Reference Width')
    axs[0].set_ylabel("WFS (m/min)")
    ax2.set_ylabel("TS (mm/s)")
    axs[1].set_ylabel("W (mm)")

    fig.tight_layout()
    fig.legend(bbox_to_anchor=(0.94, 0.98))

    if save:
        fig.savefig(
            results_dir + f"plots/experiment/control/control_{fig_filename}.{format}")
        plt.close()
    else:
        fig.show()


N = None  # Horizon plotted
end_time = 16
scale = False
save = True
format = "eps"
source = "control"
experiment_matrix = pd.read_excel(
    data_dir + f'experiment/{source}/experiment_matrix.xlsx')
ts_min = experiment_matrix['TS (mm/s)'].min()
ts_max = experiment_matrix['TS (mm/s)'].max()
data_path = data_dir + f"experiment/{source}/"
if source == "simulation":
    input_train, output_train, input_test, output_test = load_train_data(
        data_dir + 'simulation/')
    fig_filename = "train"
    plot_simulation(
        input_train,
        output_train,
        fig_filename,
        N
    )

if source == "calibration":
    bead_idxs = list(range(1, 16))
    for bead_idx in bead_idxs:
        bead_filename = data_path + f"series/bead{bead_idx}"
        wfs_command_data = pd.read_csv(
            bead_filename + "_wfs_command.csv").to_numpy()
        wfs_data = pd.read_csv(bead_filename + "_wfs.csv").to_numpy()
        w_data = pd.read_csv(bead_filename + "_w.csv").to_numpy()
        ts_data = pd.read_csv(bead_filename + "_ts.csv").to_numpy()
        ts_command_data = pd.read_csv(
            bead_filename + "_ts_command.csv").to_numpy()
        fig_filename = f"bead{bead_idx}"
        if scale:
            wfs_data[:, 1:] = normalize_data(wfs_data[:, 1:])
            wfs_command_data[:, 1:] = normalize_data(
                wfs_command_data[:, 1:])
            w_data[:, 1:] = normalize_data(w_data[:, 1:])
            ts_command_data[:, 1:] = normalize_data(
                ts_command_data[:, 1:], ts_min, ts_max)
            ts_data[:, 1:] = normalize_data(ts_data[:, 1:], ts_min, ts_max)

        plot_calibration(
            bead_idx,
            wfs_command_data,
            wfs_data,
            ts_command_data,
            ts_data,
            w_data,
            fig_filename,
            N
        )


if source == "control":
    bead_idxs = list(range(1, 3))
    for bead_idx in bead_idxs:
        bead_filename = data_path + f"series/bead{bead_idx}"
        wfs_command_data = pd.read_csv(
            bead_filename + "_wfs_command.csv").to_numpy()
        w_data = pd.read_csv(bead_filename + "_w.csv").to_numpy()
        ts_command_data = pd.read_csv(
            bead_filename + "_ts_command.csv").to_numpy()
        ref_data = np.zeros(w_data.shape)
        ref_data[:, 0] = w_data[:, 0]
        ref_data[:, 1] = 9.0
        fig_filename = f"bead{bead_idx}"
        plot_control(
            bead_idx,
            wfs_command_data,
            ts_command_data,
            w_data,
            ref_data,
            fig_filename,
            N
        )
