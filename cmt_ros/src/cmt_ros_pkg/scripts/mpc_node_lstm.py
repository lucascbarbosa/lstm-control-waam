import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
import joblib

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

import rospy
from std_msgs.msg import (Float32,
                          Float64,
                          Bool,
                          Float64MultiArray,
                          MultiArrayDimension)
import time
import sys


class MPC:
    def __init__(self, bead_idx):

        self.bead_idx = bead_idx

        # Optimization parameters
        self.lr = 1e-1
        self.alpha_time = 1e-3
        self.alpha_opt = 1e-3
        self.cost_tol = 1e-2

        # Process data
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
        process_best_model_id = 3
        process_best_model_filename = f"run_{process_best_model_id:03d}.keras"
        self.process_best_params = self.metrics_process[
            self.metrics_process["run_id"] == int(process_best_model_id)
        ]
        self.P = self.process_best_params.iloc[0, 1]
        self.Q = self.process_best_params.iloc[0, 2]

        # Load process model
        self.process_model = load_model(
            results_dir +
            f"models/experiment/best/{process_best_model_filename}"
        )

        self.opt = Adam(learning_rate=self.process_best_params["lr"])
        self.process_model.compile(optimizer=self.opt, loss=mean_squared_error)

        # Define MPC parameters
        self.M = self.P  # control horizon
        self.N = self.Q  # prediction horizon
        self.weight_control = 0.1
        self.weight_output = 1.0

        # Width count
        self.resample_factor = 11
        self.w_count = 0

        # Initial TS and reference
        self.reference_data = pd.read_csv(
            data_dir + f"experiment/control/references/bead{bead_idx}.csv").to_numpy()
        self.ts = self.reference_data[0, -2]
        self.ts = (self.ts - self.process_u_min[1]) / \
            (self.process_u_max[1] - self.process_u_min[1])
        self.y_ref = self.reference_data[0, -1]
        self.y_ref = (self.y_ref - self.process_y_min) / \
            (self.process_y_max[0] - self.process_y_min[0])

        # Historic data
        self.u_hist = np.zeros((self.P, self.process_inputs))
        self.u_hist[0, :] = [0.0, self.ts]
        self.y_hist = np.zeros((self.Q, self.process_outputs))

        # Forecast data
        self.u_forecast_data = []
        self.y_forecast_data = []

        # ROSPY Parameters
        rospy.init_node("mpc_node", anonymous=True)
        rospy.Subscriber("kr90/arc_state", Bool, self.callback_arc)
        self.arc_state = False
        rospy.Subscriber("xiris/bead/filtered", Float64, self.callback_width)
        self.pub = rospy.Publisher(
            "fronius_remote_command", Float64MultiArray, queue_size=10)
        self.pub_freq = 5  # sampling frequency of published data
        self.step_time = 1 / self.pub_freq
        self.rate = rospy.Rate(self.pub_freq)

    def pow2wfs(self, p):
        return np.round((p*9/100)+1.5, 3)

    def wfs2pow(self, f):
        return np.round((f-1.5)*100/9)

    def callback_arc(self, data):
        if not self.arc_state and bool(data.data):
            self.arcon_time = time.time()
        elif self.arc_state and not bool(data.data):
            rospy.signal_shutdown("Shutting down")
        self.arc_state = bool(data.data)

    def callback_width(self, data):
        if self.arc_state:
            if self.w_count % self.resample_factor == 0:
                y_row = data.data
                # rospy.loginfo("Received output w: %f", y_row)
                y_row_scaled = (y_row - self.process_y_min) / \
                    (self.process_y_max - self.process_y_min)
                self.y_hist = self.update_hist(
                    self.y_hist, y_row_scaled.reshape((1, 1)))
            self.w_count += 1

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
        P = u_hist.shape[0]
        Q = y_hist.shape[0]
        return np.hstack((u, y)).reshape(
            (1, P * self.process_inputs + Q * self.process_outputs, 1))

    def split_gradient(self, grad):
        grad = grad.reshape(
            (1 * (self.P * self.process_inputs + self.Q * self.process_outputs),
             ))
        u = grad[: self.process_inputs *
                 self.P].reshape((self.P, self.process_inputs))[:, 0]
        y = grad[self.process_inputs *
                 self.P:].reshape((self.Q, self.process_outputs))
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
    def cost_function(self, u_forecast, y_forecast):
        u_diff_forecast = self.create_control_diff(u_forecast)
        output_error = (self.y_ref - y_forecast) * \
            (self.process_y_max-self.process_y_min)

        output_cost = np.sum(output_error**2 * self.weight_output)
        control_cost = np.sum(u_diff_forecast**2 * self.weight_control)
        return output_cost + control_cost

    def compute_gradient(self, input_tensor, j):
        with tf.GradientTape() as t:
            t.watch(input_tensor)
            output_tensor = self.process_model(input_tensor)
            gradient = t.gradient(
                output_tensor[:, j], input_tensor
            ).numpy()[0, :, 0]
        return output_tensor, gradient

    def compute_step(self, u_hist, y_hist, u_forecast):
        output_jacobian = np.zeros((self.N, self.M))
        y_forecast = np.zeros((self.N, 1))
        for i in range(self.N):
            if i < self.M:
                u_row = np.array([[u_forecast[i, 0], self.ts]])
            if i >= self.M:
                u_row = np.array([[u_forecast[-1, 0], self.ts]])
            u_hist = self.update_hist(u_hist, u_row)
            seq_input = self.build_sequence(u_hist, y_hist)
            input_tensor = tf.convert_to_tensor(seq_input, dtype=tf.float32)
            for j in range(self.process_outputs):
                output_tensor, gradient_real = self.compute_gradient(
                    input_tensor, j)
                input_gradient, _ = self.split_gradient(gradient_real)

                if i < self.P - 1:
                    output_jacobian[i, : i + 1] = input_gradient[-(i + 1):]
                else:
                    output_jacobian[i, :] = input_gradient[:]

            y_row = output_tensor.numpy().reshape((1, 1))
            y_forecast[i, :] = y_row
            y_hist = self.update_hist(y_hist, y_row)

        input_jacobian = self.build_input_jacobian()
        steps = np.zeros(u_forecast.shape)
        u_diff_forecast = self.create_control_diff(u_forecast)
        output_error = (self.y_ref - y_forecast) * \
            (self.process_y_max-self.process_y_min)
        input_diff = u_diff_forecast

        for j in range(self.M):
            output_step = (
                -2
                * np.diag(output_error.T @ output_jacobian[:, j])
                * self.weight_output
            )

            input_step = (
                2 * input_jacobian[:, j].T @ input_diff * self.weight_control
            )

            total_step = output_step + input_step
            steps[j, 0] = total_step

        return steps, y_forecast

    # Optimization function method
    def optimization_function(self, u_hist, y_hist, lr, u_forecast=None,
                              verbose=False):
        opt_time = time.time()
        if u_forecast is None:
            u_forecast = np.random.normal(loc=0.5, scale=0.1,
                                          size=(self.M, 1))
            # u_forecast = np.random.uniform(size=(self.M, 1))
        opt_step = 0
        cost = np.inf
        last_cost = cost
        delta_cost = -cost
        # gradient history for adaptive learning rate algorithm
        # gradient_hist = np.zeros((self.process_input_test.shape[0],self.M))
        gradient_hist = []
        converged = True
        while delta_cost < -self.cost_tol:
            steps, y_forecast = self.compute_step(u_hist, y_hist, u_forecast)
            cost = self.cost_function(u_forecast, y_forecast)
            delta_cost = cost - last_cost
            gradient_hist.append(steps[:, 0].ravel().tolist())
            ada_grad = np.sqrt(np.sum(np.array(gradient_hist)[
                :opt_step+1, :]**2, axis=0)+1e-10).reshape((self.M, 1))
            if verbose:
                print(f"Opt step: {opt_step+1} Cost: {cost}\n")
            if delta_cost < 0:
                u_forecast += (-lr/ada_grad)*steps
                u_forecast = np.clip(u_forecast, a_min=0.0, a_max=1.0)
                lr = lr * (1.0 - self.alpha_opt)
                last_cost = cost
                opt_step += 1
            else:
                if verbose:
                    print("Passed optimal solution")
                converged = False
                break

        print(
            f"U_F: {u_forecast * (self.process_u_max[0] - self.process_u_min[0]) + self.process_u_min[0]}")
        print(f"Y_F: {y_forecast}")
        print(f"Y_R: {self.y_ref}")
        # Save forecast
        self.u_forecast_data.append(u_forecast.ravel().tolist())
        self.y_forecast_data.append(y_forecast.ravel().tolist())

        u_opt = u_forecast[0, 0]
        # Descaling
        u_opt = u_opt * (self.process_u_max[0] -
                         self.process_u_min[0]) + self.process_u_min[0]
        command_opt = self.wfs2pow(u_opt)  # convert to power
        # Send command
        msg = Float64MultiArray()
        msg.data = [command_opt]
        dim = []
        dim.append(MultiArrayDimension('PwrSrc', 1, 4))
        msg.layout.dim = dim
        self.pub.publish(msg)
        rospy.loginfo("Sending command: %f", command_opt)
        opt_time = time.time() - opt_time
        print(f"Steps: {opt_step} Time: {opt_time:.2f}")
        return u_opt, u_forecast, y_forecast

    def export_forecast(self):
        np.savetxt(results_dir + "predictions/forecast/u_forecast.csv",
                   np.array(self.u_forecast_data))
        np.savetxt(results_dir + "predictions/forecast/y_forecast.csv",
                   np.array(self.y_forecast_data))


