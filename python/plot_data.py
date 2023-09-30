import pandas as pd
import numpy as np
from python.process_data import load_data, standardize_data, normalize_data
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data_dir = "database/"
results_dir = "results/"
# inputs_train, outputs_train, inputs_test, outputs_test = load_data(data_dir)


def plot_data(
    N,
    data,
    data_label,
    fig_filename,
    var_type,
    fig,
    axs,
    scale=False,
    save=False,
):
    axs[0].set_title(r"$%s$" % data_label[0])

    axs[1].set_xlabel(r"k")
    axs[1].set_title(r"$%s$" % data_label[1])
    if var_type == "u":
        axs[0].step(range(N), data[:N, 0])
        axs[1].step(range(N), data[:N, 1])
    else:
        axs[0].plot(range(N), data[:N, 0])
        axs[1].plot(range(N), data[:N, 1])

    if save:
        fig.savefig(results_dir + f"plots/{fig_filename}.png")
    plt.tight_layout()


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
scale = True
save = True
var_types = ["u", "y", "u", "y"]

for data, data_label, fig_title, fig_filename, var_type in zip(
    database, data_labels, fig_titles, fig_filenames, var_types
):
    fig, axs = plt.subplots(2, 1)
    fig.set_size_inches(12, 6)
    fig.suptitle(fig_title)
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
        fig,
        axs,
        scale=scale,
        save=save,
    )

plt.show()

# N = 200
# fig, axs = plt.subplots(2, 1)
# fig.set_size_inches(12, 6)
# plot_data(N, outputs_train, ["we", "h"], None, "y", fig, axs)
# plot_data(N, outputs_gmaw, ["we", "h"], None, "y", fig, axs)
# axs[0].legend(["matlab", "python"])
# axs[1].legend(["matlab", "python"])
# plt.show()
