import rospy
from std_msgs.msg import Float32, Bool, Float64MultiArray
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import control


class Cell(object):
    def __init__(self):
        # Rospy setup
        rospy.init_node("cell_node", anonymous=True)
        rospy.Subscriber("fronius_remote_command", Float32, self.callback)
        self.pub_arc = rospy.Publisher("arc_state", Bool, queue_size=10)
        self.pub_ts = rospy.Publisher(
            "kr90/travel_speed", Float32, queue_size=10)
        self.arc_idxs = [10, 2000]
        self.pub_width = rospy.Publisher(
            "xiris/bead/filtered", Float32, queue_size=10)
        self.pub_power = rospy.Publisher(
            "powersource_state", Float32, queue_size=10)

        self.fs = 10
        self.rate = rospy.Rate(self.fs)

        # Define model
        numerator = [0, 0, 0.8]
        denominator = [0.2, 1.2, 1]
        self.T = 1 / self.fs
        G_continuous = control.TransferFunction(numerator, denominator)
        G_discrete = control.sample_system(
            G_continuous, self.T, method='tustin')
        self.ss_discrete = control.tf2ss(G_discrete)

        # Arc state
        self.arc_state = False

        # Current values
        self.time = 0.0
        self.u = 0.0
        self.p = 0.0
        self.x = np.zeros((2, 1))
        self.y = 0.0

    def callback(self, data):
        self.p = data.data
        self.u = self.pow2wfs(self.p)
        rospy.loginfo("Received command wfs: %f", self.u)

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

    def predict_output(self):
        self.x = np.dot(self.ss_discrete.A, self.x) + \
            np.dot(self.ss_discrete.B, self.u)
        self.y = list(np.dot(self.ss_discrete.C, self.x) +
                      np.dot(self.ss_discrete.D, self.u))[0]
        self.pub_width.publish(self.y)
        rospy.loginfo("Sending y: %s", self.y)
        self.pub_power.publish(self.p + np.random.normal())
        rospy.loginfo("Sending power: %s", self.p + np.random.normal())
        self.ts = 10.0 + np.random.normal()
        self.pub_ts.publish(self.ts)
        rospy.loginfo("Sending TS: %s", self.ts)

    def set_arcstate(self, t):
        arc_state = t > self.arc_idxs[0] and t < self.arc_idxs[1]
        self.pub_arc.publish(arc_state)
        rospy.loginfo("Sending arc_state: %s", arc_state)
        if self.arc_state and not arc_state:
            rospy.signal_shutdown("Shutting down...")
        else:
            self.arc_state = arc_state

    def wfs2pow(self, f):
        return np.round((f-1.5)*100/(10.5 - 1.5), 2)

    def pow2wfs(self, p):
        return np.round((p*9/100)+1.5, 3)


cell = Cell()
k = 0
try:
    while not rospy.is_shutdown():
        cell.set_arcstate(k)
        cell.time += cell.T
        cell.predict_output()
        k += 1
        cell.rate.sleep()
except rospy.ROSInterruptException:
    pass

rospy.spin()
