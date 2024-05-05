import rospy
from std_msgs.msg import Float32, Bool, Float64MultiArray
import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
import numpy as np
import pandas as pd
import sys


class Cell(object):
    def __init__(self, ts):

        self.ts = ts
        # Rospy setup
        rospy.init_node("cell_node", anonymous=True)
        rospy.Subscriber("fronius_remote_command", Float32, self.callback)
        self.pub_arc = rospy.Publisher("kr90/arc_state", Bool, queue_size=10)
        self.pub_ts = rospy.Publisher(
            "kr90/kr90/travel_speed", Float32, queue_size=10)
        self.arc_idxs = [10, 2000]
        self.pub_width = rospy.Publisher(
            "xiris/bead/filtered", Float32, queue_size=10)
        self.pub_power = rospy.Publisher(
            "kr90/powersource_state", Float32, queue_size=10)

        self.fs = 10
        self.rate = rospy.Rate(self.fs)

        # Load data
        (self.process_input_train,
         self.process_output_train,
         _,
         _) = self.load_train_data(data_dir + "experiment/calibration/")

        self.process_input_train = self.process_input_train[:, 1:]
        self.process_output_train = self.process_output_train[:, 1:]

        self.process_u_min = self.process_input_train.min(axis=0)
        self.process_u_max = self.process_input_train.max(axis=0)
        self.process_y_min = self.process_output_train.min(axis=0)
        self.process_y_max = self.process_output_train.max(axis=0)

        self.process_inputs = self.process_input_train.shape[1]
        self.process_outputs = self.process_output_train.shape[1]

        # Load process model metrics
        self.metrics_process = pd.read_csv(results_dir +
                                           f"models/experiment/hp_metrics.csv"
                                           )
        process_best_model_id = 70
        process_best_model_filename = f"run_{process_best_model_id:03d}.keras"
        self.process_best_params = self.metrics_process[
            self.metrics_process["run_id"] == int(process_best_model_id)
        ]
        self.P = self.process_best_params.iloc[0, 1]
        self.Q = self.process_best_params.iloc[0, 2]

        # Load models
        self.process_model = load_model(
            results_dir +
            f"models/experiment/best/{process_best_model_filename}"
        )

        self.opt = Adam(learning_rate=self.process_best_params["lr"])
        self.process_model.compile(optimizer=self.opt, loss=mean_squared_error)

        # Historic
        self.M = self.P
        self.N = self.Q
        self.u_hist = np.zeros((self.M, self.process_inputs))
        self.y_hist = np.zeros((self.N,  self.process_outputs))

        # Current values
        self.arc_state = False
        self.time = 0.0
        self.p = 60.0
        self.f = self.pow2wfs(self.p)
        self.u = np.array([[self.f, self.ts]])
        self.u = (self.u - self.process_u_min) / \
            (self.process_u_max - self.process_u_min)
        self.x = np.zeros((2, 1))
        self.y = 0.0

    def callback(self, data):
        self.p = data.data
        self.f = self.pow2wfs(self.p)
        self.u = np.array([[self.f, self.ts]])
        rospy.loginfo("Received command wfs: %f", self.f)
        self.u = (self.u - self.process_u_min) / \
            (self.process_u_max - self.process_u_min)
        self.u_hist = self.update_hist(self.u_hist, self.u)

    def load_train_data(self, data_dir):
        input_train = pd.read_csv(
            data_dir + "input_train.csv").to_numpy().astype(np.float32)
        output_train = pd.read_csv(
            data_dir + "output_train.csv").to_numpy().astype(np.float32)
        input_test = pd.read_csv(
            data_dir + "input_test.csv").to_numpy().astype(np.float32)
        output_test = pd.read_csv(
            data_dir + "output_test.csv").to_numpy().astype(np.float32)
        return input_train, output_train, input_test, output_test

    def update_hist(self, current_hist, new_states):
        new_hist = current_hist.copy()
        len_new = new_states.shape[0]
        new_hist[:-len_new, :] = current_hist[len_new:, :]
        new_hist[-len_new:, :] = new_states
        return new_hist

    def build_sequence(self, u_hist, y_hist):
        u = u_hist.ravel()
        y = y_hist.ravel()
        return np.hstack((u, y)).reshape(
            (1, self.P * self.process_inputs + self.Q * self.process_outputs, 1))

    def predict_output(self):
        self.u_hist = self.update_hist(self.u_hist, self.u)
        seq_input = self.build_sequence(self.u_hist, self.y_hist)
        input_tensor = tf.convert_to_tensor(seq_input, dtype=tf.float32)
        self.y = self.process_model(input_tensor).numpy()[0, 0]
        self.y_hist = self.update_hist(self.y_hist, np.array([[self.y]]))
        self.y = self.y * (self.process_y_max -
                           self.process_y_min) + self.process_y_min
        self.y = self.y[0]
        self.pub_width.publish(self.y)
        rospy.loginfo("Sending y: %s", self.y)
        self.pub_power.publish(self.p + np.random.normal())
        rospy.loginfo("Sending power: %s", self.p + np.random.normal())
        # self.ts += np.random.normal(loc=0.0, scale=0.1)
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


data_dir = f"/home/lbarbosa/Documents/Github/lstm-control-waam/database/"
results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"
args = rospy.myargv(argv=sys.argv)
ts = int(args[1])
cell = Cell(ts)
k = 0
try:
    while not rospy.is_shutdown():
        cell.set_arcstate(k)
        cell.predict_output()
        cell.rate.sleep()
        k += 1
except rospy.ROSInterruptException:
    pass

rospy.spin()
