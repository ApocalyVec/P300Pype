from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout
import sys
from pylsl import StreamInfo, StreamOutlet, local_clock, IRREGULAR_RATE, resolve_stream, StreamInlet
import numpy as np

pred_ts_list = []
em_ts_list = []

def ticks():
    pred_sample, pred_ts = pred_inlet.pull_sample(timeout=0.)
    em_sample, em_ts = em_inlet.pull_sample(timeout=0.)

    if pred_ts:
        print('PD received is ' + str(pred_sample))
        pred_ts_list.append(pred_ts + pred_inlet.time_correction())
        pred_msg.setText('<h1>Predicts {0}% Incorrect</h1>'.format(round(np.average(pred_sample) * 100, 2)))
    if em_ts:
        em_ts_list.append(em_ts)
        print('EM received is ' + str(em_sample))
        em_msg.setText('<h1>EM: {0}</h1>'.format(str(em_sample)))
    latency = np.abs(np.average(pred_ts_list) - np.average(em_ts_list))
    delay_msg.setText('<h1>Average prediction latency: {0} sec</h1>'.format(round(latency, 2)))

pred_streams = resolve_stream('name', 'NER_2015_BCI_Challenge_PRED')
pred_inlet = StreamInlet(pred_streams[0])

em_streams = resolve_stream('name', 'NER_2015_BCI_Challenge_EM')
em_inlet = StreamInlet(em_streams[0])

# create a simple window to display the classification results
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Inference Results')
window.setGeometry(100, 100, 360, 240)

pred_msg = QLabel('<h1>Predicts </h1>', parent=window)
em_msg = QLabel('<h1>True marker is </h1>', parent=window)
delay_msg = QLabel('<h1>Average prediction latency is</h1>', parent=window)

layout = QVBoxLayout()
layout.addWidget(pred_msg)
layout.addWidget(em_msg)
layout.addWidget(delay_msg)
window.setLayout(layout)
# lsl to the true label
# take in the predition results

# timer
timer = QTimer()
timer.setInterval(1)  # for 1000 Hz refresh rate
timer.timeout.connect(ticks)
timer.start()

window.show()
sys.exit(app.exec_())


#
# if __name__ == '__main__':
#     main()
