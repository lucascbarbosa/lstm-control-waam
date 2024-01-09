import numpy as np
import pandas as pd

from python.process_data import sequence_data

import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam

# Data paths
data_dir = f"/home/lbarbosa/Documents/Github/lstm-control-waam/database/"
results_dir = "/home/lbarbosa/Documents/Github/lstm-control-waam/results/"

# Functions
def update_hist(current_hist, new_states):
    new_hist = current_hist.copy()
    len_new = new_states.shape[0]
    new_hist[:-len_new, :] = current_hist[len_new:, :]
    new_hist[-len_new:, :] = new_states
    return new_hist

def build_sequence():
    u = u_hist.ravel()
    y = y_hist.ravel()
    return np.hstack((u, y)).reshape((1, P + Q, 1))

# Model parameters
metrics = pd.read_csv(results_dir + f"models/experiment_igor/hp_metrics.csv")
best_model_id = 121
best_model_filename = f"run_{best_model_id:03d}.keras"
best_params = metrics[metrics["run_id"] == int(best_model_id)]
P = best_params.iloc[0, 1]
Q = best_params.iloc[0, 2]

# Load model
model = load_model(
    results_dir + f"models/experiment_igor/best/{best_model_filename}"
)

opt = Adam(learning_rate=best_params["lr"])
model.compile(optimizer=opt, loss=mean_squared_error)

# Create steps
input_data = np.ones((100, 1))
initial_delay = 1
input_data[:initial_delay, 0] = 0

# Historic data
u_hist = np.zeros((P, 1))
y_hist = np.zeros((Q, 1))

output_data = []
for i in range(input_data.shape[0]):
    u = input_data[i]
    u_hist = update_hist(u_hist, u.reshape(1,1))
    input_seq = build_sequence()
    input_tensor = tf.convert_to_tensor(input_seq, dtype=tf.float32)
    y = model(input_tensor).numpy()
    y_hist = update_hist(y_hist, y)
    output_data.append(y[0,0])
