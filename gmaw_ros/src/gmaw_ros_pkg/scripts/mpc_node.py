import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
from sklearn.neighbors import KNeighborsRegressor
import joblib

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

import rospy
from std_msgs.msg import Float32, Bool, Float64MultiArray

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

        # Process data
        (self.process_input_train, 
         self.process_output_train, 
         self.process_input_test, 
         self.process_output_test) = self.load_experiment_igor([1, 2, 3, 4, 5, 6], [7])
        
        # (self.process_input_train, 
        #  self.process_output_train, 
        #  self.process_input_test, 
        #  self.process_output_test) = self.load_experiment([1, 2, 3, 4, 5, 6], [7])

        self.process_input_scaling = "min-max"
        self.process_output_scaling = "min-max"
        if self.process_output_scaling == "mean-std":
            self.process_y_mean = self.process_output_train.mean(axis=0)
            self.process_y_std = self.process_output_train.std(axis=0)

        elif self.process_output_scaling == "min-max":
            self.process_y_min = self.process_output_train.min(axis=0)
            self.process_y_max = self.process_output_train.max(axis=0)

        if self.process_input_scaling == "mean-std":
            self.process_u_mean = self.process_input_train.mean(axis=0)
            self.process_u_std = self.process_input_train.std(axis=0)

        elif self.process_input_scaling == "min-max":
            self.process_u_min = self.process_input_train.min(axis=0)
            self.process_u_max = self.process_input_train.max(axis=0)

        # Load process model metrics
        self.metrics_process = pd.read_csv(self.results_dir + \
                                           f"models/experiment_igor/hp_metrics.csv"
                                           )
        process_best_model_id = 121
        process_best_model_filename = f"run_{process_best_model_id:03d}.keras"
        self.process_best_params = self.metrics_process[
            self.metrics_process["run_id"] == int(process_best_model_id)
            ]
        self.P = self.process_best_params.iloc[0, 1]
        self.Q = self.process_best_params.iloc[0, 2]

        # Load process model
        self.process_model = load_model(
            self.results_dir + \
            f"models/experiment_igor/best/{process_best_model_filename}"
        )

        self.opt = Adam(learning_rate=self.process_best_params["lr"])
        self.process_model.compile(optimizer=self.opt, loss=mean_squared_error)
        
        # Gradient data
        (self.gradient_input_train,
         self.gradient_output_train,
         _, 
         _) = self.load_gradient()
        self.gradient_output_scaling = "mean-std"
        if self.gradient_output_scaling == "mean-std":
            self.gradient_y_mean = self.gradient_output_train.mean(axis=0)
            self.gradient_y_std = self.gradient_output_train.std(axis=0)

        elif self.gradient_output_scaling == "min-max":
            self.gradient_y_min = self.gradient_output_train.min(axis=0)
            self.gradient_y_max = self.gradient_output_train.max(axis=0)
        
        # Load gradient model metrics
        self.gradient_source = "knn"
        self.metrics_gradient = pd.read_csv(self.results_dir + f"models/gradient_{self.gradient_source}/hp_metrics.csv")
        if self.gradient_source == "knn":
            gradient_best_model_id = 357
            gradient_best_model_filename = f"run_{gradient_best_model_id:03d}.pkl"
            self.gradient_model = joblib.load(self.results_dir + 
                f"models/gradient_{self.gradient_source}/best/{gradient_best_model_filename}"
            )
        elif self.gradient_source == "model":
            gradient_best_model_id = 78
            gradient_best_model_filename = f"run_{gradient_best_model_id:03d}.keras"
            self.gradient_best_params = self.metrics_gradient[self.metrics_gradient["run_id"] == int(gradient_best_model_id)]
            # Load gradient model
            self.gradient_model = load_model(
                self.results_dir + f"models/gradient_{self.gradient_source}/best/{gradient_best_model_filename}"
            )

            self.opt = Adam(learning_rate=self.gradient_best_params["lr"])
            self.gradient_model.compile(optimizer=self.opt, loss=mean_squared_error)

        # Define MPC parameters
        self.M = self.P  # control horizon
        self.N = self.Q  # prediction horizon
        self.weight_control = 1.0
        self.weight_output = 1.0

        # Desired outputs
        self.y_ref = self.process_output_test[-1:].mean(axis=0)
        if self.process_input_scaling == 'min-max':
            self.y_ref = (self.y_ref - self.process_y_min) / (self.process_y_max - self.process_y_min)
        if self.process_input_scaling == 'mean-std':
            self.y_ref = (self.y_ref - self.process_y_mean) / self.process_y_std

        # Historic data
        self.u_hist = np.zeros((self.P, 1))
        self.y_hist = np.zeros((self.Q, 1))

        self.u_forecast = np.random.normal(loc=0.5, scale=0.05, size=(self.M, 1)) #

        # ROSPY Parameters
        rospy.init_node("mpc_node", anonymous=True)
        rospy.Subscriber("arc_state", Bool, self.callback_arc)
        self.arc_state = False
        rospy.Subscriber("xiris/bead/filtered", Float32, self.callback_width)
        self.pub = rospy.Publisher("fronius_remote_command", Float32, queue_size=10)
        self.pub_freq = 30  # sampling frequency of published data
        self.step_time = 1 / self.pub_freq
        self.total_steps = 10
        self.rate = rospy.Rate(self.pub_freq)

    def callback_arc(self, data):
        if not self.arc_state and bool(data.data):
            self.arcon_time = time.time()
        elif self.arc_state and not bool(data.data):
            self.export_output()
            rospy.signal_shutdown("Shutting down")
        self.arc_state = bool(data.data)

    def callback_width(self, data):
        current_time = time.time() - start_time
        y_row = data.data * int(self.arc_state)
        rospy.loginfo("Received output w: %f", y_row)
        self.y.append({'t': current_time, 'w': y_row})
        if self.process_input_scaling == 'min-max':
            y_row_scaled = (y_row - self.process_y_min) / (self.process_y_max - self.process_y_min)
        elif self.process_input_scaling == 'mean-std':
            y_row_scaled = (y_row - self.process_y_mean) / self.process_y_std
        self.y_hist = self.update_hist(self.y_hist, y_row_scaled.reshape((1, 1)))

    # Load experiment method
    def load_gradient(self):
        input_train = np.loadtxt(self.data_dir + "gradient/input_train.csv")
        output_train = np.loadtxt(self.data_dir + "gradient/output_train.csv")
        input_test = np.loadtxt(self.data_dir + "gradient/input_test.csv")
        output_test = np.loadtxt(self.data_dir + "gradient/output_test.csv")
        return input_train, output_train, input_test, output_test

    # Load experiment method
    def load_experiment(self):
        input_train = pd.read_csv(self.data_dir + "experiment/input_train.csv").to_numpy()
        output_train = pd.read_csv(self.data_dir + "experiment/output_train.csv").to_numpy()
        input_test = pd.read_csv(self.data_dir + "experiment/input_test.csv").to_numpy()
        output_test = pd.read_csv(self.data_dir + "experiment/output_test.csv").to_numpy()
        return input_train, output_train, input_test, output_test
        
    # Load experiment_igor method
    def load_experiment_igor(self, idxs_train, idxs_test):
        inputs_train = []
        outputs_train = []
        inputs_test = []
        outputs_test = []
        
        for idx_train in idxs_train:
            filename_train = f"experiment_igor/bead{idx_train}"
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
            filename_test = f"experiment_igor/bead{idx_test}"
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
    def cost_function(self, u_forecast, y_forecast):
        u_diff_forecast = self.create_control_diff(u_forecast)

        if self.process_input_scaling == 'min-max':
            output_error = (self.y_ref - y_forecast) * (self.process_y_max-self.process_y_min)
        elif self.process_input_scaling == 'mean-std':
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

                # Predict gradient
                gradient_input = tf.convert_to_tensor(
                    np.concatenate([seq_input.ravel(), output_tensor.numpy()[0]])
                    .reshape(1, self.P + self.Q + 1)
                    )
                
                gradient_pred = self.predict_gradient(gradient_input)
                print(gradient_pred)
                print(gradient)
                print('\n\n')

                # Split gradients
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

        if self.process_input_scaling == 'min-max':
            output_error = (self.y_ref - y_forecast) * (self.process_y_max-self.process_y_min)
        elif self.process_input_scaling == 'mean-std':
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
        opt_step = 0
        cost = np.inf
        last_cost = cost
        delta_cost = -cost
        # gradient_hist = np.zeros((self.process_input_test.shape[0],self.M)) # gradient history for adaptive learning rate algorithm
        gradient_hist = [] # gradient history for adaptive learning rate algorithm
        while delta_cost < -self.cost_tol:
            steps, y_forecast = self.compute_step(u_hist, y_hist, u_forecast, lr)
            cost = self.cost_function(u_forecast, y_forecast)
            delta_cost = cost - last_cost
            gradient_hist.append(steps[:,0].ravel().tolist())
            ada_grad = np.sqrt(np.sum(np.array(gradient_hist)[:opt_step+1,:]**2,axis=0)+1e-10).reshape((self.M, 1))
            print(f"Opt step: {opt_step+1} Cost: {cost}\n")
            if delta_cost < 0:
                u_forecast += (-lr/ada_grad)*steps
                u_forecast = np.clip(u_forecast, a_min=0.0, a_max=1.0)
                lr = lr * (1.0 - self.alpha_opt)
                last_cost = cost
                opt_step += 1
            else:
                print("Passed optimal solution")
                break
        u_opt = u_forecast[0, :]
        self.u_forecast[:-1 ] = u_forecast[1:]
        u_opt = u_opt[0]
        self.u_hist = self.update_hist(self.u_hist, u_opt.reshape((1, 1)))    
        if self.process_output_scaling == 'min-max':
            u_opt = u_opt * (self.process_u_max - self.process_u_min) + self.process_u_min
        elif self.process_output_scaling == 'mean-std':
            u_opt = u_opt * self.process_u_mean + self.process_u_std
        self.pub.publish(u_opt)
        rospy.loginfo("Sending control u: %f", u_opt)
        self.u.append(u_opt)
        return u_opt, y_forecast, last_cost

    def predict_gradient(self,gradient_input):
        if self.gradient_source == "model":
            gradient_pred = self.gradient_model(gradient_input).numpy().ravel()
        elif self.gradient_source == "knn":
            gradient_pred = self.gradient_model.predict(gradient_input).ravel()
        
        if self.gradient_output_scaling == 'mean-std':
            gradient_pred = gradient_pred * self.gradient_y_std + self.gradient_y_mean
        elif self.gradient_output_scaling == 'min-max':
            gradient_pred = gradient_pred * (self.gradient_y_max - self.gradient_y_min) + self.gradient_y_min

        return gradient_pred
# Create an instance of the MPC class
mpc = MPC()

# MPC loop
exp_time = 0
exp_step = 1
start_time = time.time()
rospy.wait_for_message("xiris/bead/filtered", Float32)
while not rospy.is_shutdown():
    if mpc.arc_state:
        print(f"Time step: {exp_step}")
        u_opt, y_forecast, cost = mpc.optimization_function(mpc.u_hist, mpc.y_hist, mpc.lr, mpc.u_forecast)
        
        # Send the "u_row" variable
        mpc.rate.sleep()
        exp_step += 1
        exp_time = mpc.step_time
        mpc.lr = mpc.lr * (1.0 - mpc.alpha_time)
    else:
        pass

rospy.spin()
