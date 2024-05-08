"""MPC ROS node."""
import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
import threading
from std_msgs.msg import (Float64,
                          Bool,
                          Float64MultiArray,
                          MultiArrayDimension)
import rospy
import sys
import time
import pandas as pd
import numpy as np


class MPC:
    def __init__(self, bead_idx):

        self.bead_idx = bead_idx

        # Optimization parameters
        self.lr = 1e-1
        self.alpha_time = 1e-2
        self.alpha_opt = 1e-2
        self.cost_tol = 1e-3

        # Process data
        (self.process_input_train,
         self.process_output_train,
         self.process_input_test,
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
        process_best_model_id = 26
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
        self.M = self.P   # control horizon
        self.N = self.Q  # prediction horizon
        self.weight_control = 0.0
        self.weight_output = 1.0

        # Width count
        self.resample_factor = 2
        self.w_count = 0

        # Initial TS and reference
        self.reference_data = pd.read_csv(
            data_dir + f"experiment/control/references/bead{bead_idx}.csv").to_numpy()
        self.ts = self.reference_data[0, -2]
        self.ts = (self.ts - self.process_u_min[1]) / \
            (self.process_u_max[1] - self.process_u_min[1])
        # self.y_ref = self.reference_data[0, -1]
        self.y_ref = 5.0
        self.y_ref = (self.y_ref - self.process_y_min) / \
            (self.process_y_max[0] - self.process_y_min[0])

        # Historic data
        self.u_hist = np.zeros((self.P, self.process_inputs))
        self.u_hist[:, :] = [0.0, self.ts]
        self.y_hist = np.zeros((self.Q, self.process_outputs))

        # ROSPY Parameters
        rospy.init_node("mpc_node", anonymous=True)
        rospy.Subscriber("kr90/arc_state", Bool, self.callback_arc)
        self.arc_state = False
        rospy.Subscriber("xiris/bead/filtered", Float64, self.callback_width)
        self.pub = rospy.Publisher(
            "fronius_remote_command", Float64MultiArray, queue_size=10)
        self.pub_mpc = rospy.Publisher(
            "mpc_state", Bool, queue_size=10)
        self.pub = rospy.Publisher(
            "width_reference", Float64, queue_size=10)
        self. mpc_state = False
        self.pub_freq = 5  # sampling frequency of published data
        self.step_time = 1 / self.pub_freq
        self.rate = rospy.Rate(self.pub_freq * 2)

        # Forecast data
        # self.u_forecast = np.random.normal(loc=0.5, scale=0.1,
        #                                    size=(self.M, 1))
        self.u_forecast = np.full((self.M, 1), 0.0)
        self.u_forecast_data = []
        self.y_forecast_data = []

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
        rospy.loginfo("Received arc: %f", self.arc_state)

    def callback_width(self, data):
        if self.arc_state:
            if self.w_count % self.resample_factor == 0:
                y_row = data.data
                rospy.loginfo("Received output w: %f", y_row)
                y_row_scaled = (y_row - self.process_y_min) / \
                    (self.process_y_max - self.process_y_min)
                self.y_hist = self.update_hist(
                    self.y_hist, y_row_scaled.reshape((1, 1)))
                if y_row_scaled >= 0.0:
                    self.mpc_state = True
                    self.pub_mpc.publish(self.mpc_state)
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
        sequence = np.hstack((u, y)).reshape(
            (1, P * self.process_inputs + Q * self.process_outputs, 1))
        return sequence
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
    def cost_function(self):
        u_diff_forecast = self.create_control_diff(self.u_forecast)
        output_error = (self.y_ref - self.y_forecast) * \
            (self.process_y_max-self.process_y_min)

        output_cost = np.sum(output_error**2 * self.weight_output)
        control_cost = np.sum(u_diff_forecast**2 * self.weight_control)
        return output_cost + control_cost

    def compute_gradient(self, input_tensor, j):
        # start_time = time.time()
        with tf.GradientTape() as t:
            t.watch(input_tensor)
            output_tensor = self.process_model(input_tensor)
            gradient = t.gradient(
                output_tensor[:, j], input_tensor
            ).numpy()[0, :, 0]
        # print(time.time() - start_time)
        return output_tensor, gradient

    def split_gradient(self, grad):
        grad = grad.reshape(
            (self.P * self.process_inputs + self.Q * self.process_outputs,))
        u = grad[: self.process_inputs *
                 self.P].reshape((self.P, self.process_inputs))
        y = grad[self.process_inputs *
                 self.P:].reshape((self.Q, self.process_outputs))
        return u[:, 0], y

    def compute_step(self):
        u_forecast = self.u_forecast.copy()
        u_hist = self.u_hist.copy()
        y_hist = self.y_hist.copy()
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
                output_tensor, gradient = self.compute_gradient(
                    input_tensor, j)
                input_gradient, _ = self.split_gradient(gradient)

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
        output_error = (self.y_ref - y_forecast)
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
    def optimization_function(self):
        current_time = np.round(time.time(), 1)
        opt_step = 1
        cost = np.inf
        last_cost = cost
        delta_cost = -cost
        # gradient history for adaptive learning rate algorithm
        gradient_hist = np.zeros((self.process_input_test.shape[0], self.M))
        gradient_hist = []
        lr = self.lr
        while delta_cost < -self.cost_tol and opt_step < 15:
            steps, self.y_forecast = self.compute_step()
            cost = self.cost_function()
            delta_cost = cost - last_cost
            gradient_hist.append(steps[:, 0].ravel().tolist())
            ada_grad = np.sqrt(np.sum(np.array(gradient_hist)[
                :opt_step, :]**2, axis=0)+1e-10).reshape((self.M, 1))
            if verbose:
                print(f"Opt step: {opt_step} Cost: {cost}")
            if delta_cost < 0:
                self.u_forecast += (-lr/ada_grad)*steps
                self.u_forecast = np.clip(
                    self.u_forecast, a_min=0.0, a_max=1.0)
                lr = lr * (1.0 - self.alpha_opt)
                last_cost = cost
            else:
                if verbose:
                    print("Passed optimal solution")
                break
            opt_step += 1

        opt_time = time.time() - current_time
        print(f"Steps: {opt_step} Time: {opt_time:.2f} " +
              f"Time per step: {opt_time/opt_step:.2f} " +
              f"Time per grad: {opt_time/(opt_step*self.N):.3f}")

        print(
            f"U_F: {self.u_forecast * (self.process_u_max[0] - self.process_u_min[0]) + self.process_u_min[0]}")
        print(
            f"Y_F: {self.y_forecast * (self.process_y_max - self.process_y_min) + self.process_y_min}")
        print(
            f"Y_R: {self.y_ref * (self.process_y_max - self.process_y_min) + self.process_y_min}")

        # Save forecast
        self.u_forecast_data.append(self.u_forecast.ravel().tolist())
        self.y_forecast_data.append(self.y_forecast.ravel().tolist())

        if simulation:
            command = self.u_forecast[0] * (self.process_u_max[0] -
                                            self.process_u_min[0]) + \
                self.process_u_min[0]
            command = self.wfs2pow(command)
            msg.data = [command]
            self.pub.publish(msg)
            rospy.loginfo("Sending command: %f", command)

        # Send command
        self.u_forecast[:-1] = self.u_forecast[1:]
        self.lr = self.lr * (1.0 - self.alpha_time)

    def publish_command(self, command_index):
        # Get index
        idx = min(command_index, len(self.u_forecast)-1)
        # Update hist
        new_u = np.array([self.u_forecast[idx, 0], self.ts])
        self.u_hist = self.update_hist(self.u_hist, new_u)

        # Descaling
        command_forecast = self.u_forecast * (self.process_u_max[0] -
                                              self.process_u_min[0]) + \
            self.process_u_min[0]

        # Select command in forecast
        command = command_forecast[idx]

        # Convert to power
        command = self.wfs2pow(command)

        # Send command
        msg.data = [command]
        self.pub.publish(msg)
        rospy.loginfo("Sending command: %f", command)

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
if len(args) > 2:
    simulation = bool(args[2] == '-s')
else:
    simulation = False
mpc = MPC(bead_idx)
verbose = True

# MPC loop
delay_time = 3.0
rospy.wait_for_message("xiris/bead/filtered", Float64)  # Wait for width

# Timing parameters
forecast_time = mpc.N * mpc.step_time  # forecast period in seconds
# time in seconds after command_time to trigger optimization
trigger_time = forecast_time * 0.1  # 10% of closed loop
start_time = None

# Simulation timing index parameters
exp_index = 0
command_index = 0  # Index of command in command_forecast
delay_index = 30

# Send Initial command
msg = Float64MultiArray()
msg.data = [40.0]
dim = []
dim.append(MultiArrayDimension('PwrSrc', 1, 4))
msg.layout.dim = dim
rospy.loginfo("Sending command: %f", 40.0)
mpc.pub.publish(msg)
if simulation:
    while not rospy.is_shutdown():
        if mpc.arc_state:
            print(
                f"Time step: {exp_index}")
            if mpc.mpc_state and exp_index > delay_index:
                mpc.optimization_function()
            exp_index += 1
            mpc.rate.sleep()
        else:
            pass
else:
    while not rospy.is_shutdown():
        if mpc.arc_state:
            if start_time is None:
                start_time = np.round(time.time(), 1)
                exp_time = 0.0
                command_time = 0.0
            else:
                exp_time = np.round(time.time() - start_time, 1)
            if exp_time >= delay_time:
                print(
                    f"Time: {exp_time} Command_time: {command_time} Command: {command_index // 2}")
                if exp_time == command_time + trigger_time:
                    threading.Thread(target=mpc.optimization_function).start()
                mpc.publish_command(command_index//2)
                command_time = (exp_time // forecast_time) * forecast_time
                command_index += 1
                if exp_time == command_time + forecast_time:
                    command_index = 0
            mpc.rate.sleep()
        else:
            pass

mpc.export_forecast()
rospy.spin()
