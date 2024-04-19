import rospy
from std_msgs.msg import Float32, Bool, Float64MultiArray
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from functools import partial

import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam


class Cell(object):
    def __init__(self):
        self.data_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/database/experiment_igor/series/"
        self.results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"
        self.input_train, self.output_train, _, _ = self.load_experiment(
            [1, 2, 3, 4, 5, 6], [7])

        # Rospy setup
        rospy.init_node("cell_node", anonymous=True)
        rospy.Subscriber("fronius_remote_command", Float32, self.callback)
        self.pub_arc = rospy.Publisher("arc_state", Bool, queue_size=10)
        self.arc_idxs = [10, 500]
        self.pub_width = rospy.Publisher(
            "xiris/bead/filtered", Float32, queue_size=10)
        fs = 10
        self.rate = rospy.Rate(fs)

        # Arc state
        self.arc_state = False

    def callback(self, data):
        u = data.data
        rospy.loginfo("Received command wfs: %f", u)
        if self.input_scaling == "min-max":
            u_scaled = (u - self.u_min) / (self.u_max - self.u_min)
        if self.input_scaling == "mean-std":
            u_scaled = (u - self.u_mean) / self.u_std
        self.u_hist = self.update_hist(self.u_hist, u_scaled)
        self.control_mpc.append(u)

    def resample_data(self, original_data, original_time, new_time):
        interp_func = interp1d(
            original_time,
            original_data,
            kind="linear",
            fill_value="extrapolate",
        )

        resampled_data = np.zeros((new_time.shape[0], 2))
        resampled_data[:, 0] = new_time
        resampled_data[:, 1] = interp_func(new_time)
        return resampled_data

    def set_arcstate(self, t):
        arc_state = t > self.arc_idxs[0] and t < self.arc_idxs[1]
        self.pub_arc.publish(arc_state)
        rospy.loginfo("Sending arc_state: %s", arc_state)
        if self.arc_state and not arc_state:
            rospy.signal_shutdown("Shutting down...")
        else:
            self.arc_state = arc_state


cell = Cell()
t = 0
try:
    while not rospy.is_shutdown():
        cell.predict_output()
        cell.set_arcstate(t)
        t += 1
        cell.rate.sleep()
except rospy.ROSInterruptException:
    pass

rospy.spin()
