import pandas as pd
import numpy as np
from python.process_data import (
    load_simulation,
    load_experiment,
    load_experiment_igor,
    load_mpc,
    standardize_data,
    normalize_data,
)
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data_dir = "database/"
results_dir = "results/"

def plot_data(
    data,
    data_label,
    fig_filename,
    var_type,
    source="sim",
    scale=False,
    save=False,
    N=None,
):
    if N == None:
        N = data.shape[0]
    if source == "simulation":
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

    elif source == "experiment":
        fig = plt.figure(figsize=(12, 6))
        fig.suptitle(fig_title)
        plt.title(r"$%s$" % data_label)
        plt.xlabel(r"t")
        if var_type == "u":
            plt.step(data[:N, 0], data[:N, 1])
        else:
            plt.plot(data[:N, 0], data[:N, 1])

    plt.tight_layout()
    if save:
        if scale:
            fig.savefig(results_dir + f"plots/{source}_{fig_filename}.png")
        else:
            fig.savefig(results_dir + f"plots/{source}_{fig_filename}_raw.png")


N = None  # Horizon plotted
source = "experiment"
scale = True
save = True
if source == "simulation":
    inputs_train, outputs_train, inputs_test, outputs_test = load_simulation(data_dir + "simulation/")
    database = [inputs_train, outputs_train, inputs_test, outputs_test]
    data_labels = [
        ["f\;(mm/s)", "I_r\;(A)"],
        ["w_e\;(mm)", "h\;(mm)"],
        ["f\;(mm/s)", "I_r\;(A)"],
        ["w_e\;(mm)", "h\;(mm)"]]
    data_labels_scaled = [
        ["f", "I_r"],
        ["w_e", "h"],
        ["f", "I_r"],
        ["w_e", "h"]]

data_path = data_dir + f"{source}/"
    
if source == "experiment_igor":
    input_train, output_train, input_test, output_test = load_experiment_igor(
        data_path, [1,2,3,4,5,6], [7]
        )
    database = [input_train, output_train, input_test, output_test]
    data_labels = ["f\;(mm/s)", "w_e\;(mm)", "f\;(mm/s)", "w_e\;(mm)"]
    data_labels_scaled = ["f", "w_e", "f", "w_e"]

if source == "experiment":
    input_train, output_train, input_test, output_test = load_experiment(data_path)
    database = [input_train, output_train, input_test, output_test]
    data_labels = ["f\;(mm/s)", "w_e\;(mm)", "f\;(mm/s)", "w_e\;(mm)"]
    data_labels_scaled = ["f", "w_e", "f", "w_e"]

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
        if var_type == "u":
            if source == "simulation":
                data = normalize_data(data)
            elif source == "experiment":
                data[:, 1] = normalize_data(data[:, 1].reshape(-1, 1)).ravel()
        else:
            if source == "simulation":
                data = normalize_data(data)
            elif source == "experiment":
                data[:, 1] = normalize_data(data[:, 1].reshape(-1, 1)).ravel()
    plot_data(
        data,
        data_label,
        fig_filename,
        var_type,
        source=source,
        scale=scale,
        save=save,
        N=N,
    )

plt.show()
