import pandas as pd
import numpy as np
from python.process_data import (
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
    return (power_data*9/100) + 1.5

def plot_simulation(
    data,
    data_label,
    fig_filename,
    var_type,
    scale=False,
    save=False,
    N=None,
):
    if N == None:
        N = data.shape[0]

    fig, axs = plt.subplots(2, 1)
    fig.set_size_inches(12, 6)
    fig.suptitle(fig_title)
    for i in range(len(data_label)):
        axs[i].set_title(r"$%s$" % data_label[i])

    axs[1].set_xlabel(r"k")
    if var_type == "u":
        for i in range(data.shape[1]):
            axs[i].step(range(N), data[:N, i])
    else:
        for i in range(data.shape[1]):
            axs[i].plot(range(N), data[:N, i] * 1000)
    
    plt.tight_layout()
    if save:
        if scale:
            fig.savefig(results_dir + f"plots/{source}_{fig_filename}.png")
        else:
            fig.savefig(results_dir + f"plots/{source}_{fig_filename}_raw.png")

def plot_experiment(
        wfs_data,
        command_data,
        w_data,
        fig_filename, 
        save=True,
        scale=True,
        N = None
):
    if N == None:
        N = w_data.shape[0]
    
    fig, ax1 = plt.subplots()
    fig.set_size_inches((10, 6))
    ax1.step(wfs_data[:, 0], 
             wfs_data[:, 1], 
             where='post', 
             color='#000080', 
             label='wfs_state')
    ax1.step(command_data[:, 0], 
             pow2wfs(command_data[:, 1]), 
             where='post', 
             linestyle='--', 
             color='b', 
             label='wfs_command')
    ax1.set_xlabel('t')
    ax1.set_ylabel('WFS (m/min)')

    ax2 = ax1.twinx()
    ax2.plot(w_data[:, 0], w_data[:, 1] * 1000, color='#006400', label='w')
    ax2.set_ylabel('W (mm)')

    fig.tight_layout()
    fig.legend(bbox_to_anchor=(0.95, 0.95))
    fig.show()

    if save:
        if scale:
            fig.savefig(results_dir + f"plots/{source}_{fig_filename}.png")
        else:
            fig.savefig(results_dir + f"plots/{source}_{fig_filename}_raw.png")

N = None  # Horizon plotted
source = "experiment"
scale = False
save = False
data_path = data_dir + f"{source}/" 
if source == "simulation":
    inputs_train, outputs_train, inputs_test, outputs_test = load_train_data(data_dir + "simulation/")
    database = [inputs_train, outputs_train, inputs_test, outputs_test]
    data_labels = [
        ["f\;(mm/min)", "I_r\;(A)"],
        ["w_e\;(mm)", "h\;(mm)"],
        ["f\;(mm/min)", "I_r\;(A)"],
        ["w_e\;(mm)", "h\;(mm)"]]
    data_labels_scaled = [
        ["f", "I_r"],
        ["w_e", "h"],
        ["f", "I_r"],
        ["w_e", "h"]]

    if scale:
        data_labels = data_labels_scaled

    fig_titles = [
        "Entradas de treinamento",
        "Saídas de treinamento",
        "Entradas de teste",
        "Saídas de teste",
    ]
    fig_filenames = [
        "inputs_train",
        "outputs_train",
        "inputs_test",
        "outputs_test",
    ]

    var_types = ["u", "y", "u", "y"]
    for data, data_label, fig_title, fig_filename, var_type in zip(
        database, data_labels, fig_titles, fig_filenames, var_types
    ):
        if scale:
            data = normalize_data(data)

        plot_simulation(
            data,
            data_label,
            fig_filename,
            var_type,
            source=source,
            scale=scale,
            save=save,
            N=N,
        )

if source == "experiment":
    bead_idxs = [1]
    for bead_idx in bead_idxs:
        bead_filename = data_path + f"series/bead{bead_idx}"
        command_data =  pd.read_csv(bead_filename + "_command.csv").to_numpy()
        wfs_data =  pd.read_csv(bead_filename + "_wfs.csv").to_numpy()
        w_data =  pd.read_csv(bead_filename + "_w.csv").to_numpy()
        fig_filename = results_dir + f"plots/experiment_bead{bead_idx}_prediction.png"
        plot_experiment(wfs_data, command_data, w_data, fig_filename, save, scale, N)
