import rospy
from std_msgs.msg import Float64, Bool, Float64MultiArray
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import control
import sys


class Cell(object):
    def __init__(self, ts):

        self.ts = ts

        # Read gain
        with open(results_dir + f'models/tf/ts_{ts}.txt', 'r') as f:
            gain = float(f.read())

        # Rospy setup
        rospy.init_node("cell_node", anonymous=True)
        rospy.Subscriber("fronius_remote_command",
                         Float64MultiArray, self.callback)
        rospy.Subscriber("mpc_state", Bool, self.callback_mpc)
        self.pub_arc = rospy.Publisher("kr90/arc_state", Bool, queue_size=10)
        self.pub_width = rospy.Publisher(
            "xiris/bead/filtered", Float64, queue_size=10)

        self.fs = 10
        self.rate = rospy.Rate(self.fs)

        # Define model
        numerator = [0, 0, gain]
        denominator = [0.2, 1.2, 1]
        self.T = 1 / self.fs
        G_continuous = control.TransferFunction(numerator, denominator)
        G_discrete = control.sample_system(
            G_continuous, self.T, method='tustin')
        self.ss_discrete = control.tf2ss(G_discrete)

        # Arc state
        self.arc_state = False
        # MPC state
        self.mpc_state = False

        # Current values
        self.time = 0.0
        self.u = 0.0
        self.p = 0.0
        self.x = np.zeros((2, 1))
        self.y = 0.0

    def callback(self, data):
        self.p = data.data[0]
        self.u = self.pow2wfs(self.p)
        rospy.loginfo("Received command wfs: %f", self.u)

    def callback_mpc(self, data):
        self.mpc_state = data.data
        rospy.loginfo("MPC state: %f", self.mpc_state)

    def predict_output(self):
        self.x = np.dot(self.ss_discrete.A, self.x) + \
            np.dot(self.ss_discrete.B, self.u)
        self.y = list(np.dot(self.ss_discrete.C, self.x) +
                      np.dot(self.ss_discrete.D, self.u))[0]
        self.pub_width.publish(self.y)
        rospy.loginfo("Sending y: %s", self.y)

    def set_arcstate(self, t):
        arc_state = t < arc_off
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


results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"
args = rospy.myargv(argv=sys.argv)
ts = int(args[1])
if len(args) > 2:
    simulation = bool(args[2] == '-s')
else:
    simulation = False
arc_off = 2000
cell = Cell(ts)
k = 0
if simulation:
    for i in range(10):
        cell.pub_arc.publish(False)
        cell.rate.sleep()
    try:
        while not rospy.is_shutdown():
            cell.set_arcstate(k)
            cell.predict_output()
            if cell.mpc_state:
                rospy.wait_for_message("fronius_remote_command",
                                       Float64MultiArray)
            k += 1
            cell.rate.sleep()
    except rospy.ROSInterruptException:
        pass
else:
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