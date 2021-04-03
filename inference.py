from tensorflow.python.keras.models import load_model
from pylsl import StreamInlet, resolve_stream, StreamInfo, StreamOutlet, IRREGULAR_RATE
import matplotlib.pyplot as plt

import numpy as np

def main():
    model = load_model('')
    print("looking for an EEG stream...")
    streams = resolve_stream('name', 'NER_2015_BCI_Challenge_Samples')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])
    # Pred stream
    info_pred = StreamInfo('NER_2015_BCI_Challenge_PRED', 'PRED', 1, IRREGULAR_RATE, 'string', 'PREDID')
    outlet_pred = StreamOutlet(info_pred)
    while True:
        sample = np.empty((0, 56))
        timestamps = []
        while len(sample) < 2001:
            chunk, ts = inlet.pull_chunk()
            if ts:
                ts = timestamps + ts
                sample = np.concatenate([sample, chunk], axis=0)
        pred = model.predict(np.expand_dims(sample, axis=0))
        if pred[0] <= 0.5:
            outlet_pred.push_sample(['PRED-Correct'])
        else:
            outlet_pred.push_sample(['PRED-Incorrect'])


if __name__ == '__main__':
    main()


