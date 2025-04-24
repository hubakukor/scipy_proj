import mne
import numpy as np

def load_data(path):

    X = []
    Y = []
    raw = mne.io.read_raw_edf(path) #load files
    events, extracted_event_id = mne.events_from_annotations(raw)
    epochs = mne.Epochs(events, extracted_event_id)

    X.append(epochs)
    X = np.concatenate(X, axis=0)

    return X

