import mne
import numpy as np


def load_edf_data(filepath):

    raw = mne.io.read_raw_edf(filepath, preload=True, verbose=False)

    data = raw.get_data()
    ch_names = raw.ch_names
    sfreq = raw.info['sfreq']

    return data, ch_names, sfreq

