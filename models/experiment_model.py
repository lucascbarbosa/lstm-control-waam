import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras.optimizers import Adam


def create_model(
    P,
    Q,
    num_features_input,
    num_features_output,
    lr,
    random_seed=None,
    summary=True,
):
    """
    Create process model.

    Args:
        sequence_length (int): length of sequence input
        num_features_input (int): input dimension
        num_features_output (int): output dimension
        lr (float): learning rate
        random_seed (int): random seed for initialization of model weights
        summary (float): wheather or not print model summary

    Returns:
        model (Sequential): process model

    """
    input_sequence_length = P * num_features_input + Q * num_features_output
    if random_seed:
        tf.random.set_seed(random_seed)
    model = Sequential()
    model.add(
        Dense(
            units=num_features_output,
            input_shape=(input_sequence_length, ))
    )
    # Compile the model
    model.compile(optimizer=Adam(learning_rate=lr), loss=mean_squared_error)

    # Display model summary
    if summary:
        model.summary()
    return model


def train_model(
    model,
    X_train_seq,
    Y_train_seq,
    batch_size,
    epochs,
    validation_split,
    verbose=0,
):
    """
    Train process model

    Args:
        model (Sequential): tf model to be trained
        batch_size (int): size of batch of training
        epochs (int): number of epochs of training
        validation_split (float): percentage of train dataset used for validation during training
        verbose (int): verbosity level of training

    Returns:
        model (Sequential): trained model
        history (dict): history of training metrics
    """
    history = model.fit(
        X_train_seq,
        Y_train_seq,
        batch_size=batch_size,
        epochs=epochs,
        validation_split=validation_split,
        verbose=verbose,
    )  # fit data
    return model, history


def predict_data(model, X_test_seq, verbose=0):
    """
    Predict database using trained model

    Args:
        model (Sequential): trained model
        X_test_seq (np.array): inputs of test dataset
        verbose (int): verbosity level of prediction

    Returns:
        Y_pred_seq (np.array): predicted outputs
    """
    # Predict with model
    Y_pred_seq = model.predict(X_test_seq, verbose=verbose)
    return Y_pred_seq


def plot_loss(history):
    """
    Plot loss of training

    Args:
        history (dict): history of training metrics

    Returns:

    """
    fig, axs = plt.subplots(2, 1, figsize=(8, 6))
    keys = list(history.history.keys())
    titles = ["Treino", "Validação"]
    for i, ax in enumerate(axs):
        ax.plot(history.history[keys[i]], label=keys[i])
        ax.set_xlabel("Epoch")
        ax.set_ylabel("Erro")
        ax.set_title(titles[i])

    plt.show()
