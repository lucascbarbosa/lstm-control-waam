import pandas as pd
import numpy as np

from sklearn.neighbors import KNeighborsRegressor

import matplotlib.pyplot as plt
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

def create_model(
    n_neighbors,
    weights,
    algorithm,
    leaf_size, 
    p
):
    knn_model = KNeighborsRegressor(n_neighbors=n_neighbors, 
                                    weights=weights, 
                                    algorithm=algorithm,
                                    leaf_size=leaf_size,
                                    p=p
                                    )
    return knn_model

def train_model(
    model,
    X_train,
    Y_train,
):
    model.fit(X_train, Y_train)
    return model

def predict_data(model, X_test, verbose=0):
    # Predict with model
    Y_pred = model.predict(X_test)
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