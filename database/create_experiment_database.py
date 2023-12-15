from scipy.io import loadmat
import numpy as np
import pandas as pd

data_dir = "database/"

for idx_bead in range(1, 8):
    bead_data = loadmat(data_dir + f'experiment/bead{idx_bead}.mat')
    wfs_df = pd.DataFrame()
    wfs_df['t'] = bead_data['powersource_state_time'].ravel()
    wfs_df['wfs'] = bead_data['wfs'].ravel()
    wfs_df.to_csv(data_dir + f'experiment/bead{idx_bead}_wfs.csv', index=False)

    w_df = pd.DataFrame()
    w_df['t'] = bead_data['width_f_time'].ravel()
    w_df['w'] = bead_data['width_f_array'].ravel()
    w_df.to_csv(data_dir + f'experiment/bead{idx_bead}_w.csv', index=False)
    