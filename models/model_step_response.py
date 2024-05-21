import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
from models.process_data import load_train_data
from scipy.signal import find_peaks
import control

# Data paths
data_dir = "database/"
results_dir = "results/"

# Functions


def update_hist(current_hist, new_states):
    new_hist = current_hist.copy()
    len_new = new_states.shape[0]
    new_hist[:-len_new, :] = current_hist[len_new:, :]
    new_hist[-len_new:, :] = new_states
    return new_hist


def build_sequence():
    u = u_hist.ravel()
    y = y_hist.ravel()
    P = u_hist.shape[0]
    Q = y_hist.shape[0]
    sequence = np.hstack((u, y)).reshape(
        (1, P * process_inputs + Q * process_outputs, 1))
    return sequence


def compute_ss(output_data):
    peaks, _ = find_peaks(output_data)
    if len(peaks) > 1:
        time_constant = time[peaks[1]] - time[peaks[0]]
        overshoot = (output_data[peaks[0]] -
                     output_data[-1]) / output_data[-1]
        zeta = np.abs(np.log(overshoot)) / \
            np.sqrt(np.pi**2 + np.log(overshoot)**2)
        omega_n = 4 / (zeta * time_constant)
        print(f"Zeta: {zeta} W_n: {omega_n} \n")

        numerator = [0, 0, omega_n**2]
        denominator = [1, 2*zeta*omega_n, omega_n**2]

        G_continuous = control.TransferFunction(numerator, denominator)
        G_discrete = control.sample_system(
            G_continuous, T, method='tustin')
        ss_discrete = control.tf2ss(G_discrete)

        return ss_discrete.A, ss_discrete.B, ss_discrete.C, ss_discrete. D


def plot_test(
    time,
    wfs_command_data,
    ts_command,
    w_data,
    fig_filename=None,
    N=None
):
    """
    Plot experiment data of specific welded bead.

    Args:
        ts_command (np.array): ts_command
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
    fig.set_size_inches((10, 4))
    ax.set_xlabel("t")
    ax2 = ax.twinx()
    ax2.set_xlabel("t")
    plt.title(f"TS: {ts_command} (mm/s)")
    ax.step(
        time,
        wfs_command_data,
        where="post",
        color="b",
        linestyle='--',
        label="WFS command",
    )
    ax2.plot(time,
             w_data,
             color="#006400",
             label="Width"
             )
    ax.set_ylabel("WFS (mm/min)")
    ax2.set_ylabel("W (mm)")

    plt.tight_layout()

    if save:
        plt.savefig(
            results_dir + f"plots/{source}/calibration/{source}_calibration__ts_{ts_command}__step_response.{format}")
    plt.show()


source = "experiment"
save = True
format = "eps"
best_model_id = 16
if source == "experiment":
    # Load data
    (input_train,
     output_train,
     _,
     _) = load_train_data(data_dir + "experiment/calibration/")

elif source == "simulation":
    list_input_train = []
    list_input_test = []
    list_output_train = []
    list_output_test = []
    for ts in [4, 8, 12, 16, 20]:
        input_train, output_train, input_test, output_test = load_train_data(
            data_dir + f"simulation/TS {ts}/"
        )
        list_input_train.append(input_train)
        list_input_test.append(input_test)
        list_output_train.append(output_train)
        list_output_test.append(output_test)

    input_train = np.concatenate(list_input_train)
    input_test = np.concatenate(list_input_test)
    output_train = np.concatenate(list_output_train)
    output_test = np.concatenate(list_output_test)

input_train = input_train[:, 1:]
output_train = output_train[:, 1:]

u_min = input_train.min(axis=0)
u_max = input_train.max(axis=0)
y_min = output_train.min(axis=0)
y_max = output_train.max(axis=0)

process_inputs = input_train.shape[1]
process_outputs = output_train.shape[1]

# Model parameters
metrics = pd.read_csv(results_dir + f"models/{source}/hp_metrics.csv")
best_model_filename = f"run_{best_model_id:03d}.keras"
best_params = metrics[metrics["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = 3

# Load model
model = load_model(
    results_dir + f"models/{source}/best/{best_model_filename}"
)

opt = Adam(learning_rate=best_params["lr"])
model.compile(optimizer=opt, loss=mean_squared_error)

# Create steps
N = 100
T = 0.2
time = np.arange(0.0, N*T, T)
wfs_steps = np.arange(0.0, 1.01, 0.1)
ts_steps = np.arange(0.0, 1.1, 0.25)
for ts_step in ts_steps:
    input_data = np.zeros((N, process_inputs))
    for i in range(len(wfs_steps)):
        wfs_step = wfs_steps[i]
        input_data[i * int(N/len(wfs_steps)):(i+1) *
                   int(N/len(wfs_steps)), :] = [wfs_step, ts_step]

    # Historic data
    u_hist = np.zeros((P, process_inputs))
    y_hist = np.zeros((Q, process_outputs))
    output_data = []
    for i in range(input_data.shape[0]):
        u = input_data[i].reshape((1, 2))
        u_hist = update_hist(u_hist, u)
        input_seq = build_sequence()
        input_tensor = tensorflow.convert_to_tensor(
            input_seq, dtype=tensorflow.float32)
        y = model(input_tensor).numpy()
        y_hist = update_hist(y_hist, y)
        y_descaled = y[0, 0] * (y_max - y_min) + y_min
        output_data.append(y_descaled[0])

    # Rescale data
    input_data = input_data * (u_max - u_min) + u_min
    output_data = np.array(output_data)
    print(f"TS: {ts_step}")

    # Plot
    plot_test(time, input_data[:, 0], int(input_data[0, 1]), output_data)
