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
X_train, Y_train, X_test, Y_test = load_data()
Y_train, Y_test = normalize_data(Y_train, Y_test)

X_train = X_train[:1000, :]
Y_train = Y_train[:1000, :]
X_test = X_test[:1000, :]
Y_test = Y_test[:1000, :]

inputs_seq_len = 50  # hp
outputs_seq_len = 50  # hp
sequence_length = inputs_seq_len + outputs_seq_len
sequence_stride = 1
dim_inputs = X_train.shape[1]
dim_outputs = Y_train.shape[1]
X_train_seq, Y_train_seq = sequence_data(
    X_train, Y_train, inputs_seq_len, outputs_seq_len, sequence_stride)
X_test_seq, Y_test_seq = sequence_data(
    X_test, Y_test, inputs_seq_len, outputs_seq_len, sequence_stride)

# Define model

# Number of features in the input time series
num_features_input = X_train.shape[1]
# Number of features in the output time series
num_features_output = Y_train.shape[1]
model = Sequential()
model.add(LSTM(units=64, activation='relu', input_shape=(
    sequence_length, num_features_input)))
# model.add(TimeDistributed(Dense(units=Y_train_seq.shape[-1])))
model.add(Dense(units=num_features_output))

# Compile the model
lr = 1e-4  # hp
model.compile(optimizer=Adam(learning_rate=lr), loss=mean_squared_error)

# Display model summary
model.summary()

# Train the model
batch_size = 32  # hp
epochs = 150  # hp
validation_split = 0.1   # hp
history = model.fit(X_train_seq, Y_train_seq, batch_size=batch_size,
                    epochs=epochs, validation_split=validation_split)  # fit data

train_loss = history.history['loss']
val_loss = history.history['val_loss']

# Predict with model
