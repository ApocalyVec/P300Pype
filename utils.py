import mne
import pandas as pd
import numpy as np

def get_layout_from_file(file_path):
    df = pd.read_csv(file_path)
    rho, phi = df.iloc[:, 2].values, df.iloc[:, 3].values
    xy_coord = np.array([rho * np.cos(phi * np. pi/180), rho * np.sin(phi * np. pi/180)]).transpose()
    return list(df.iloc[:, 1].values), mne.channels.generate_2d_layout(xy_coord, ch_names=df.iloc[:, 1].values)
