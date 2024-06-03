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
        plant_df = pd.read_csv(results_dir + "models/experiment/model.csv")
        gain = plant_df[plant_df["TS"] == ts].values[0, 1]

        # Rospy setup
        rospy.init_node("cell_node", anonymous=True)
        rospy.Subscriber("fronius_remote_command",
                         Float64MultiArray, self.callback__command)
        rospy.Subscriber("mpc_state", Bool, self.callback__mpc_state)
        rospy.Subscriber(
            "mpc/u_forecast", Float64MultiArray, self.callback__u_forecast)
        rospy.Subscriber(
            "mpc/y_forecast", Float64MultiArray, self.callback__y_forecast)
        rospy.Subscriber(
            "mpc/control_cost", Float64, self.callback__control_cost)
        rospy.Subscriber(
            "mpc/output_cost", Float64, self.callback__output_cost)
        rospy.Subscriber(
            "mpc/mpc_state", Bool, self.callback__mpc_state)

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

    def callback__command(self, data):
        self.p = data.data[0]
        rospy.loginfo("Received command power: %f", self.p)
        self.u = np.sqrt(self.pow2wfs(self.p))

    def callback__mpc_state(self, data):
        self.mpc_state = data.data
        rospy.loginfo("Received MPC state: %f", self.mpc_state)

    def callback__control_cost(self, data):
        self.control_cost = data.data
        rospy.loginfo("Received MPC control_cost: %f", self.control_cost)

    def callback__output_cost(self, data):
        self.output_cost = data.data
        rospy.loginfo("Received MPC output_cost: %f", self.output_cost)

    def callback__u_forecast(self, data):
        self.u_forecast = data.data
        print(f"Received u_forecast: {self.u_forecast}")

    def callback__y_forecast(self, data):
        self.y_forecast = data.data
        print(f"Received y_forecast: {self.y_forecast}")

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
arc_off = 2000
cell = Cell(ts)
k = 0
while not rospy.is_shutdown():
    cell.set_arcstate(k)
    cell.time += cell.T
    cell.predict_output()
    k += 1
    cell.rate.sleep()

rospy.spin()
