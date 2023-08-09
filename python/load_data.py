import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load data
data_dir = 'C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/database/'
X = pd.read_csv(data_dir + 'train_inputs.csv')
Y = pd.read_csv(data_dir + 'train_outputs.csv')

# Process database
scaler = StandardScaler()
for col in Y.columns:
    arr = Y[col].to_numpy().reshape(-1, 1)
    Y[col] = scaler.fit_transform(arr)

# Export Data
data = pd.DataFrame(columns=list(X.columns) + list(Y.columns))
data[X.columns] = X
data[Y.columns] = Y

data.to_csv(data_dir + 'train_data.csv')