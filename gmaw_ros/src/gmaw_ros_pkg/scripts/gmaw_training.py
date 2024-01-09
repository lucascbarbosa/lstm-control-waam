import numpy as np
import pandas as pd

import rospy
from std_msgs.msg import Float32, Bool

import time

class Experiment(object):
    def __init__(self, pub_freq):
        # Filepaths
        self.data_dir = f"/home/lbarbosa/Documents/Github/lstm-control-waam/database/"
        self.results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"

        # Load input data
        self.input_train = pd.read_csv(self.data_dir + "experiment/inputs_train.csv").to_numpy()
        self.input_test = pd.read_csv(self.data_dir + "experiment/inputs_test.csv").to_numpy()

        # Output data
        self.output_train = self.input_train.shape
        self.output_test = self.input_test.shape

        self.input_scaling = "min-max"
        self.output_scaling = "min-max"

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
        self.arc_state = bool(data.data)

    def callback_width(self, data):
        rospy.loginfo("Received output w: %f", data.data)
        y_row = data.data
        t = time.time()
        self.y.append([t-start_time, y_row])
        if self.input_scaling == 'min-max':
            y_row_scaled = (y_row - self.y_min) / (self.y_max - self.y_min)
        elif self.input_scaling == 'mean-std':
            y_row_scaled = (y_row - self.y_mean) / self.y_std
        self.y.append(y_row_scaled)

start_time = time.time()
exp_time = 0
pub_freq = 10
exp = Experiment(pub_freq)
while not rospy.is_shutdown():
    if exp.arc_state:
        exp.rate.sleep()
        exp_time = exp.step_time
        
rospy.spin()

