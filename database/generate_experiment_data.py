from scipy.io import loadmat
import numpy as np
import pandas as pd

data_dir = "database/"

train_data = loadmat(data_dir + f'experiment/experiment_train.mat')
wfs_df = pd.DataFrame()
wfs_df['t'] = train_data['powersource_state_time'].ravel()
wfs_df['wfs'] = train_data['wfs'].ravel()
wfs_df.to_csv(data_dir + f'experiment/input_train.csv', index=False)

w_df = pd.DataFrame()
w_df['t'] = train_data['width_f_time'].ravel()
w_df['w'] = train_data['width_f_array'].ravel()
w_df.to_csv(data_dir + f'experiment/output_train.csv', index=False)

test_data = loadmat(data_dir + f'experiment/experiment_test.mat')
wfs_df = pd.DataFrame()
wfs_df['t'] = test_data['powersource_state_time'].ravel()
wfs_df['wfs'] = test_data['wfs'].ravel()
wfs_df.to_csv(data_dir + f'experiment/input_test.csv', index=False)

w_df = pd.DataFrame()
w_df['t'] = test_data['width_f_time'].ravel()
w_df['w'] = test_data['width_f_array'].ravel()
w_df.to_csv(data_dir + f'experiment/output_test.csv', index=False)
