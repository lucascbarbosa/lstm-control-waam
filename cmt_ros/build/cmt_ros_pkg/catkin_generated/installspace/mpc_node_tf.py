"""MPC ROS node."""
import numpy as np
import pandas as pd
import time
import sys
import rospy
from std_msgs.msg import (Float64,
                          Bool,
                          Float64MultiArray,
                          MultiArrayDimension)
import threading
import control


class MPC:
    def __init__(self, bead_idx):
        self.bead_idx = bead_idx

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

        # Define MPC parameters
        self.M = 20   # control horizon
        self.N = 20  # prediction horizon
        self.weight_control = 0.1
        self.weight_output = 100.0
        self.lr = 1e-2
        self.cost_tol = 1e-4

        # Width count
        self.resample_factor = 11
        self.w_count = 0

        # Initial TS and reference
        self.reference_data = pd.read_csv(
            data_dir + f"experiment/control/references/bead{bead_idx}.csv").to_numpy()
        self.ts = self.reference_data[0, -2]
        self.y_ref = self.reference_data[0, -1]

        # Historic data
        self.u_hist = np.zeros((self.P, self.process_inputs))
        self.u_hist[:, :] = [0.0, self.ts]
        self.y_hist = np.zeros((self.Q, self.process_outputs))

        # ROSPY Parameters
        rospy.init_node("mpc_node", anonymous=True)
        rospy.Subscriber("kr90/arc_state", Bool, self.callback_arc)
        self.arc_state = False
        rospy.Subscriber("xiris/bead/filtered", Float64, self.callback_width)
        self.pub__command = rospy.Publisher(
            "fronius_remote_command", Float64MultiArray, queue_size=10)
        self.pub__u_forecast = rospy.Publisher(
            "mpc/u_forecast", Float64MultiArray, queue_size=10)
        self.pub__y_forecast = rospy.Publisher(
            "mpc/y_forecast", Float64MultiArray, queue_size=10)
        self.pub__control_cost = rospy.Publisher(
            "mpc/control_cost", Float64, queue_size=10)
        self.pub__output_cost = rospy.Publisher(
            "mpc/output_cost", Float64, queue_size=10)
        self.pub__mpc_state = rospy.Publisher(
            "mpc/mpc_state", Bool, queue_size=10)

        self.pub_freq = 5  # sampling frequency of published data
        self.step_time = 1 / self.pub_freq
        self.rate = rospy.Rate(self.pub_freq)

        # Forecast data
        self.u_forecast = np.full((self.M, 1), 0.5)

        # gradient history for adaptive learning rate algorithm
        self.gradient_hist = np.zeros(self.u_forecast.shape)

        self.x_row = np.zeros((2, 1))

        # Load model
        ts_gain = pd.read_csv(results_dir + "models/experiment/model.csv")
        gain = ts_gain[ts_gain["TS"] == self.ts].values[0, 1]
        desvio = 0.95
        numerator = [0, 0, gain*desvio]
        denominator = [0.2, 1.2, 1]
        model_continuous = control.TransferFunction(numerator, denominator)
        model_discrete = control.sample_system(
            model_continuous, self.step_time, method='tustin')
        self.model_ss = control.tf2ss(model_discrete)

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
                self.y_hist = self.update_hist(
                    self.y_hist, y_row.reshape((1, 1)))
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

    def cost_function(self):
        u_diff_forecast = self.create_control_diff(self.u_forecast)
        output_error = (self.y_ref - self.y_forecast)
        output_cost = np.sum(output_error**2 * self.weight_output)
        control_cost = np.sum(u_diff_forecast**2 * self.weight_control)
        return output_cost, control_cost

    def create_control_vector(self, i):
        control_vector = np.zeros(N-i-1)
        for i in range(control_vector.shape[0]):
            control_vector[i] = np.dot(
                model_ss.C,
                np.dot(
                    np.linalg.matrix_power(model_ss.A, i+1),
                    model_ss.B
                )
            )
        return control_vector

    def compute_step(self):
        u_forecast = self.u_forecast.copy()
        output_jacobian = np.zeros((self.N, self.M))
        y_forecast = np.zeros((self.N, 1))
        for i in range(self.N):
            if i < self.M:
                u_row = u_forecast[i, 0]
            if i >= self.M:
                u_row = u_forecast[-1, 0]
            for j in range(self.process_outputs):
                x_row, y_row = self.predict_output(self.model_ss, x_row, u_row)
                output_jacobian[i, i] = self.model_ss.D
                output_jacobian[i+1:, i] = self.create_control_vector(i)
                y_forecast[i, :] = y_row

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
        lr = self.lr
        opt_time = current_time
        while delta_cost < -self.cost_tol and opt_time - current_time < 0.2:
            steps, self.y_forecast = self.compute_step()
            output_cost, control_cost = self.cost_function()
            cost = output_cost + control_cost
            delta_cost = cost - last_cost
            self.gradient_hist += steps ** 2
            ada_grad = np.sqrt(self.gradient_hist + 1e-10)
            if verbose:
                print(f"Opt step: {opt_step} Cost: {cost}")
            if delta_cost < 0:
                self.u_forecast += (-lr/ada_grad)*steps
                self.u_forecast = np.clip(
                    self.u_forecast, a_min=0.0, a_max=1.0)
                last_cost = cost
                last_control_cost = control_cost
                last_output_cost = output_cost
            else:
                if verbose:
                    print("Passed optimal solution")
                break
            opt_step += 1
            opt_time = np.round(time.time(), 1)

        print(f"Steps: {opt_step} Time: {opt_time:.2f} " +
              f"Time per step: {opt_time/opt_step:.2f} " +
              f"Time per grad: {opt_time/(opt_step*self.N):.3f}")
        print(
            f"U_F: {self.u_forecast}")
        print(
            f"Y_F: {self.y_forecast}")
        print(
            f"Y_R: {self.y_ref}")

        command = self.u_forecast[0, 0]

        # Convert to Power
        command = self.wfs2pow(command)  # convert to power

        # Publish command
        rospy.loginfo("Sending command: %f", command)
        msg = Float64MultiArray()
        msg.data = [command]
        dim = []
        dim.append(MultiArrayDimension('PwrSrc', 1, 4))
        msg.layout.dim = dim
        self.pub__command.publish(msg)

        # Publish costs
        rospy.loginfo("Sending control_cost: %f", last_control_cost)
        self.pub__control_cost.publish(last_control_cost)
        rospy.loginfo("Sending output_cost: %f", last_output_cost)
        self.pub__output_cost.publish(last_output_cost)

        # # Publish forecasts
        # msg = Float64MultiArray()
        # data = self.u_forecast.ravel(
        # ) * (self.process_u_max[0] - self.process_u_min[0]) + self.process_u_min[0]
        # data = data.tolist()
        # msg.data = data
        # dim = []
        # dim.append(MultiArrayDimension('u_forecast', self.M, 4))
        # msg.layout.dim = dim
        # self.pub__u_forecast.publish(msg)

        msg = Float64MultiArray()
        data = self.y_forecast.ravel()
        data = data.tolist()
        msg.data = data
        dim = []
        dim.append(MultiArrayDimension('y_forecast', self.N, 4))
        msg.layout.dim = dim
        self.pub__y_forecast.publish(msg)

        # Update u_forecast
        self.u_forecast[:-1] = self.u_forecast[1:]


# Filepaths
data_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/database/"
results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"

# Create an instance of the MPC class
args = rospy.myargv(argv=sys.argv)
bead_idx = int(args[1])
mpc = MPC(bead_idx)
verbose = True

# MPC loop
initial_delay = 3.0
msg = Float64MultiArray()
msg.data = [60.0]
dim = []
dim.append(MultiArrayDimension('PwrSrc', 1, 4))
msg.layout.dim = dim
rospy.wait_for_message("xiris/bead/filtered", Float64)  # Wait for width
mpc.pub__command.publish(msg)

start_time = None
u_forecast = None
mpc_state = False
while not rospy.is_shutdown():
    if mpc.arc_state:
        if start_time is None:
            start_time = np.round(time.time(), 1)
            exp_time = 0.0
        else:
            exp_time = np.round(time.time() - start_time, 1)
        print(f"Time: {exp_time} s")
        if exp_time >= initial_delay:
            threading.Thread(target=mpc.optimization_function).start()
            if not mpc_state:
                mpc_state = True
                mpc.pub__mpc_state.publish(True)
        mpc.rate.sleep()
    else:
        pass
