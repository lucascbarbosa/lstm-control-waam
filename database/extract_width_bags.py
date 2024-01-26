import rosbag
import numpy as np
from cv_bridge import CvBridge 
import cv2

# Bag paths
bag_file_path = "database/experiment/bags_width/bead1_width.bag"

# Input and Output topics
topics = ["/xiris/bead/filtered", "/fronius_remote_command", "/arc_state"]


# Functions
def get_arc_times(arc_time, arc_state):
    arcon_idx = np.where(np.diff(arc_state.astype(int)) == 1)[0][0]
    arcon_time = arc_time[arcon_idx]
    arcoff_idx = np.where(np.diff(arc_state.astype(int)) == -1)[0][0]
    arcoff_time = arc_time[arcoff_idx]
    return arcon_time, arcoff_time

def slice_data(wfs_time, wfs_data, w_time, w_data, arc_times):
    arcon_time, arcoff_time = arc_times

    wfs_on_idx = np.where((wfs_time > arcon_time) & ( wfs_time < arcoff_time))
    wfs_time = wfs_time[wfs_on_idx]
    wfs_data = wfs_data[wfs_on_idx]
    
    w_on_idx = np.where((w_time > arcon_time) & ( w_time < arcoff_time))
    w_time = w_time[w_on_idx]
    w_data = w_data[w_on_idx]

    return wfs_time, wfs_data, w_time, w_data

# Input and output data
w_time = []
w_data = []

wfs_time = []
wfs_data = []

arc_time = []
arc_state = []

# Read rosbag
with rosbag.Bag(bag_file_path, 'r') as bag:
    # Iterate through the messages in the bag
    for topic, msg, t in bag.read_messages(topics=topics):
        t = t.to_sec()
        data = msg.data
        if topic == topics[0]:
            w_time.append(t)
            w_data.append(data)
        elif topic == topics[1]:
            wfs_time.append(t)
            wfs_data.append(data)
        elif topic == topics[2]:
            arc_time.append(t)
            arc_state.append(data)

# Format
wfs_time = np.array(wfs_time)
wfs_time = wfs_time - wfs_time[0]
w_time = np.array(w_time)
w_time = w_time - w_time[0]
arc_time = np.array(arc_time)
arc_time = arc_time - arc_time[0]

wfs_data = np.array(wfs_data)
w_data = np.array(w_data)
arc_state = np.array(arc_state)

# # Get arc on and off
arc_times = get_arc_times(arc_time, arc_state)

# # Remove arc_offs
# wfs_time, wfs_data, w_time, w_data = slice_data(wfs_time, wfs_data, w_time, w_data, arc_times)

# import matplotlib.pyplot as plt

# fig, ax1 = plt.subplots()

# ax1.step(wfs_time, wfs_data, color='k', label='wfs')
# ax1.set_xlabel('t')
# ax1.set_ylabel('WFS')

# ax2 = ax1.twinx()
# ax2.plot(w_time, w_data, color='r', label='w')
# ax2.set_ylabel('W')

# fig.legend()
# plt.tight_layout()
# plt.show()