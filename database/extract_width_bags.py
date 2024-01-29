import rosbag
import numpy as np
import pandas as pd

# Bag pathsd
data_dir = "database/experiment/%s"
bag_dir = data_dir % "bags_width/%s"
series_path = data_dir % "series/%s"

# Input and Output topics
topics = ["/xiris/bead/filtered", 
          "/fronius_remote_command", 
          "/powersource_state", 
          "/arc_state"]

# Functions
def get_arc_times(arc_time, arc_state):
    arcon_idx = np.where(np.diff(arc_state.astype(int)) == 1)[0][0]
    arcon_time = arc_time[arcon_idx]
    arcoff_idx = np.where(np.diff(arc_state.astype(int)) == -1)[0][0]
    arcoff_time = arc_time[arcoff_idx]
    return arcon_time, arcoff_time

def slice_data(power_time, power_data, wfs_time, wfs_data, w_time, w_data, arc_times):
    arcon_time, arcoff_time = arc_times

    power_on_idx = np.where((power_time > arcon_time) & ( power_time < arcoff_time))
    power_time = power_time[power_on_idx]
    power_data = power_data[power_on_idx]
    
    wfs_on_idx = np.where((wfs_time > arcon_time) & ( wfs_time < arcoff_time))
    wfs_time = wfs_time[wfs_on_idx]
    wfs_data = wfs_data[wfs_on_idx]

    w_on_idx = np.where((w_time > arcon_time) & ( w_time < arcoff_time))
    w_time = w_time[w_on_idx]
    w_data = w_data[w_on_idx]

    return power_time, power_data, wfs_time, wfs_data, w_time, w_data

def pow2wfs(power_data):
    return (power_data*9/100) + 1.5


bead_idxs = list(range(1,2))
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
    with rosbag.Bag(bead_file_path, 'r') as bag:
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
    power_time, power_data, wfs_time, wfs_data, w_time, w_data = slice_data(power_time, 
                                                        power_data, 
                                                        wfs_time, 
                                                        wfs_data, 
                                                        w_time, 
                                                        w_data, 
                                                        arc_times)
    arc_time = arc_time - arc_times[0]
    power_time = power_time - arc_times[0]
    wfs_time = wfs_time - arc_times[0]
    w_time = w_time - arc_times[0]
    power_time = np.concatenate([power_time, w_time[-1:]])
    power_data = np.concatenate([power_data, power_data[-1:]])

    # Remove initial outliers of wfs
    wfs_data[:np.where(wfs_data > wfs_data.mean())[0][0]] = wfs_data.mean()
    
    # save data
    wfs_df = pd.DataFrame({'t': wfs_time, 'wfs_state': wfs_data})
    wfs_df.to_csv(series_path % f'bead{bead_idx}_wfs.csv', index=False)
    
    command_df = pd.DataFrame({'t': power_time, 'wfs_command': power_data})
    command_df.to_csv(series_path % f'bead{bead_idx}_command.csv', index=False)
    
    w_df = pd.DataFrame({'t': w_time, 'w': w_data})
    w_df.to_csv(series_path % f'bead{bead_idx}_w.csv', index=False)
