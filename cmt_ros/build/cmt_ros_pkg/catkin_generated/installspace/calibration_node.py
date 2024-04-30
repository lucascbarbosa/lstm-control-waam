import numpy as np
import pandas as pd
import sys
import rospy
from std_msgs.msg import Float32, Bool, Float64MultiArray, MultiArrayDimension
import time


class Experiment(object):
    def __init__(self, pub_freq, bead_idx, reverse_text):
        # Filepaths
        self.data_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/database/"
        self.results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"

        # Load input data
        self.bead_idx = bead_idx
        self.command_data = pd.read_csv(
            self.data_dir +
            f"experiment/calibration/commands/bead{bead_idx}{reverse_text}.csv"
        ).to_numpy()

        # ROSPY Parameters
        rospy.init_node("kr90/mpc_node", anonymous=True)
        rospy.Subscriber("kr90/arc_state", Bool, self.callback_arc)
        self.arc_state = False
        self.pub = rospy.Publisher(
            "fronius_remote_command", Float64MultiArray, queue_size=10)
        self.pub_freq = pub_freq  # sampling frequency of width data
        self.step_time = 1 / self.pub_freq
        self.rate = rospy.Rate(self.pub_freq)

    # Callback method
    def callback_arc(self, data):
        if not self.arc_state and bool(data.data):
            rospy.loginfo("Received arc state: %f", bool(data.data))
            self.arcon_time = time.time()
        elif self.arc_state and not bool(data.data):
            rospy.signal_shutdown("Shutting down")
        self.arc_state = bool(data.data)

    def publish_command(self):
        if self.arc_state:
            current_time = np.round(time.time() - self.arcon_time, 1)
            idx = np.where(self.command_data[:, 0] == current_time)[0]
            if len(idx) > 0:
                idx = idx[0]
                f = self.command_data[idx, -1]
                p = self.wfs2pow(f)
                msg = Float64MultiArray()
                msg.data = [p]
                dim = []
                dim.append(MultiArrayDimension('PwrSrc', 1, 4))
                msg.layout.dim = dim
                self.pub.publish(msg)
                rospy.loginfo("Sending command power: %f", p)

    def wfs2pow(self, f):
        return (f - 1.5)*100/9


pub_freq = 10
args = rospy.myargv(argv=sys.argv)
bead_idx = int(args[1])
if len(args) == 3:
    reverse = args[2] == "-r"
    reverse_text = "_reverse"
else:
    reverse_text = ""
exp = Experiment(pub_freq, bead_idx, reverse_text)
start_time = time.time()
while not rospy.is_shutdown():
    if exp.arc_state:
        exp.publish_command()
        exp.rate.sleep()

rospy.spin()
