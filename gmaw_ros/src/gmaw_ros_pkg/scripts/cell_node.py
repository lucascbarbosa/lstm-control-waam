#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32, Header
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

def callback(data):
    u = data.data
    rospy.loginfo("Received control u: %f", u)
    input_mpc.append([u])

# def load_experiment(data_dir, idx_bead):
#     filename_train = f"bead{idx_bead}"
#     input_data = pd.read_csv(data_dir + filename_train + "_wfs.csv").to_numpy()
#     output_data = pd.read_csv(
#         data_dir + filename_train + "_w.csv"
#     ).to_numpy()

#     input_data = resample_data(
#         input_data[:, 1], input_data[:, 0], output_data[:, 0]
#     )
#     return input_data[:, 1:], output_data[:, 1:]

# def resample_data(original_data, original_time, new_time):
#     interp_func = interp1d(
#         original_time,
#         original_data,
#         kind="linear",
#         fill_value="extrapolate",
#     )
#     resampled_data = np.zeros((new_time.shape[0], 2))
#     resampled_data[:, 0] = new_time
#     resampled_data[:, 1] = interp_func(new_time)
#     return resampled_data

# data_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/database/experiment/"
# idx_bead = 2
# input_data, output_data = load_experiment(data_dir, idx_bead)
# input_mpc = []

if __name__ == '__main__':
    try:
        rospy.init_node('cell_node', anonymous=True)
        rospy.Subscriber('u', Float32, callback)
        pub = rospy.Publisher('y', Float32, queue_size=10)
        fs = 30
        rate = rospy.Rate(fs)
        t = 0
        while not rospy.is_shutdown():
            # y = output_data[t]
            y = np.random.normal()
            pub.publish(y)
            rospy.loginfo("Sending output y: %f", y)
            rate.sleep()
            rospy.wait_for_message('u', Float32)
            t += 1

    except rospy.ROSInterruptException:
        pass
