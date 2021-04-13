import os
import sys
import getopt

import time
from random import random as rand

from pylsl import StreamInfo, StreamOutlet, local_clock, IRREGULAR_RATE
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():

    # read in the files

    root = 'E:/inria-bci-challenge/train/'
    train_label_location = 'E:/inria-bci-challenge/TrainLabels.csv'
    files = [os.path.join(root, fn) for fn in os.listdir(root)]
    srate = 800

    n_channels = 56

    array_eeg = np.empty((0, n_channels))
    array_em = np.empty((0,))

    for i, fn in enumerate(files):
        print('Loading {0} of {1} session files'.format(i+1, len(files)))
        df = pd.read_csv(fn)  # change this to your path
        array_eeg = np.concatenate([array_eeg, df.iloc[:, 1:57].values], axis=0)
        array_em = np.concatenate([array_em, df.iloc[:, -1].values], axis=0)

    array_prediction = np.expand_dims(pd.read_csv(train_label_location)['Prediction'].values, axis=-1)
    array_prediction[array_prediction == 1] = 2  # 2 is correct
    array_prediction[array_prediction == 0] = 1  # 1 is correct
    array_em[np.argwhere(array_em)] = array_prediction

    # next make an outlet
    # EEG stream
    info_EEG = StreamInfo('NER_2015_BCI_Challenge_EEG', 'EEG', n_channels, srate, 'float32', 'EEGID')
    outlet_EEG = StreamOutlet(info_EEG)
    # EM stream
    info_EM = StreamInfo('NER_2015_BCI_Challenge_EM', 'EM', 1, IRREGULAR_RATE, 'string', 'EMID')
    outlet_EM = StreamOutlet(info_EM)

    array_eeg = array_eeg[7500:, :]
    array_em = array_em[7500:]

    print("now sending data...")
    start_time = local_clock()
    sent_samples = 0

    while True:
        elapsed_time = local_clock() - start_time
        required_samples = int(srate * elapsed_time) - sent_samples
        for sample_ix in range(required_samples):
            # make a new random n_channels sample; this is converted into a
            # pylsl.vectorf (the data type that is expected by push_sample)
            sample_eeg = array_eeg[0, :]

            if array_em[0] == 0.:
                pass
            elif array_em[0] == 1.:
                outlet_EM.push_sample(['S X'])
                outlet_EM.push_sample(['incorrect'])

                print('EM sent is incorrect')
            elif array_em[0] == 2.:
                outlet_EM.push_sample(['S X'])
                outlet_EM.push_sample(['correct'])

                print('EM sent is correct')
            else:
                raise Exception('Unrecognized event, this should never happen ')
            # now send it
            outlet_EEG.push_sample(sample_eeg)

            # forward the pointer
            array_em = array_em[1:]
            array_eeg = array_eeg[1:, :]


        sent_samples += required_samples
        # now send it and wait for a bit before trying again.
        time.sleep(1/srate)


if __name__ == '__main__':
    main()


# ['Fp1', 'Fp2', 'AF7', 'AF3', 'AF4', 'AF8', 'F7', 'F5', 'F3', 'F1', 'Fz', 'F2', 'F4', 'F6', 'F8', 'FT7', 'FC5', 'FC3', 'FC1', 'FCz', 'FC2', 'FC4','FC6', 'FT8', 'T7', 'C5', 'C3', 'C1', 'Cz', 'C2', 'C4', 'C6', 'T8', 'TP7', 'CP5', 'CP3', 'CP1', 'CPz', 'CP2', 'CP4', 'CP6', 'TP8', 'P7', 'P5', 'P3', 'P1', 'Pz', 'P2', 'P4', 'P6', 'P8', 'PO7', 'POz', 'P08', 'O1', 'O2']