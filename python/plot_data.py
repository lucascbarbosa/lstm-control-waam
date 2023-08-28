import pandas as pd
import numpy as np
from python.process_data import (
    load_data,
    standardize_data,
    normalize_data,
    sequence_data,
)
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data_dir = "database/"
results_dir = "results/"
inputs_train, outputs_train, inputs_test, outputs_test = load_data(data_dir)


def plot_data(
    N,
    database,
    data_labels,
    fig_titles,
    fig_filenames,
    scale=False,
    save=False,
):
    for data, data_label, fig_title, fig_filename in zip(
        database, data_labels, fig_titles, fig_filenames
    ):
        if scale:
            if fig_title.split(" ")[0] == "Entradas":
                data = normalize_data(data)
            else:
                data = standardize_data(data)

        fig, axs = plt.subplots(2, 1)
        fig.set_size_inches(8, 6)
        axs[0].step(range(N), data[:N, 0])
        axs[0].set_title(r"$%s$" % data_label[0])

        axs[1].step(range(N), data[:N, 1])
        axs[1].set_xlabel(r"k")
        axs[0].set_title(r"$%s$" % data_label[1])

        fig.suptitle(fig_title)
        if save:
            fig.savefig(results_dir + f"{fig_filename}.png")

    plt.show()


N = 200  # Horizon plotted
database = [inputs_train, outputs_train, inputs_test, outputs_test]
data_labels = [["f", "Ir"], ["we", "h"], ["f", "Ir"], ["we", "h"]]
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

plot_data(
    N, database, data_labels, fig_titles, fig_filenames, scale=True, save=True
)
