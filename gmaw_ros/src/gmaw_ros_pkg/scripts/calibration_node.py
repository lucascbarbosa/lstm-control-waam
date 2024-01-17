import numpy as np
import pandas as pd

import rospy
from std_msgs.msg import Float32, Bool

import time

class Experiment(object):
    def __init__(self, pub_freq, bead_idx):
        # Filepaths
        self.data_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/database/"
        self.results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"

        # Load input data
        self.bead_idx = bead_idx
        self.command_data = pd.read_csv(self.data_dir + f"experiment/commands/bead{bead_idx}.csv").to_numpy()
        
        # Output data
        self.output_data = []

        # ROSPY Parameters
        rospy.init_node("mpc_node", anonymous=True)
        rospy.Subscriber("arc_state", Bool, self.callback_arc)
        self.arc_state = False
        rospy.Subscriber("xiris/bead/filtered", Float32, self.callback_width)
        self.pub = rospy.Publisher("fronius_remote_command", Float32, queue_size=10)
        self.pub_freq = pub_freq  # sampling frequency of width data
        self.step_time = 1 / self.pub_freq
        self.rate = rospy.Rate(self.pub_freq)
    
    # Callback method
    def callback_arc(self, data):
        if not self.arc_state and bool(data.data):
            self.arcon_time = time.time()
        elif self.arc_state and not bool(data.data):
            self.export_output()
            rospy.signal_shutdown("Shutting down")
        self.arc_state = bool(data.data)

    def callback_width(self, data):
        current_time = time.time() - start_time
        y_row = data.data * int(self.arc_state)
        rospy.loginfo("Received output w: %f", y_row)
        self.output_data.append({'t': current_time, 'w': y_row})

    def publish_command(self):
        if self.arc_state:
            current_time = np.round(time.time() - self.arcon_time, 2)
            idx = np.where(self.command_data[:, 0] == current_time)[0]
            if len(idx) > 0:
                idx = idx[0]
                f = self.command_data[idx, -1]
                self.pub.publish(f)
                rospy.loginfo("Sending command wfs: %f", f)

    def export_output(self):
        self.output_data = pd.DataFrame(self.output_data)
        self.output_data = self.output_data[self.output_data['w'] > 0]
        self.output_data.to_csv(self.data_dir + f"experiment/series/output_{self.bead_idx}.csv", index=False) 

pub_freq = 10
bead_idx = 1
exp = Experiment(pub_freq, bead_idx)
start_time = time.time()
while not rospy.is_shutdown():
    if exp.arc_state:
        exp.rate.sleep()
        exp.publish_command()

rospy.spin()
