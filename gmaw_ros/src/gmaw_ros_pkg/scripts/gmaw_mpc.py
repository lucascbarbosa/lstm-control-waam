import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

import rospy
from std_msgs.msg import Float32

import time

class MPC:
    def __init__(self):
        # Filepaths
        self.data_dir = f"/home/lbarbosa/Documents/Github/lstm-control-waam/database/experiment/"
        self.results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"

        # ROSPY Parameters
        rospy.init_node("mpc_node", anonymous=True)
        rospy.Subscriber("y", Float32, self.callback)
        self.pub = rospy.Publisher("u", Float32, queue_size=10)
        self.pub_freq = 30  # sampling frequency of published data
        self.step_time = 1 / self.pub_freq
        self.total_steps = 10
        self.rate = rospy.Rate(self.pub_freq)

        # Experiment data
        self.y = []
        self.u = []

        # Optimization parameters
        self.lr = 5e-2
        self.alpha = 1e-3
        self.cost_tol = 0.1

        # Load data
        self.inputs_train, self.outputs_train, _, _ = self.load_experiment(1, 2)

        self.u_min = self.inputs_train.min(axis=0)
        self.u_max = self.inputs_train.max(axis=0)
        self.y_mean = self.outputs_train.mean(axis=0)
        self.y_std = self.outputs_train.std(axis=0)

        # Load metrics
        self.metrics_df = pd.read_csv(self.results_dir + f"models/experiment/hp_metrics.csv")
        self.best_model_id = 85
        self.best_model_filename = f"run_{self.best_model_id:03d}.keras"
        self.best_params = self.metrics_df[self.metrics_df["run_id"] == int(self.best_model_id)]
        self.P = self.best_params.iloc[0, 1]
        self.Q = self.best_params.iloc[0, 2]

        # Load Keras model
        self.keras_model = load_model(
            self.results_dir + f"models/experiment/best/{self.best_model_filename}"
        )

        self.opt = Adam(learning_rate=self.best_params["lr"])
        self.keras_model.compile(optimizer=self.opt, loss=mean_squared_error)

        # Define MPC parameters
        self.M = self.P  # control horizon
        self.N = self.Q  # prediction horizon
        self.weight_control = 0.1 
        self.weight_output = 10

        # Desired outputs
        self.y_ref = np.zeros(1)

        # Historic data
        self.u_hist = np.zeros((self.P, 1))
        self.y_hist = np.zeros((self.Q, 1))

        self.u_forecast = np.random.normal(loc=0.5, scale=0.05, size=(self.M, 1)) #

    # Callback method
    def callback(self, data):
        rospy.loginfo("Received output y: %f", data.data)
        y_row = data.data
        t = time.time()
        self.y.append([t-start_time, y_row])
        y_row_scaled = (y_row - self.y_mean) / self.y_std
        self.y_hist = self.update_hist(self.y_hist, y_row_scaled.reshape((1, 1)))

    # Load experiment method
    def load_experiment(self, idx_train, idx_test):
        filename_train = f"bead{idx_train}"
        input_train = pd.read_csv(self.data_dir + filename_train + "_wfs.csv").to_numpy()
        output_train = pd.read_csv(
            self.data_dir + filename_train + "_w.csv"
        ).to_numpy()

        output_train = self.resample_data(
            output_train[:, 1], output_train[:, 0], input_train[:, 0]
        )

        filename_test = f"bead{idx_test}"
        input_test = pd.read_csv(self.data_dir + filename_test + "_wfs.csv").to_numpy()
        output_test = pd.read_csv(self.data_dir + filename_test + "_w.csv").to_numpy()

        output_test = self.resample_data(
            output_test[:, 1], output_test[:, 0], input_test[:, 0]
        )

        return (
            input_train[:, 1:],
            output_train[:, 1:],
            input_test[:, 1:],
            output_test[:, 1:],
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

    def update_hist(self, current_hist, new_states):
        new_hist = current_hist.copy()
        len_new = new_states.shape[0]
        new_hist[:-len_new, :] = current_hist[len_new:, :]
        new_hist[-len_new:, :] = new_states
        return new_hist

    def build_sequence(self, u_hist, y_hist):
        u = u_hist.ravel()
        y = y_hist.ravel()
        return np.hstack((u, y)).reshape((1, 1 * (self.P + self.Q), 1))

    def split_sequence(self, seq):
        seq = seq.reshape((1 * (self.P + self.Q),))
        u = seq[: 1 * self.P].reshape((self.P, 1))
        y = seq[1 * self.P :].reshape((self.Q, 1))
        return u, y
    
    # Create control diff method
    def create_control_diff(self, u_forecast):
        u_diff = u_forecast.copy()
        u_diff[1:] = u_diff[1:] - u_diff[:-1]
        return u_diff

    # Build input jacobian method
    def build_input_jacobian(self):
        input_jacobian = np.eye(self.M)
        for i in range(self.M):
            if i < self.M - 1:
                input_jacobian[i + 1, i] = -1
        return input_jacobian

    # Cost function method
    def cost_function(self, u_forecast, y_forecast, y_ref):
        u_diff_forecast = self.create_control_diff(u_forecast)
        output_error = (y_ref - y_forecast) * self.y_std
        output_cost = np.sum(output_error**2 * self.weight_output)
        control_cost = np.sum(u_diff_forecast**2 * self.weight_control)
        return output_cost + control_cost

    def compute_step(self, u_hist, y_hist, u_forecast, lr):
        output_jacobian = np.zeros((self.N, self.M))
        y_forecast = np.zeros((self.N, 1))
        for i in range(self.N):
            if i < self.M:
                u_row = u_forecast[i].reshape((1, 1))
            if i >= self.M:
                u_row = u_forecast[-1].reshape((1, 1))
            u_hist = self.update_hist(u_hist, u_row)
            seq_input = self.build_sequence(u_hist, y_hist)
            input_tensor = tf.convert_to_tensor(seq_input, dtype=tf.float32)
            for j in range(1):
                with tf.GradientTape() as t:
                    t.watch(input_tensor)
                    output_tensor = self.keras_model(input_tensor)
                    gradient = t.gradient(
                        output_tensor[:, j], input_tensor
                    ).numpy()[0, :, 0]

                input_gradient, _ = self.split_sequence(gradient)
                if i < self.P - 1:
                    output_jacobian[i, : i + 1] = input_gradient[
                        -(i + 1) :, :
                    ].ravel()
                else:
                    output_jacobian[i, :] = input_gradient[:, :].ravel()

            y_row = output_tensor.numpy().reshape((1, 1))
            y_forecast[i, :] = y_row
            y_hist = self.update_hist(y_hist, y_row)
        # ---------

        input_jacobian = self.build_input_jacobian()
        steps = np.zeros(u_forecast.shape)
        u_diff_forecast = self.create_control_diff(u_forecast)
        output_error = (self.y_ref - y_forecast) * self.y_std
        input_diff = u_diff_forecast
        for j in range(self.M):
            output_gradient = (
                -2
                * np.diag(output_error.T @ output_jacobian[:, j])
                * self.weight_output
            )

            input_gradient = (
                2 * input_jacobian[:, j].T @ input_diff * self.weight_control
            )

            steps[j, 0] = -lr * (output_gradient + input_gradient)

        return steps, y_forecast

    # Optimization function method
    def optimization_function(self, u_hist, y_hist, lr, u_forecast=None):
        if u_forecast is None:
            u_forecast = np.random.normal(loc=0.5, scale=0.05, size=(M, 1)) #
        s = 0
        cost = np.inf
        last_cost = cost
        delta_cost = -cost
        while delta_cost < -self.cost_tol:
            steps, y_forecast = self.compute_step(u_hist, y_hist, u_forecast, lr)
            cost = self.cost_function(u_forecast, y_forecast, self.y_ref)
            delta_cost = cost - last_cost
            print(f"Opt step: {s+1}")
            print(f"Cost: {cost}\n ")
            if delta_cost < 0:
                u_forecast += steps
                lr = lr * (1.0 - self.alpha)
                last_cost = cost
                s += 1
            else:
                print("Passed optimal solution")
                break
        u_opt = u_forecast[0, :]
        return u_opt, u_forecast, y_forecast


start_time = time.time()
# Create an instance of the MPC class
mpc = MPC()

# MPC loop
exp_time = 0
exp_step = 1
rospy.wait_for_message('y', Float32)
print(f"y: {mpc.y}")
while not rospy.is_shutdown():
    print(f"Time step: {exp_step}")
    u_opt, u_forecast, y_forecast = mpc.optimization_function(mpc.u_hist, mpc.y_hist, mpc.lr, mpc.u_forecast)
    mpc.u_hist = mpc.update_hist(mpc.u_hist, u_opt.reshape((1, 1)))
    u_opt = u_opt[0]
    u_row = u_opt * (mpc.u_max - mpc.u_min) + mpc.u_min  # Denormalize
    mpc.u.append(u_row)
    
    # Send the "u_row" variable
    mpc.pub.publish(u_row)
    rospy.loginfo("Sending control u_opt: %f", u_row)
    mpc.rate.sleep()
    exp_step += 1
    exp_time = mpc.step_time
    
rospy.spin()

