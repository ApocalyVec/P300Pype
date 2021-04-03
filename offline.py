from multiprocessing import pool

import mne
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

root = 'E:/inria-bci-challenge/train/'
train_label_location = 'E:/inria-bci-challenge/TrainLabels.csv'
files = [os.path.join(root, fn) for fn in os.listdir(root)]

n_channels = 59
n_eeg_channels = 56
array_eeg = np.empty((0, n_channels))

tmin = -10.

for i, fn in enumerate(files):
    print('Loading {0} of {1} session files'.format(i + 1, len(files)))
    df = pd.read_csv(fn)

    # change this to your path
    array_eeg = np.concatenate([array_eeg, df.values], axis=0)

array_eeg_copy = np.copy(array_eeg)
array_prediction = np.expand_dims(pd.read_csv(train_label_location)['Prediction'].values, axis=-1)
array_prediction[array_prediction == 1] = 2  # 2 is correct
array_prediction[array_prediction == 0] = 1  # 1 is correct
array_eeg_copy[:, -1][np.argwhere(array_eeg_copy[:, -1])] = array_prediction

mne_raw = mne.io.RawArray(array_eeg_copy.transpose(), mne.create_info(['Time'] + ['eeg'] * n_eeg_channels + ['eog', 'stim'], 200, ch_types=['misc'] + ['eeg'] * n_eeg_channels + ['eog', 'stim']))
mne_raw, _ = mne.set_eeg_reference(mne_raw, 'average', projection=False)
mne_raw = mne_raw.filter(l_freq=0.1, h_freq=15)  # bandpass filter

mne_events = mne.find_events(mne_raw, ['stim'])

epochs_params = dict(events=mne_events, event_id=[2], tmin=tmin, tmax=0.)
evoked_correct = mne.Epochs(raw=mne_raw, **epochs_params)
evoked_correct_ave = evoked_correct.average()

epochs_params = dict(events=mne_events, event_id=[1], tmin=tmin, tmax=0.)
evoked_incorrect = mne.Epochs(raw=mne_raw, **epochs_params)
evoked_incorrect_ave = evoked_incorrect.average()

# fig = evoked_correct_ave.plot(gfp=True, spatial_colors=True, ylim=dict(eeg=[-30, 20]), titles=dict(eeg=title), scalings=dict(eeg=1.))
fig = evoked_correct_ave.plot(gfp=True, spatial_colors=True, ylim=dict(eeg=[-5, 10]), titles=dict(eeg='Correct'), scalings=dict(eeg=1.))
fig = evoked_incorrect_ave.plot(gfp=True, spatial_colors=True, ylim=dict(eeg=[-5, 10]),   titles=dict(eeg='Incorrect'), scalings=dict(eeg=1.))

# classifier
array_correct = evoked_correct.get_data()
array_incorrect = evoked_incorrect.get_data()
array_all = np.concatenate([array_correct, array_incorrect], axis=0)
label_all = np.concatenate([np.zeros(len(array_correct)), np.ones(len(array_incorrect))])

np.save( 'data', array_all)
np.save( 'label', label_all)


