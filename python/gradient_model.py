import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Reshape
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam

import matplotlib.pyplot as plt
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

def create_model(
    num_features_input,
    num_features_output,
    lr,
    random_seed=None,
    summary=True,
):
    if random_seed:
        tf.random.set_seed(random_seed)
    model = Sequential()
    model.add(
        Dense(num_features_input * num_features_output,
              activation="relu",
              input_shape=(num_features_input+num_features_output, ),)
    )

    # Compile the model
    model.compile(optimizer=Adam(learning_rate=lr), loss=mean_squared_error)
    # Display model summary
    if summary:
        model.summary()
    return model

def train_model(
    model,
    X_train,
    Y_train,
    batch_size,
    num_epochs,
    validation_split,
    verbose=0,
):
    history = model.fit(
        X_train,
        Y_train,
        batch_size=batch_size,
        epochs=num_epochs,
        validation_split=validation_split,
        verbose=verbose,
    )  # fit data
    return model, history


def predict_data(model, X_test, verbose=0):
    # Predict with model
    Y_pred = model.predict(X_test, verbose=verbose)
    return Y_pred

def plot_loss(history):
    fig, axs = plt.subplots(2, 1, figsize=(8, 6))
    keys = list(history.history.keys())
    titles = ["Treino", "Validação"]
    for i, ax in enumerate(axs):
        ax.plot(history.history[keys[i]], label=keys[i])
        ax.set_xlabel("Epoch")
        ax.set_ylabel("Erro")
        ax.set_title(titles[i])

    plt.show()
