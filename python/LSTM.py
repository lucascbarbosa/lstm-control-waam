import pandas as pd
import numpy as np

from load_data import load_data, normalize_data, sequence_data

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, TimeDistributed
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# Load data
X_train, Y_train = load_data()
Y_train = normalize_data(Y_train)

sequence_length = 100
sequence_stride = 50
dim_inputs = X_train.shape[1]
dim_outputs = Y_train.shape[1]
X_train_seq, Y_train_seq = sequence_data(
    X_train, Y_train, sequence_length, sequence_stride)

# Define model
# Number of features in the input time series
num_features_input = X_train.shape[1]
# Number of features in the output time series
num_features_output = Y_train.shape[1]
model = Sequential()
model.add(LSTM(units=64, activation='relu', input_shape=(
    sequence_length, X_train_seq.shape[-1]), return_sequences=True))
# model.add(TimeDistributed(Dense(units=Y_train_seq.shape[-1])))
model.add(Dense(units=Y_train_seq.shape[-1]))

# Compile the model
lr = 1e-4  # hp
model.compile(optimizer=Adam(learning_rate=lr), loss=mean_squared_error)

# Display model summary
model.summary()

# Train the model
batch_size = 32  # hp
epochs = 1000  # hp
validation_split = 0.1   # hp
history = model.fit(X_train_seq, Y_train_seq, batch_size=batch_size,
                    epochs=epochs, validation_split=validation_split)  # fit data
