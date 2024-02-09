import rosbag
import numpy as np
import pandas as pd

# Bag pathsd
data_dir = "database/experiment/%s"
bag_dir = data_dir % "bags_width/%s"
series_path = data_dir % "series/%s"

# Input and Output topics
topics = [
    "/xiris/bead/filtered",
    "/fronius_remote_command",
    "/powersource_state",
    "/arc_state",
]


# Functions
def get_arc_times(arc_time, arc_state):
    """
    Calculate arc on and arc off times

    Args:
        arc_time (np.array): A list of arc times.
        arc_state (np.array): A list of arc states.

    Returns:
        arcon_time (float): the arc on time
        arcoff_time (float): the arc off time
    """
    arcon_idx = np.where(np.diff(arc_state.astype(int)) == 1)[0][0]
    arcon_time = arc_time[arcon_idx]
    arcoff_idx = np.where(np.diff(arc_state.astype(int)) == -1)[0][0]
    arcoff_time = arc_time[arcoff_idx]
    return arcon_time, arcoff_time


def slice_data(
    power_time, power_data, wfs_time, wfs_data, w_time, w_data, arc_times
):
    """
    Slice time series between arc on and arc off times

    Args:
        power_time (np.array): A list of power time (in seconds).
        power_time (np.array): A list of power values.
        wfs_time (np.array): A list of wfs time (in seconds).
        wfs_time (np.array): A list of wfs values.
        w_time (np.array): A list of w time (in seconds).
        w_time (np.array): A list of w values.
        arc_times (np.array): A list of arc times
    Returns:
        power_time (np.array): A list of power time (in seconds) sliced between arc on and arc off times.
        power_time (np.array): A list of power values sliced between arc on and arc off times.
        wfs_time (np.array): A list of wfs time (in seconds) sliced between arc on and arc off times.
        wfs_time (np.array): A list of wfs values sliced between arc on and arc off times.
        w_time (np.array): A list of w time (in seconds) sliced between arc on and arc off times.
        w_time (np.array): A list of w values sliced between arc on and arc off times.
    """
    arcon_time, arcoff_time = arc_times

    power_on_idx = np.where(
        (power_time > arcon_time) & (power_time < arcoff_time)
    )
    power_time = power_time[power_on_idx]
    power_data = power_data[power_on_idx]

    wfs_on_idx = np.where((wfs_time > arcon_time) & (wfs_time < arcoff_time))
    wfs_time = wfs_time[wfs_on_idx]
    wfs_data = wfs_data[wfs_on_idx]

    w_on_idx = np.where((w_time > arcon_time) & (w_time < arcoff_time))
    w_time = w_time[w_on_idx]
    w_data = w_data[w_on_idx]

    return power_time, power_data, wfs_time, wfs_data, w_time, w_data


def pow2wfs(power_data):
    """
    Covert power to wfs

    Args:
        power_data (float): power command

    Returns:
        float: wfs command
    """
    return (power_data * 9 / 100) + 1.5


def filter_start(power_time, power_data, wfs_time, wfs_data, w_time, w_data):
    """
    Remove initial seconds of noide from data

    Args:
        power_time (np.array): A list of power time (in seconds).
        power_time (np.array): A list of power values.
        wfs_time (np.array): A list of wfs time (in seconds).
        wfs_time (np.array): A list of wfs values.
        w_time (np.array): A list of w time (in seconds).
        w_time (np.array): A list of w values.
        arc_times (np.array): A list of arc times
    Returns:
        power_time (np.array): A list of power time (in seconds) without initial noise.
        power_time (np.array): A list of power values without initial noise.
        wfs_time (np.array): A list of wfs time (in seconds) without initial noise.
        wfs_time (np.array): A list of wfs values without initial noise.
        w_time (np.array): A list of w time (in seconds) without initial noise.
        w_time (np.array): A list of w values without initial noise.
    """
    start_time = 4.0

    w_start = np.where(w_time >= start_time)[0][0]
    w_time = w_time[w_start:]
    w_data = w_data[w_start:]

    # Remove initial outliers of wfs
    wfs_start = np.where(wfs_time >= start_time)[0][0]
    wfs_time = wfs_time[wfs_start:]
    wfs_data = wfs_data[wfs_start:]

    # Remove initial outliers of power command
    power_start = np.where(power_time >= start_time)[0][0]
    power_time = power_time[power_start - 1 :]
    power_data = power_data[power_start - 1 :]
    power_time[0] = start_time
    return power_time, power_data, wfs_time, wfs_data, w_time, w_data


bead_idxs = list(range(1, 2))
for bead_idx in bead_idxs:
    bead_file_path = bag_dir % f"bead{bead_idx}_width.bag"
    # Input and output data
    w_time = []
    w_data = []

    power_time = []
    power_data = []

    wfs_time = []
    wfs_data = []

    arc_time = []
    arc_state = []

    # Read rosbag
    with rosbag.Bag(bead_file_path, "r") as bag:
        # Iterate through the messages in the bag
        for topic, msg, t in bag.read_messages(topics=topics):
            t = t.to_sec()
            if topic == topics[0]:
                data = msg.data
                w_time.append(t)
                w_data.append(data)
            elif topic == topics[1]:
                data = msg.data
                power_time.append(t)
                power_data.append(data)
            elif topic == topics[2]:
                data = msg.wire_feed_speed
                wfs_time.append(t)
                wfs_data.append(data)
            elif topic == topics[3]:
                data = msg.data
                arc_time.append(t)
                arc_state.append(data)

    # Format to np array
    arc_time = np.array(arc_time).ravel()
    power_time = np.array(power_time).ravel()
    wfs_time = np.array(wfs_time).ravel()
    w_time = np.array(w_time).ravel()

    power_data = np.array(power_data).ravel()
    wfs_data = np.array(wfs_data).ravel()
    w_data = np.array(w_data).ravel()
    arc_state = np.array(arc_state).ravel()

    # Remove offset of t0
    power_time = power_time - arc_time[0]
    wfs_time = wfs_time - arc_time[0]
    w_time = w_time - arc_time[0]
    arc_time = arc_time - arc_time[0]

    # Get arc on and off
    arc_times = get_arc_times(arc_time, arc_state)

    # Remove arc_offs
    (power_time, power_data, wfs_time, wfs_data, w_time, w_data) = slice_data(
        power_time, power_data, wfs_time, wfs_data, w_time, w_data, arc_times
    )
    arc_time = arc_time - arc_times[0]
    power_time = power_time - arc_times[0]
    wfs_time = wfs_time - arc_times[0]
    w_time = w_time - arc_times[0]
    power_time = np.concatenate([power_time, w_time[-1:]])
    power_data = np.concatenate([power_data, power_data[-1:]])

    # Remove initial dynamics
    (
        power_time,
        power_data,
        wfs_time,
        wfs_data,
        w_time,
        w_data,
    ) = filter_start(
        power_time, power_data, wfs_time, wfs_data, w_time, w_data
    )

    # save data
    wfs_df = pd.DataFrame({"t": wfs_time, "wfs_state": wfs_data})
    wfs_df.to_csv(series_path % f"bead{bead_idx}_wfs.csv", index=False)

    command_df = pd.DataFrame({"t": power_time, "wfs_command": power_data})
    command_df.to_csv(series_path % f"bead{bead_idx}_command.csv", index=False)

    w_df = pd.DataFrame({"t": w_time, "w": w_data})
    w_df.to_csv(series_path % f"bead{bead_idx}_w.csv", index=False)
