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
        self.arc_idxs = [10, 500]
        self.pub_width = rospy.Publisher(
            "xiris/bead/filtered", Float32, queue_size=10)
        self.fs = 10
        self.rate = rospy.Rate(self.fs)

        # Define model
        numerator = [0, 0, 0.8]
        denominator = [0.2, 1.2, 1]
        self.lag = 1.25
        self.T = 1/self.fs
        G_continuous = control.TransferFunction(numerator, denominator)
        self.G_discrete = control.sample_system(
            G_continuous, self.T, method='tustin')

        # Arc state
        self.arc_state = False

        # Current values
        self.time = 0.0
        self.u = 0.0
        self.y = 0.0

        # Data arrays
        self.time_array = [self.time]
        self.u_array = [self.u]
        self.y_array = []

    def callback(self, data):
        self.u = data.data
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
        num_zeros = int(self.lag*self.fs) - len(self.u_array)
        u = np.pad(self.u_array, (max(0, num_zeros), 0), 'constant')[
            :len(self.time_array)]
        y = control.forced_response(
            self.G_discrete, T=self.time_array, U=u)[1][-1]
        self.y_array.append(y)
        rospy.loginfo("Sending y: %s", y)

    def set_arcstate(self, t):
        arc_state = t > self.arc_idxs[0] and t < self.arc_idxs[1]
        self.pub_arc.publish(arc_state)
        rospy.loginfo("Sending arc_state: %s", arc_state)
        if self.arc_state and not arc_state:
            rospy.signal_shutdown("Shutting down...")
        else:
            self.arc_state = arc_state


cell = Cell()
k = 0
try:
    while not rospy.is_shutdown():
        cell.set_arcstate(k)
        cell.time += cell.T
        cell.time_array.append(np.round(cell.time, 2))
        cell.u_array.append(cell.u)
        cell.predict_output()
        cell.y_array.append(cell.y)
        k += 1
        cell.rate.sleep()
except rospy.ROSInterruptException:
    pass

rospy.spin()