# Filepaths
data_dir = f"/home/lbarbosa/Documents/Github/lstm-control-waam/database/"
results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"


# Create an instance of the MPC class
args = rospy.myargv(argv=sys.argv)
bead_idx = int(args[1])
mpc = MPC(bead_idx)
# u_forecast = np.random.normal(loc=0.5, scale=0.05, size=(M, 1)) #
# u_forecast = np.random.uniform(size=(mpc.M, 1)) #

# MPC loop
exp_time = 0.0
exp_step = 1
start_time = time.time()
msg = Float64MultiArray()
msg.data = [40.0]
dim = []
dim.append(MultiArrayDimension('PwrSrc', 1, 4))
msg.layout.dim = dim
rospy.wait_for_message("xiris/bead/filtered", Float64)  # Wait for width
mpc.pub.publish(msg)
while not rospy.is_shutdown():
    if mpc.arc_state:
        if exp_step == 1:
            print('Sleeping 5 seconds')
            time.sleep(5)
        print(f"Time step: {exp_step}")
        u_opt, u_forecast, y_forecast = mpc.optimization_function(
            mpc.u_hist,
            mpc.y_hist,
            mpc.lr,
            u_forecast=None,
            verbose=True)
        u_forecast[:-1] = u_forecast[1:]
        mpc.rate.sleep()
        exp_step += 1
        exp_time += mpc.step_time
        mpc.lr = mpc.lr * (1.0 - mpc.alpha_time)
    else:
        pass

mpc.export_forecast()
rospy.spin()
