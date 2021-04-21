import numpy as np

import mne

from pyriemann.estimation import Covariances
from pyriemann.tangentspace import TangentSpace

from sklearn.pipeline import make_pipeline
from sklearn.model_selection import KFold
from sklearn.ensemble import BaggingClassifier
from sklearn.svm import SVC
from sklearn.metrics import roc_curve, auc, classification_report, plot_confusion_matrix, plot_roc_curve
from sklearn.model_selection import train_test_split

from imblearn.over_sampling import SMOTE

from matplotlib import pyplot as plt


data = np.load('data.npy')
data = data[:, 1:57, :]
labels = np.load('label.npy')

sm = SMOTE(random_state=42)
orig_shape = data.shape
data_two_dim = np.reshape(data, (orig_shape[0], orig_shape[1]*orig_shape[2]))

data, labels = sm.fit_resample(data_two_dim, labels)

data_train, data_test, labels_train, labels_test = \
    train_test_split(data, labels, test_size=0.3, random_state=42)
data_train = np.reshape(data_train, (labels_train.shape[0], orig_shape[1], orig_shape[2]))
data_test = np.reshape(data_test, (labels_test.shape[0], orig_shape[1], orig_shape[2]))


'''
np.save('data_balanced_train.npy', data_train)
np.save('labels_balanced_train.npy', labels_train)

np.save('data_test.npy', data_test)
np.save('labels_test.npy', labels_test)
'''

'''
data_train = np.load('data_balanced_train.npy')
labels_train = np.load('labels_balanced_train.npy')
data_test = np.load('data_test.npy')
labels_test = np.load('labels_test.npy')
'''

n_eeg_channels = 56
epochs = mne.EpochsArray(data_train,
                         mne.create_info(['eeg'] * n_eeg_channels, 200, ch_types=['eeg'] * n_eeg_channels))
epochs_test_mne = mne.EpochsArray(data_test,
                         mne.create_info(['eeg'] * n_eeg_channels, 200, ch_types=['eeg'] * n_eeg_channels))

# K-Fold cross validation generator
cv = KFold(n_splits=10, shuffle=True, random_state=42)
epochs_train = epochs.get_data()
epochs_test = epochs_test_mne.get_data()
clf = make_pipeline(Covariances('oas'),
                    TangentSpace(metric='riemann'),
                    BaggingClassifier(SVC(), n_estimators=10, random_state=0, n_jobs=64))

tprs = []
aucs = []
mean_fpr = np.linspace(0, 1, 100)
preds = np.zeros(len(labels_train))
plt.figure(1)
fig, ax = plt.subplots()
for i, (train_idx, test_idx) in enumerate(cv.split(epochs_train)):
    y_train, y_test = labels_train[train_idx], labels_train[test_idx]
    clf.fit(epochs_train[train_idx], y_train)

    viz = plot_roc_curve(clf, epochs_train[test_idx], y_test,
                         name=f"ROC fold {i}", alpha=0.3, lw=1, ax=ax)
    interp_tpr = np.interp(mean_fpr, viz.fpr, viz.tpr)
    interp_tpr[0] = 0.0
    tprs.append(interp_tpr)
    aucs.append(viz.roc_auc)

    epoch_pred = epochs_train[test_idx]
    preds[test_idx] = clf.predict(epoch_pred)

ax.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r', label='Chance', alpha=0.8)
mean_tpr = np.mean(tprs, axis=0)
mean_tpr[-1] = 1.
mean_auc = auc(mean_fpr, mean_tpr)
std_auc = np.std(aucs)

std_tpr = np.std(tprs, axis=0)
tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
ax.fill_between(mean_fpr, tprs_lower, tprs_upper,
                color='grey', alpha=0.2,
                label=f'+= 1 std. dev.')
ax.set(xlim=[0.05, 1.05], ylim=[-0.05, 1.05],
       title="ROC Training", xlabel='False Positive Rate', ylabel='True Positive Rate')
ax.legend(loc="lower right")
plt.show()

preds_train = clf.predict(epochs_train)
print("Training Set Report")
print(classification_report(labels_train, preds_train))

#plot_confusion_matrix(clf, epochs_test, labels_test)
#plt.show()

preds_test = clf.predict(epochs_test)
print("Test Set Report")
print(classification_report(labels_test, preds_test))

num_classes = 2
fpr = {}
tpr = {}
roc_auc = {}
for i in range(num_classes):
    fpr[i], tpr[i], _ = roc_curve(labels_test, preds_test, pos_label=1.)
    roc_auc[i] = auc(fpr[i], tpr[i])

fpr["micro"], tpr["micro"], _ = roc_curve(labels_test.ravel(), preds_test.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

plt.figure(2)
lw = 2
plt.plot(fpr["micro"], tpr["micro"], color='darkorange', lw=lw,
         label=f'ROC curve (area = {roc_auc["micro"]})')
plt.plot([0,1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC')
plt.legend(loc="lower right")
plt.show()
