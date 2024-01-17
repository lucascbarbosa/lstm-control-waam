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
        self.data_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/database/experiment_igor/"
        self.results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"
        self.input_train, self.output_train, _, _ = self.load_experiment([1, 2, 3, 4, 5, 6], [7])
        self.input_scaling = "min-max"
        self.output_scaling = "min-max"
        
        if self.input_scaling == "mean-std":
            self.u_mean = self.input_train.mean(axis=0)
            self.u_std = self.input_train.std(axis=0)
        elif self.input_scaling == "min-max":
            self.u_min = self.input_train.min(axis=0)
            self.u_max = self.input_train.max(axis=0)

        if self.output_scaling == "mean-std":
            self.y_mean = self.output_train.mean(axis=0)
            self.y_std = self.output_train.std(axis=0)

        elif self.output_scaling == "min-max":
            self.y_min = self.output_train.min(axis=0)
            self.y_max = self.output_train.max(axis=0)

        metrics = pd.read_csv(self.results_dir + f"models/experiment_igor/hp_metrics.csv")
        best_model_id = 121
        best_model_filename = f"run_{best_model_id:03d}.keras"
        best_params = metrics[metrics["run_id"] == int(best_model_id)]
        self.P = best_params.iloc[0, 1]
        self.Q = best_params.iloc[0, 2]

        # Load process model
        self.model = load_model(
            self.results_dir + f"models/experiment_igor/best/{best_model_filename}"
        )

        opt = Adam(learning_rate=best_params["lr"])
        self.model.compile(optimizer=opt, loss=mean_squared_error)

        self.control_mpc = []
        self.u_hist = np.zeros((self.P, 1))
        self.y_hist = np.zeros((self.Q, 1))

        # Rospy setup
        rospy.init_node("cell_node", anonymous=True)
        rospy.Subscriber("fronius_remote_command", Float32, self.callback)
        self.pub_arc = rospy.Publisher("arc_state", Bool, queue_size=10)
        self.arc_idxs = [30, 350]
        self.pub_width = rospy.Publisher("xiris/bead/filtered", Float32, queue_size=10)
        fs = 10
        self.rate = rospy.Rate(fs)

    def callback(self, data):
        u = data.data
        rospy.loginfo("Received command wfs: %f", u)
        if self.input_scaling == "min-max":
            u_scaled = (u - self.u_min) / (self.u_max - self.u_min)
        if self.input_scaling == "mean-std":
            u_scaled = (u - self.u_mean) / self.u_std
        self.u_hist = self.update_hist(self.u_hist, u_scaled)
        self.control_mpc.append(u)

    def load_experiment(self, idxs_train, idxs_test):
        inputs_train = []
        outputs_train = []
        inputs_test = []
        outputs_test = []
        
        for idx_train in idxs_train:
            filename_train = f"bead{idx_train}"
            input_train = pd.read_csv(self.data_dir + filename_train + "_wfs.csv").to_numpy()
            output_train = pd.read_csv(
                self.data_dir + filename_train + "_w.csv"
            ).to_numpy()

            input_train = self.resample_data(
                input_train[:, 1], input_train[:, 0], output_train[:, 0]
            )
            inputs_train.append(input_train)
            outputs_train.append(output_train)

        inputs_train = np.concatenate(inputs_train, axis=0)
        outputs_train = np.concatenate(outputs_train, axis=0)
        
        for idx_test in idxs_test:
            filename_test = f"bead{idx_test}"
            input_test = pd.read_csv(self.data_dir + filename_test + "_wfs.csv").to_numpy()
            output_test = pd.read_csv(self.data_dir + filename_test + "_w.csv").to_numpy()

            input_test = self.resample_data(
                input_test[:, 1], input_test[:, 0], output_test[:, 0]
            )
            
            inputs_test.append(input_test)
            outputs_test.append(output_test)
            
        inputs_test = np.concatenate(inputs_test, axis=0)
        outputs_test = np.concatenate(outputs_test, axis=0)

        return (
            inputs_train[:, 1:],
            outputs_train[:, 1:],
            inputs_test[:, 1:],
            outputs_test[:, 1:],
        )

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

    # Load experiment method
    def update_hist(self, current_hist, new_states):
        new_hist = current_hist.copy()
        len_new = new_states.shape[0]
        new_hist[:-len_new, :] = current_hist[len_new:, :]
        new_hist[-len_new:, :] = new_states
        return new_hist

    def build_sequence(self):
        u = self.u_hist.ravel()
        y = self.y_hist.ravel()
        return np.hstack((u, y)).reshape((1, self.P + self.Q, 1))

    def predict_output(self):
        input_seq = self.build_sequence()
        input_tensor = tf.convert_to_tensor(input_seq, dtype=tf.float32)
        y_scaled = self.model(input_tensor).numpy()
        self.y_hist = self.update_hist(self.y_hist, y_scaled)
        if self.output_scaling == "min-max":
            y = y_scaled * (self.y_max - self.y_min) + self.y_min
        if self.output_scaling == "mean-std":
            y = y_scaled * self.y_std + self.y_mean
        self.pub_width.publish(y)
        rospy.loginfo("Sending output y: %f", y)

    def set_arcstate(self, t):
        arc_state = t > self.arc_idxs[0] and t < self.arc_idxs[1]
        self.pub_arc.publish(arc_state)
        rospy.loginfo("Sending arc_state: %s", arc_state)
        
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