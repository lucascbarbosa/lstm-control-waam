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
        self.data_dir = f"/home/lbarbosa/Documents/Github/lstm-control-waam/database/"
        self.results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"

        # Experiment data
        self.y = []
        self.u = []

        # Optimization parameters
        self.lr = 5e-2
        self.alpha_time = 1e-3
        self.alpha_opt = 1e-3
        self.cost_tol = 1e-2

        # Load data
        self.process_inputs_train, self.process_outputs_train, self.process_input_test, _ = self.load_experiment([1, 2, 3, 4, 5, 6], [7])
        self.mpc_inputs_train, self.mpc_outputs_train, _, _ = self.load_mpc()

        self.input_scaling = "min-max"
        self.output_scaling = "min-max"
        if self.input_scaling == "mean-std":
            self.process_y_mean = self.process_inputs_train.mean(axis=0)
            self.process_y_std = self.process_inputs_train.std(axis=0)
            self.mpc_y_mean = self.mpc_inputs_train.mean(axis=0)
            self.mpc_y_std = self.mpc_inputs_train.std(axis=0)

        elif self.input_scaling == "min-max":
            self.process_y_min = self.process_inputs_train.min(axis=0)
            self.process_y_max = self.process_inputs_train.max(axis=0)
            self.mpc_y_min = self.mpc_inputs_train.min(axis=0)
            self.mpc_y_max = self.mpc_inputs_train.max(axis=0)

        if self.output_scaling == "mean-std":
            self.process_u_mean = self.process_outputs_train.mean(axis=0)
            self.process_u_std = self.process_outputs_train.std(axis=0)
            self.mpc_u_mean = self.mpc_outputs_train.mean(axis=0)
            self.mpc_u_std = self.mpc_outputs_train.std(axis=0)

        elif self.output_scaling == "min-max":
            self.process_u_min = self.process_outputs_train.min(axis=0)
            self.process_u_max = self.process_outputs_train.max(axis=0)
            self.mpc_u_min = self.mpc_outputs_train.min(axis=0)
            self.mpc_u_max = self.mpc_outputs_train.max(axis=0)

        # Load process metrics
        self.metrics_process = pd.read_csv(self.results_dir + f"models/experiment/hp_metrics.csv")
        self.process_best_model_id = 121
        self.process_best_model_filename = f"run_{self.process_best_model_id:03d}.keras"
        self.process_best_params = self.metrics_process[self.metrics_process["run_id"] == int(self.process_best_model_id)]
        self.process_P = self.process_best_params.iloc[0, 1]
        self.process_Q = self.process_best_params.iloc[0, 2]

        # Load process model
        self.process_model = load_model(
            self.results_dir + f"models/experiment/best/{self.process_best_model_filename}"
        )

        self.opt = Adam(learning_rate=self.process_best_params["lr"])
        self.process_model.compile(optimizer=self.opt, loss=mean_squared_error)

        # Load process metrics
        self.metrics_mpc = pd.read_csv(self.results_dir + f"models/mpc/hp_metrics.csv")
        self.mpc_best_model_id = 25
        self.mpc_best_model_filename = f"run_{self.mpc_best_model_id:03d}.keras"
        self.mpc_best_params = self.metrics_mpc[self.metrics_mpc["run_id"] == int(self.mpc_best_model_id)]
        self.mpc_P = self.mpc_best_params.iloc[0, 1]
        self.mpc_Q = self.mpc_best_params.iloc[0, 2]

        # Load mpc model
        self.mpc_model = load_model(
            self.results_dir + f"models/mpc/best/{self.mpc_best_model_filename}"
        )

        self.opt = Adam(learning_rate=self.mpc_best_params["lr"])
        self.mpc_model.compile(optimizer=self.opt, loss=mean_squared_error)

        # Define MPC parameters
        self.M = self.process_P  # control horizon
        self.N = self.process_Q  # prediction horizon
        self.weight_control = 1.0
        self.weight_output = 1.0

        # Desired outputs
        self.y_ref = np.zeros(1)

        # Historic data
        self.process_u_hist = np.zeros((self.process_P, 1))
        self.process_y_hist = np.zeros((self.process_Q, 1))

        self.mpc_u_hist = np.zeros((self.mpc_P, 1))
        self.mpc_y_hist = np.zeros((self.mpc_Q, 1))

        self.u_forecast = np.random.normal(loc=0.5, scale=0.05, size=(self.M, 1)) #

        # ROSPY Parameters
        rospy.init_node("mpc_node", anonymous=True)
        rospy.Subscriber("y", Float32, self.callback)
        self.pub = rospy.Publisher("u", Float32, queue_size=10)
        self.pub_freq = 30  # sampling frequency of published data
        self.step_time = 1 / self.pub_freq
        self.total_steps = 10
        self.rate = rospy.Rate(self.pub_freq)

    # Callback method
    def callback(self, data):
        rospy.loginfo("Received output y: %f", data.data)
        y_row = data.data
        t = time.time()
        self.y.append([t-start_time, y_row])
        if self.output_scaling == 'min-max':
            y_row_scaled = (y_row - self.process_y_min) / (self.process_y_max - self.process_y_min)
        elif self.output_scaling == 'mean-std':
            y_row_scaled = (y_row - self.process_y_mean) / self.process_y_std
        self.process_y_hist = self.update_hist(self.process_y_hist, y_row_scaled.reshape((1, 1)))
        self.mpc_y_hist = self.update_hist(self.mpc_y_hist, (self.y_ref - y_row_scaled).reshape((1, 1)))

    # Load experiment method
    def load_experiment(self, idxs_train, idxs_test):
        inputs_train = []
        outputs_train = []
        inputs_test = []
        outputs_test = []
        
        for idx_train in idxs_train:
            filename_train = f"experiment/bead{idx_train}"
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
            filename_test = f"experiment/bead{idx_test}"
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

    def load_mpc(self):
        input_train = pd.read_csv(self.data_dir + "mpc/input_train.csv").to_numpy()
        output_train = pd.read_csv(self.data_dir + "mpc/output_train.csv").to_numpy()
        input_test = pd.read_csv(self.data_dir + "mpc/input_test.csv").to_numpy()
        output_test = pd.read_csv(self.data_dir + "mpc/output_test.csv").to_numpy()
        
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
        return np.hstack((u, y)).reshape((1, 1 * (P + Q), 1))

    def split_sequence(self, seq):
        seq = seq.reshape((1 * (self.process_P + self.process_Q),))
        u = seq[: 1 * self.process_P].reshape((self.process_P, 1))
        y = seq[1 * self.process_P :].reshape((self.process_Q, 1))
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

        if self.input_scaling == 'min-max':
            output_error = (self.y_ref - y_forecast) * (self.process_y_max-self.process_y_min)
        elif self.input_scaling == 'mean-std':
            output_error = (self.y_ref - y_forecast) * self.process_y_std

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
                    output_tensor = self.process_model(input_tensor)
                    gradient = t.gradient(
                        output_tensor[:, j], input_tensor
                    ).numpy()[0, :, 0]

                input_gradient, _ = self.split_sequence(gradient)
                if i < self.process_P - 1:
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

        if self.input_scaling == 'min-max':
            output_error = (self.y_ref - y_forecast) * (self.process_y_max-self.process_y_min)
        elif self.input_scaling == 'mean-std':
            output_error = (self.y_ref - y_forecast) * self.process_y_std      
              
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
    def optimization_function(self, u_hist, y_hist, lr, u_forecast=None):
        if u_forecast is None:
            u_forecast = np.random.normal(loc=0.5, scale=0.05, size=(self.M, 1)) #
        s = 0
        cost = np.inf
        last_cost = cost
        delta_cost = -cost
        gradient_hist = np.zeros((self.process_input_test.shape[0],self.M)) # gradient history for adaptive learning rate algorithm
        while delta_cost < -self.cost_tol:
            steps, y_forecast = self.compute_step(u_hist, y_hist, u_forecast, lr)
            cost = self.cost_function(u_forecast, y_forecast)
            delta_cost = cost - last_cost
            gradient_hist[s, :] = steps[:,0]
            ada_grad = np.sqrt(np.sum(gradient_hist[:s+1,:]**2,axis=0)+1e-10).reshape((self.M, 1))
            print(f"Opt step: {s+1}")
            print(f"Cost: {cost}\n ")
            if delta_cost < 0:
                u_forecast += (-lr/ada_grad)*steps
                u_forecast = np.clip(u_forecast, a_min=0.0, a_max=1.0)
                lr = lr * (1.0 - self.alpha_opt)
                last_cost = cost
                s += 1
            else:
                print("Passed optimal solution")
                break
        u_opt = u_forecast[0, :]
        self.u_forecast[:-1 ] = u_forecast[1:]
        u_opt = u_opt[0]
        self.process_u_hist = self.update_hist(self.process_u_hist, u_opt.reshape((1, 1)))    
        print(f"u_opt_scaled: {u_opt}")
        if self.output_scaling == 'min-max':
            u_opt = u_opt * (self.process_u_max - self.process_u_min) + self.process_u_min
        elif self.output_scaling == 'mean-std':
            u_opt = u_opt * self.process_u_mean + self.process_u_std
        print(f"u_opt: {u_opt}")
        return u_opt, y_forecast, last_cost

    def mpc_prediction(self):
        input_seq = self.build_sequence(self.mpc_u_hist, self.mpc_y_hist)
        input_tensor = tf.convert_to_tensor(input_seq, dtype=tf.float32)
        u_pred = self.mpc_model(input_tensor).numpy()[0,0]
        print(f"u_pred_scaled: {u_pred}")
        self.mpc_u_hist = self.update_hist(self.mpc_u_hist, u_pred.reshape((1, 1)))
        if self.output_scaling == 'min-max':
            u_pred = u_pred * (self.mpc_u_max - self.mpc_u_min) + self.mpc_u_min
        if self.output_scaling == 'mean-std':
            u_pred = u_pred * self.process_u_mean + self.process_u_std
        print(f"u_pred: {u_pred}")
        return u_pred
    
start_time = time.time()
# Create an instance of the MPC class
mpc = MPC()

# MPC loop
exp_time = 0
exp_step = 1
while not rospy.is_shutdown():
    print(f"Time step: {exp_step}")
    for i in range(10):
        rospy.wait_for_message('y', Float32)
    u_opt, y_forecast, cost = mpc.optimization_function(mpc.process_u_hist, mpc.process_y_hist, mpc.lr, mpc.u_forecast)
    u_pred = mpc.mpc_prediction()
    u_selected = u_opt
    mpc.u.append(u_selected)
    
    # Send the "u_row" variable
    mpc.pub.publish(u_selected)
    rospy.loginfo("Sending control u: %f", u_selected)
    mpc.rate.sleep()
    exp_step += 1
    exp_time = mpc.step_time
    mpc.lr = mpc.lr * (1.0 - mpc.alpha_time)
    
rospy.spin()

