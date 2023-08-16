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

#############
# Filepaths #
data_dir = 'C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/database/'
results_dir = 'C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/results/'

#############
# Functions #


def create_model(num_features_input, num_features_output, summary=True):
    model = Sequential()
    model.add(LSTM(units=64, activation='relu', input_shape=(
        sequence_length, num_features_input)))
    # model.add(TimeDistributed(Dense(units=Y_train_seq.shape[-1])))
    model.add(Dense(units=num_features_output))
    # Compile the model
    lr = 1e-4  # hp
    model.compile(optimizer=Adam(learning_rate=lr), loss=mean_squared_error)

    # Display model summary
    if summary:
        model.summary()
    return model


def train_model(model, X_train_seq, Y_train_seq, batch_size, epochs, validation_split, save_model=True):
    history = model.fit(X_train_seq, Y_train_seq, batch_size=batch_size,
                        epochs=epochs, validation_split=validation_split)  # fit data
    # Save model
    model.save(results_dir + "LSTM.h5")
    return model, history


def predict_data(model, X_test_seq):
    # Predict with model
    Y_pred_seq = model.predict(X_test_seq)
    return Y_pred_seq


# Load data
X_train, Y_train, X_test, Y_test = load_data(data_dir)
Y_train, Y_test = normalize_data(Y_train, Y_test)

# Slice to fit sequencing
X_train = X_train[:1000, :]
Y_train = Y_train[:1000, :]
X_test = X_test[:1000, :]
Y_test = Y_test[:1000, :]

# Sequencing
inputs_seq_len = 50  # hp
outputs_seq_len = 50  # hp
sequence_length = inputs_seq_len + outputs_seq_len
forecast_h = 1  # hp (H)
dim_inputs = X_train.shape[1]
dim_outputs = Y_train.shape[1]
X_train_seq, Y_train_seq = sequence_data(
    X_train, Y_train, inputs_seq_len, outputs_seq_len, forecast_h)
X_test_seq, Y_test_seq = sequence_data(
    X_test, Y_test, inputs_seq_len, outputs_seq_len, forecast_h)

# Define model
num_features_input = X_train.shape[1]
num_features_output = Y_train.shape[1]
model = create_model(num_features_input, num_features_output)

# Training
batch_size = 32  # hp
epochs = 50  # hp
validation_split = 0.1   # hp
model, history = train_model(
    model, X_train_seq, Y_train_seq, batch_size, epochs, validation_split)

train_loss = history.history['loss']
val_loss = history.history['val_loss']

Y_pred_seq = predict_data(model, X_test_seq)

print('MSE: %.3f' % mse)
# Export prediction
np.savetxt(results_dir+'y_pred_seq.csv', Y_pred_seq)
np.savetxt(results_dir+'y_test_seq.csv', Y_test_seq)
