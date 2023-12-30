#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam

def callback(data):
    u = data.data
    u_scaled = (u - u_min) / (u_max - u_min)
    u_hist = update_hist(u_hist, u_scaled)
    rospy.loginfo("Received control u: %f", u)
    input_mpc.append([u])

def load_experiment(data_dir, idxs_train, idxs_test):
    inputs_train = []
    outputs_train = []
    inputs_test = []
    outputs_test = []
    
    for idx_train in idxs_train:
        filename_train = f"bead{idx_train}"
        input_train = pd.read_csv(data_dir + filename_train + "_wfs.csv").to_numpy()
        output_train = pd.read_csv(
            data_dir + filename_train + "_w.csv"
        ).to_numpy()

        input_train = resample_data(
            input_train[:, 1], input_train[:, 0], output_train[:, 0]
        )
        inputs_train.append(input_train)
        outputs_train.append(output_train)

    inputs_train = np.concatenate(inputs_train, axis=0)
    outputs_train = np.concatenate(outputs_train, axis=0)
    
    for idx_test in idxs_test:
        filename_test = f"bead{idx_test}"
        input_test = pd.read_csv(data_dir + filename_test + "_wfs.csv").to_numpy()
        output_test = pd.read_csv(data_dir + filename_test + "_w.csv").to_numpy()

        input_test = resample_data(
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

def resample_data(original_data, original_time, new_time):
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
def update_hist(current_hist, new_states):
    new_hist = current_hist.copy()
    len_new = new_states.shape[0]
    new_hist[:-len_new, :] = current_hist[len_new:, :]
    new_hist[-len_new:, :] = new_states
    return new_hist

def build_sequence(u_hist, y_hist):
    u = u_hist.ravel()
    y = y_hist.ravel()
    return np.hstack((u, y)).reshape((1, 1 * (P + Q), 1))

data_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/database/experiment/"
results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"
input_train, output_train, _, _ = load_experiment(data_dir, [1, 2, 3, 4, 5, 6], [7])

u_min = input_train.min(axis=0)
u_max = input_train.max(axis=0)

y_mean = output_train.mean(axis=0)
y_std = output_train.std(axis=0)

metrics = pd.read_csv(results_dir + f"models/experiment/hp_metrics.csv")
best_model_id = 281
best_model_filename = f"run_{best_model_id:03d}.keras"
best_params = metrics[metrics["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

M = P
N = Q

# Load process model
model = load_model(
    results_dir + f"models/experiment/best/{best_model_filename}"
)

opt = Adam(learning_rate=best_params["lr"])
model.compile(optimizer=opt, loss=mean_squared_error)

input_mpc = []
u_hist = np.zeros((P, 1))
y_hist = np.zeros((Q, 1))

if __name__ == '__main__':
    try:
        rospy.init_node('cell_node', anonymous=True)
        rospy.Subscriber('u', Float32, callback)
        pub = rospy.Publisher('y', Float32, queue_size=10)
        fs = 10
        rate = rospy.Rate(fs)
        t = 0
        while not rospy.is_shutdown():
            y = np.random.normal()
            # input_seq = build_sequence(u_hist, y_hist)
            # input_tensor = tf.convert_to_tensor(input_seq, dtype=tf.float32)
            # y_scaled = model(input_tensor).numpy()
            # y_hist = update_hist(y_hist, y_scaled)
            # y = y_scaled * y_std + y_mean
            pub.publish(y)
            rospy.loginfo("Sending output y: %f", y)
            rate.sleep()
            # rospy.wait_for_message('u', Float32)
            t += 1

    except rospy.ROSInterruptException:
        pass
