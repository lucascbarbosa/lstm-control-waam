import pandas as pd
import numpy as np
from python.process_data import (
    load_simulation,
    load_experiment,
    standardize_data,
    normalize_data,
)
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data_dir = "database/"
results_dir = "results/"
inputs_train, outputs_train, inputs_test, outputs_test = load_simulation(
    data_dir + "simulation/"
)
input_train, output_train, input_test, output_test = load_experiment(
    data_dir + "experiment/", 1, 2
)


def plot_data(
    N,
    data,
    data_label,
    fig_filename,
    var_type,
    source="sim",
    scale=False,
    save=False,
):
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

    if source == "experiment":
        fig = plt.figure(figsize=(12, 6))
        fig.suptitle(fig_title)
        plt.title(r"$%s$" % data_label)
        plt.xlabel(r"k")
        if var_type == "u":
            plt.step(range(N), data[:N])
        else:
            plt.plot(range(N), data[:N])

    plt.tight_layout()
    if save:
        if scale:
            fig.savefig(results_dir + f"plots/{source}_{fig_filename}.png")
        else:
            fig.savefig(results_dir + f"plots/{source}_{fig_filename}_raw.png")


N = 500  # Horizon plotted
database_sim = [inputs_train, outputs_train, inputs_test, outputs_test]
database_exp = [input_train, output_train, input_test, output_test]
data_labels_sim = [
    ["f\;(mm/s)", "I_r\;(A)"],
    ["w_e\;(mm)", "h\;(mm)"],
    ["f\;(mm/s)", "I_r\;(A)"],
    ["w_e\;(mm)", "h\;(mm)"],
]
data_labels_sim_scaled = [
    ["f", "I_r"],
    ["w_e", "h"],
    ["f", "I_r"],
    ["w_e", "h"],
]

data_labels_exp = ["f\;(mm/s)", "w_e\;(mm)", "f\;(mm/s)", "w_e\;(mm)"]
data_labels_exp_scaled = ["f", "w_e", "f", "w_e"]

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
scale = True
save = True

if scale:
    data_labels_exp = data_labels_exp_scaled
    data_labels_sim = data_labels_sim_scaled

source = "experiment"
if source == "simulation":
    database = database_sim
    data_labels = data_labels_sim
elif source == "experiment":
    database = database_exp
    data_labels = data_labels_exp

for data, data_label, fig_title, fig_filename, var_type in zip(
    database, data_labels, fig_titles, fig_filenames, var_types
):
    if scale:
        if var_type == "u":
            data = normalize_data(data)
        else:
            data = standardize_data(data)

    plot_data(
        N,
        data,
        data_label,
        fig_filename,
        var_type,
        source=source,
        scale=scale,
        save=save,
    )

plt.show()
