import numpy as np
import pandas as pd

# Paths
data_dir = "database/experiment/control/"


def generate_w(N, bounds, n_amps, min_diff=3):
    """
    Compute w references.

    Args:
        N (int): number of references
        output_bounds (tuple): lower and upper bounds of width
        n_amps (int): number of possible amplitudes for width
        min_diff (int): number of minimal change in amplitude of width

    Returns:
        np.array: width references
    """
    w_lv, w_uv = bounds
    amps = np.arange(n_amps)
    w_step_signal = np.zeros(N)
    for i in range(N):
        current_step = w_step_signal[i - 1]
        valid_amps = amps[
            np.where(
                (amps >= current_step + min_diff)
                | (amps <= current_step - min_diff)
            )
        ]
        w_step_signal[i] = np.random.choice(valid_amps)

    w_signal = w_lv + (w_uv - w_lv) * w_step_signal / (n_amps - 1)
    return np.round(w_signal, 2).tolist()


# Experiment parameters
step_time = 15.0  # Period between width references steps
traj_length = 340.0  # total length (mm)
x0, y0 = 330.0, 30.0
bead_distance = 20.0  # Distance between consecutives beads
travel_speeds = np.array([8, 12])  # Travel Speed (mm/s)
beads_per_ts = [2, 1]
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

list_references = []
for bead_idx, travel_speed in beads_ts.items():
    exp_time = traj_length / travel_speed  # Total experiment time (s)
    # Length of each reference step (mm)
    step_length = step_time * travel_speed
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
    w_lv = 4  # (mm)
    w_uv = 14  # (mm)
    bounds = (w_lv, w_uv)

    # Build input data
    widths = generate_w(N, bounds, 11, min_diff=2)
    widths = pd.DataFrame(
        {
            "ti (s)": np.round(time_i, 2),
            "tf (s)": np.round(time_f, 2),
            "xi (mm)": traj_xi,
            "yi (mm)": traj_yi,
            "xf (mm)": traj_xf,
            "yf (mm)": traj_yf,
            "TS (mm/s)": travel_speed,
            "W_ref (mm)": widths,
        }
    )

    widths.to_csv(
        data_dir + f"references/bead{bead_idx+1}.csv", index=False)
    widths["bead"] = bead_idx + 1
    list_references.append(widths)

# Build experiment matrix
exp_matrix = pd.concat(list_references, ignore_index=True)
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
        "W_ref (mm)",
        "CTWD (mm)",
        "gas flow (l/min)",
        "DC",
        "AC",
        "pre flow",
        "pos flow",
    ]
]

exp_matrix.to_excel(data_dir + "experiment_matrix.xlsx", index=False)
