import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

# Paths
data_dir = "database/experiment/"

# Functions


def generate_wfs(N, input_bounds, n_amps, min_diff=3):
    """
    Compute wfs commands.

    Args:
        N (int): number of commands
        input_bounds (tuple): lower and upper bounds of command
        n_amps (int): number of possible amplitudes for command
        min_diff (int): number of minimal change in amplitude of command

    Returns:
        np.array: wfs commands
    """
    f_lv, f_uv = input_bounds
    amps = np.arange(n_amps)
    f_step_signal = np.zeros(
        N,
    )
    f_step_signal[0] = amps[len(amps) // 2]
    for i in range(1, N):
        current_step = f_step_signal[i - 1]
        valid_amps = amps[
            np.where(
                (amps >= current_step + min_diff)
                | (amps <= current_step - min_diff)
            )
        ]
        f_step_signal[i] = np.random.choice(valid_amps)

    f_signal = f_lv + (f_uv - f_lv) * f_step_signal / (n_amps - 1)
    return np.round(f_signal, 2).tolist()


# Experiment parameters
step_time = 5.0  # Period between wfs steps
traj_length = 340.0  # total length (mm)
x0, y0 = 30.0, 30.0
bead_distance = 20.0  # Distance between consecutives beads
travel_speeds = np.arange(4, 21, 4).tolist()  # Travel Speed (mm/s)
beads_per_ts = [1, 2, 3, 4, 5]
# pats_per_ts = [17, 9, 6, 5, 4]
beads_ts = {}  # Dict of TS of each bead
bead_idx = 0
for i in range(len(travel_speeds)):
    n = beads_per_ts[i]
    ts = travel_speeds[i]
    for j in range(n):
        beads_ts[bead_idx] = ts
        bead_idx += 1
num_beads = sum(beads_ts)
beads = list(range(num_beads))
list_commands = []
for bead_idx, travel_speed in beads_ts.items():
    exp_time = traj_length / travel_speed  # Total experiment time (s)
    step_length = step_time * travel_speed  # Length of each wfs step (mm)
    # Generate time vectors
    time = np.concatenate(
        [np.arange(0, exp_time, step_time).tolist(), np.array([exp_time])]
    )

    time_i = time[:-1]
    time_f = time[1:]

    # Generate trajectory vectors
    trajectory = np.concatenate(
        [np.arange(0, traj_length, step_length), np.array([traj_length])]
    )
    traj_xi = np.ones(trajectory[:-1].shape) * bead_distance * bead_idx + x0
    traj_xf = np.ones(trajectory[1:].shape) * bead_distance * bead_idx + x0
    traj_yi = trajectory[:-1] + y0
    traj_yf = trajectory[1:] + y0

    # Dataset size
    n_inputs = 1
    n_outputs = 1
    N = len(time_i)

    # Input bounds
    f_lv = 5.1  # 40% (m/min)
    f_uv = 8.7  # 80% (m/min)
    input_bounds = (f_lv, f_uv)

    # Build input data
    commands = generate_wfs(N, input_bounds, 11, min_diff=4)
    commands = pd.DataFrame(
        {
            "ti (s)": np.round(time_i, 2),
            "tf (s)": np.round(time_f, 2),
            "xi (mm)": traj_xi,
            "yi (mm)": traj_yi,
            "xf (mm)": traj_xf,
            "yf (mm)": traj_yf,
            "TS (mm/s)": travel_speed,
            "WFS (m/min)": commands,
        }
    )

    commands.to_csv(data_dir + f"commands/bead{bead_idx+1}.csv", index=False)
    commands["bead"] = bead_idx + 1
    list_commands.append(commands)

# Build experiment matrix
exp_matrix = pd.concat(list_commands, ignore_index=True)
exp_matrix["CTWD (mm)"] = 15
exp_matrix["gas flow (l/min)"] = 15
exp_matrix["AC"] = 0
exp_matrix["DC"] = 0
exp_matrix["pre flow"] = 2000
exp_matrix["pos flow"] = 2000
exp_matrix = exp_matrix[
    [
        "bead",
        "ti (s)",
        "tf (s)",
        "xi (mm)",
        "xf (mm)",
        "yi (mm)",
        "yf (mm)",
        "TS (mm/s)",
        "WFS (m/min)",
        "CTWD (mm)",
        "gas flow (l/min)",
        "DC",
        "AC",
        "pre flow",
        "pos flow",
    ]
]

exp_matrix.to_excel(data_dir + "experiment_matrix.xlsx", index=False)
