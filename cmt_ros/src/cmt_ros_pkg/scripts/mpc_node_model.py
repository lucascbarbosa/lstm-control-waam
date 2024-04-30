import tensorflow as tf
from keras.models import load_model
import joblib

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

import rospy
from std_msgs.msg import Float32, Bool, Float64MultiArray, MultiArrayDimension
import time
import control
import sys


class MPC:
    def __init__(self, bead_idx):

        self.bead_idx = bead_idx
        self.reference_data = pd.read_csv(
            data_dir + f"experiment/control/references/bead{bead_idx}.csv").to_numpy()

        # Optimization parameters
        self.lr = 1e-1
        self.alpha_time = 1e-3
        self.alpha_opt = 1e-3
        self.cost_tol = 1e-2
        self.M = 5
        self.N = 5
        self.weight_control = 1
        self.weight_output = 1

        # ROSPY Parameters
        rospy.init_node("mpc_node", anonymous=True)
        rospy.Subscriber("kr90/arc_state", Bool, self.callback_arc)
        self.arc_state = False
        rospy.Subscriber("xiris/bead/filtered", Float32, self.callback_width)
        rospy.Subscriber("kr90/powersource_state",
                         Float32, self.callback_power)
        rospy.Subscriber("kr90/travel_speed", Float32, self.callback_ts)
        self.pub = rospy.Publisher(
            "fronius_remote_command", Float64MultiArray, queue_size=10)
        self.pub_freq = 10  # sampling frequency of published data
        self.step_time = 1 / self.pub_freq
        self.total_steps = 10
        self.rate = rospy.Rate(self.pub_freq)

        # Define system model
        self.process_inputs = 1
        self.process_outputs = 1
        numerator = [0, 0, 0.8]
        denominator = [0.2, 1.2, 1]
        self.T = 1/self.pub_freq
        G_continuous = control.TransferFunction(numerator, denominator)
        G_discrete = control.sample_system(
            G_continuous, self.T, method='tustin')
        self.ss_discrete = control.tf2ss(G_discrete)

        self.y_ref = 0.0

        # Current sort_values
        self.u = 0.0
        self.x = np.zeros((2, 1))
        self.y = 0.0

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

    def callback_ts(self, data):
        ts = data.data
        # rospy.loginfo("Received TS %f", ts)

    def callback_power(self, data):
        p = data.data
        # rospy.loginfo("Received power %f", p)
        f = self.pow2wfs(p)
        self.u = f
        self.x = np.dot(self.ss_discrete.A, self.x) + \
            np.dot(self.ss_discrete.B, self.u)
        # print(self.x, self.u)
        y = list(np.dot(self.ss_discrete.C, self.x) +
                 np.dot(self.ss_discrete.D, self.u))[0]

    def callback_width(self, data):
        if self.arc_state:
            self.y = data.data
            # rospy.loginfo("Received output w: %f", self.y)
        self.set_reference()

    def create_control_diff(self, u_forecast):
        u_diff = u_forecast.copy()
        u_diff[1:] = u_diff[1:] - u_diff[:-1]
        return u_diff

    def cost_function(self, u_forecast, y_forecast):
        u_diff_forecast = self.create_control_diff(u_forecast)
        output_error = self.y_ref - y_forecast

        output_cost = np.sum(output_error**2 * self.weight_output)
        control_cost = np.sum(u_diff_forecast**2 * self.weight_control)
        return output_cost + control_cost

    def create_controL_vector(self, i):
        control_vector = np.zeros(self.N-i-1)
        for i in range(control_vector.shape[0]):
            control_vector[i] = np.dot(
                self.ss_discrete.C,
                np.dot(
                    np.linalg.matrix_power(self.ss_discrete.A, i+1),
                    self.ss_discrete.B))
        return control_vector

    def build_input_jacobian(self):
        input_jacobian = np.eye(self.M)
        for i in range(self.M):
            if i < self.M - 1:
                input_jacobian[i + 1, i] = -1
        return input_jacobian

    def compute_step(self, u_forecast):
        output_jacobian = np.zeros((self.N, self.M))
        y_forecast = np.zeros((self.N, 1))
        x_row = self.x.copy()
        # Create prediction
        for i in range(self.N):
            if i < self.M:
                u_row = u_forecast[i]
                output_jacobian[i, i] = self.ss_discrete.D
                output_jacobian[i+1:, i] = self.create_controL_vector(i)
            if i >= self.M:
                u_row = u_forecast[-1]
            for j in range(self.process_inputs):
                x_row = np.dot(self.ss_discrete.A, x_row) + \
                    self.ss_discrete.B * u_row
                y_forecast[i, j] = list(np.dot(self.ss_discrete.C, x_row) +
                                        self.ss_discrete.D * u_row)[0]

        input_jacobian = self.build_input_jacobian()
        steps = np.zeros(u_forecast.shape)
        u_diff_forecast = self.create_control_diff(u_forecast)
        output_error = self.y_ref - y_forecast
        input_diff = u_diff_forecast

        for j in range(self.M):
            output_step = (
                -2
                * np.diag(output_error.T @ output_jacobian[:, j])
                * self.weight_output
            )

            input_step = (
                2 * input_jacobian[:, j].T @ input_diff *
                self.weight_control
            )

            total_step = output_step + input_step
            steps[j, 0] = total_step

        return steps, y_forecast

    def optimization_function(self, lr, u_forecast=None, verbose=False):
        opt_time = time.time()
        if u_forecast is None:
            # u_forecast = np.random.normal(loc=0.5, scale=0.05, size=(self.M, 1)) #
            u_forecast = np.random.uniform(low=5.1, high=8.7, size=(self.M, 1))
        opt_step = 0
        cost = np.inf
        last_cost = cost
        delta_cost = -cost
        # gradient_hist = np.zeros((self.process_input_test.shape[0],self.M)) # gradient history for adaptive learning rate algorithm
        gradient_hist = []  # gradient history for adaptive learning rate algorithm
        converged = True
        while delta_cost < -self.cost_tol:
            steps, y_forecast = self.compute_step(u_forecast)
            cost = self.cost_function(u_forecast, y_forecast)
            delta_cost = cost - last_cost
            gradient_hist.append(steps[:, 0].ravel().tolist())
            ada_grad = np.sqrt(np.sum(np.array(gradient_hist)[
                :opt_step+1, :]**2, axis=0)+1e-10).reshape((self.M, 1))
            if verbose:
                print(f"Opt step: {opt_step+1} Cost: {cost}\n")
            if delta_cost < 0:
                u_forecast += (-lr/ada_grad)*steps
                u_forecast = np.clip(u_forecast, a_min=5.1, a_max=8.7)
                lr = lr * (1.0 - self.alpha_opt)
                last_cost = cost
                opt_step += 1
            else:
                if verbose:
                    print("Passed optimal solution")
                converged = False
                break
        u_opt = u_forecast[0, :]
        u_opt = u_opt[0]
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

    def set_reference(self):
        if self.arc_state:
            current_time = np.round(time.time() - self.arcon_time, 1)
            idx = np.where(current_time > self.reference_data[:, 0])[0]
            if len(idx) > 0:
                idx = idx[-1]
                self.y_ref = self.reference_data[idx, -1]

    def export_gradient(self):
        np.savetxt(results_dir + "predictions/gradient/gradient_reals.csv",
                   np.array(self.gradient_reals))
        np.savetxt(results_dir + "predictions/gradient/gradient_preds.csv",
                   np.array(self.gradient_preds))


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
exp_time = 0
exp_step = 1
start_time = time.time()
rospy.wait_for_message("xiris/bead/filtered", Float32)  # Wait for width
mpc.pub.publish(60)  # publish initial command of 60%
while not rospy.is_shutdown():
    if mpc.arc_state:
        print(f"Time step: {exp_step}")
        u_opt, u_forecast, y_forecast = mpc.optimization_function(
            mpc.lr,
            u_forecast=None,
            verbose=True)
        u_forecast[:-1] = u_forecast[1:]
        # Send the "u_row" variable
        mpc.rate.sleep()
        exp_step += 1
        exp_time = mpc.step_time
        mpc.lr = mpc.lr * (1.0 - mpc.alpha_time)
    else:
        pass

rospy.spin()
