import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, TimeDistributed
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import plot_model

import matplotlib.pyplot as plt
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

#############
# Filepaths #
# data_dir = 'C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/database/'
# results_dir = 'C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/results/'

#############
# Functions #


def create_model(sequence_length, num_features_input, num_features_output, random_seed=None, summary=True):
    if random_seed:
        tf.random.set_seed(random_seed)
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


def train_model(model, X_train_seq, Y_train_seq, batch_size, epochs, validation_split):
    history = model.fit(X_train_seq, Y_train_seq, batch_size=batch_size,
                        epochs=epochs, validation_split=validation_split)  # fit data
    return model, history


def predict_data(model, X_test_seq):
    # Predict with model
    Y_pred_seq = model.predict(X_test_seq)
    return Y_pred_seq


def plot_loss(history):
    fig, axs = plt.subplots(2, 1, figsize=(8, 6))
    keys = list(history.history.keys())
    titles = ['Treino', 'Validação']
    for i, ax in enumerate(axs):
        ax.plot(history.history[keys[i]], label=keys[i])
        ax.set_xlabel('Epoch')
        ax.set_ylabel('Erro')
        ax.set_title(titles[i])

    plt.show()


# # Load data
# X_train, Y_train, X_test, Y_test = load_data(data_dir)
# num_features_input = X_train.shape[1]
# num_features_output = Y_train.shape[1]

# # Slice to fit sequencing
# X_train = X_train[:1000, :]
# Y_train = Y_train[:1000, :]
# X_test = X_test[:1000, :]
# Y_test = Y_test[:1000, :]

# Y_train = normalize_data(Y_train)
# Y_test = normalize_data(Y_test)

# # Sequencing
# inputs_seq_len = 50  # hp (P)
# outputs_seq_len = 50  # hp (Q)
# sequence_length = inputs_seq_len + outputs_seq_len
# forecast_h = 50  # hp (H)
# X_train, Y_train = sequence_data(
#     X_train, Y_train, inputs_seq_len, outputs_seq_len, forecast_h)
# X_test, Y_test = sequence_data(
#     X_test, Y_test, inputs_seq_len, outputs_seq_len, forecast_h)
# y_means = Y_test.mean(axis=0)
# y_stds = Y_test.std(axis=0)

# # Define model
# model = create_model(num_features_input, num_features_output)

# # Training
# batch_size = 32  # hp
# epochs = 100  # hp
# validation_split = 0.1   # hp
# model, history = train_model(
#     model, X_train, Y_train, batch_size, epochs, validation_split)

# # Train loss
# plot_loss(history)

# # Prediction
# Y_pred = predict_data(model, X_test)
# for i in range(num_features_output):
#     Y_pred[:, i] = denormalize_data(
#         Y_pred[:, i], y_means[i], y_stds[i])  # Denormalize

#     Y_test[:, i] = denormalize_data(
#         Y_test[:, i], y_means[i], y_stds[i])  # Denormalize

# # Export prediction data
# save = True
# if save:
#     np.savetxt(results_dir+'y_real.csv', Y_test)
#     np.savetxt(results_dir+'y_pred.csv', Y_pred)
