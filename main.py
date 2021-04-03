"""Example program to demonstrate how to send a multi-channel time series to
LSL."""
import os
import sys
import getopt

import time
from random import random as rand

from pylsl import StreamInfo, StreamOutlet, local_clock
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():

    # read in the files

    root = 'E:/inria-bci-challenge/train/'
    session_num = 10
    files = [os.path.join(root, fn) for fn in os.listdir(root)]
    srate = 200
    name = 'NER_2015_BCI_Challenge'
    type = 'EEG'
    n_channels = 56

    info = StreamInfo(name, type, n_channels, srate, 'float32', 'someid')
    array_eeg = np.empty((0, n_channels))

    for i, fn in enumerate(files):
        print('Loading {0} of {1} session files'.format(i+1, min(session_num, len(files))))
        if i >= session_num:
            break
        df = pd.read_csv(fn)  # change this to your path
        array_eeg = np.concatenate([array_eeg, df.iloc[:, 1:57].values], axis=0)

    # next make an outlet
    outlet = StreamOutlet(info)

    print("now sending data...")
    start_time = local_clock()
    sent_samples = 0
    while True:
        elapsed_time = local_clock() - start_time
        required_samples = int(srate * elapsed_time) - sent_samples
        for sample_ix in range(required_samples):
            # make a new random n_channels sample; this is converted into a
            # pylsl.vectorf (the data type that is expected by push_sample)
            mysample = array_eeg[0, :]
            array_eeg = array_eeg[1:, :]
            # now send it
            outlet.push_sample(mysample)
        sent_samples += required_samples
        # now send it and wait for a bit before trying again.
        time.sleep(0.005)


if __name__ == '__main__':
    main()


# ['Fp1', 'Fp2', 'AF7', 'AF3', 'AF4', 'AF8', 'F7', 'F5', 'F3', 'F1', 'Fz', 'F2', 'F4', 'F6', 'F8', 'FT7', 'FC5', 'FC3', 'FC1', 'FCz', 'FC2', 'FC4','FC6', 'FT8', 'T7', 'C5', 'C3', 'C1', 'Cz', 'C2', 'C4', 'C6', 'T8', 'TP7', 'CP5', 'CP3', 'CP1', 'CPz', 'CP2', 'CP4', 'CP6', 'TP8', 'P7', 'P5', 'P3', 'P1', 'Pz', 'P2', 'P4', 'P6', 'P8', 'PO7', 'POz', 'P08', 'O1', 'O2']