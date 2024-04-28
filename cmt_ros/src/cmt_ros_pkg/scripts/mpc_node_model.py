import tensorflow as tf
from keras.models import load_model
import joblib

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

import rospy
from std_msgs.msg import Float32, Bool, Float64MultiArray
import time
import control


class MPC:
    def __init__(self, bead_idx):

        self.bead_idx = bead_idx

        # Optimization parameters
        self.lr = 1e-1
        self.alpha_time = 1e-3
        self.alpha_opt = 1e-3
        self.cost_tol = 1e-2

        # ROSPY Parameters
        rospy.init_node("mpc_node", anonymous=True)
        rospy.Subscriber("arc_state", Bool, self.callback_arc)
        self.arc_state = False
        rospy.Subscriber("xiris/bead/filtered", Float32, self.callback_width)
        rospy.Subscriber("powersource_state", Float32, self.callback_power)
        rospy.Subscriber("kr90/travel_speed", Float32, self.callback_ts)
        self.pub = rospy.Publisher(
            "fronius_remote_command", Float32, queue_size=10)
        self.pub_freq = 10  # sampling frequency of published data
        self.step_time = 1 / self.pub_freq
        self.total_steps = 10
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

    def callback_ts(self, data):
        ts = data.data
        # rospy.loginfo("Received TS %f", ts)
        self.ts = (ts - self.process_u_min[1]) / \
            (self.process_u_max[1] - self.process_u_min[1])

    def callback_power(self, data):
        p = data.data
        # rospy.loginfo("Received power %f", p)
        f = self.pow2wfs(p)
        self.f = (f - self.process_u_min[0]) / \
            (self.process_u_max[0] - self.process_u_min[0])
        new_u = np.array([[self.f, self.ts]])
        self.u_hist = self.update_hist(self.u_hist, new_u)

    def callback_width(self, data):
        if self.arc_state:
            current_time = time.time() - start_time
            y_row = data.data
            # rospy.loginfo("Received output w: %f", y_row)
            y_row_scaled = (y_row - self.process_y_min) / \
                (self.process_y_max - self.process_y_min)
            self.y_hist = self.update_hist(
                self.y_hist, y_row_scaled.reshape((1, 1)))

    # Optimization function method
    def optimization_function(self, u_hist, y_hist, lr, u_forecast=None, verbose=False):
        opt_time = time.time()
        if u_forecast is None:
            # u_forecast = np.random.normal(loc=0.5, scale=0.05, size=(self.M, 1)) #
            u_forecast = np.random.uniform(size=(self.M, 1))
        opt_step = 0
        cost = np.inf
        last_cost = cost
        delta_cost = -cost
        # gradient_hist = np.zeros((self.process_input_test.shape[0],self.M)) # gradient history for adaptive learning rate algorithm
        gradient_hist = []  # gradient history for adaptive learning rate algorithm
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
        u_opt = u_forecast[0, :]
        u_opt = u_opt[0]
        u_opt = self.wfs2pow(u_opt)
        self.pub.publish(u_opt)
        rospy.loginfo("Sending control wfs: %f", u_opt)
        opt_time = time.time() - opt_time
        print(f"Steps: {opt_step} Time: {opt_time:.2f}")
        self.list_performance_opt.append(
            {'Steps': opt_step, 'Time': opt_time, 'Cost': last_cost, 'Converged': converged})
        return u_opt, u_forecast, y_forecast

    def export_gradient(self):
        np.savetxt(results_dir + "predictions/gradient/gradient_reals.csv",
                   np.array(self.gradient_reals))
        np.savetxt(results_dir + "predictions/gradient/gradient_preds.csv",
                   np.array(self.gradient_preds))

    def export_performance(self):
        performance_df = pd.DataFrame(self.list_performance_opt)
        performance_df.to_csv(
            results_dir +
            f'mpc_performance/gradient_{self.gradient_source}.csv', index=False)


# Filepaths
data_dir = f"/home/lbarbosa/Documents/Github/lstm-control-waam/database/"
results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"


# Create an instance of the MPC class
bead_idx = 1
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
            mpc.u_hist,
            mpc.y_hist,
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

mpc.export_performance()
if mpc.gradient_source == 'both':
    mpc.export_gradient()
rospy.spin()
