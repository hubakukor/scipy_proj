# EEG Toolbox

eeg_toolbox is a standardized Python toolkit for processing, analyzing, and visualizing long-term EEG signals. The package allows for the preprocessing of raw EEG data (filtering, resampling), extraction of time-frequency-based features (FFT, STFT), and automatic detection of abnormal brain activity (graphoelements).
The algorithms use open-format EDF files as input and provide a transparent, modular way to evaluate clinically relevant patterns derived from EEG data. The methods used for detection (e.g., spectral peak analysis, frequency band-based dominance) enable the temporal localization and classification of slow waves and unusual activities.
As a result, the package offers a reliable, customizable, and easily expandable solution for analyzing EEG signals for research and educational purposes.


Documentation: https://scipy-proj.readthedocs.io/en/latest/index.html

Source code: https://github.com/hubakukor/scipy_proj

## Installation

```bash
pip install eeg_toolbox
```

## Example Usage

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hubakukor/scipy_proj/blob/master/examples/demo.ipynb)

Click on the Colab button above to open the demo notebook in Google Colab, or download the example notebook demo.ipynb and the example data file PN00-1.edf from the [examples](https://github.com/hubakukor/scipy_proj/tree/master/examples) folder in the repository.
The notebook can be run in Google Colab after uploading the data file and the notebook.


## Description
The following steps are implemented in the EEG processing toolbox:

### Loading EEG data

The toolbox supports the loading of EEG signals from .edf (European Data Format) files using the mne library. The raw data is returned in NumPy array format along with the sampling frequency and channel names, enabling further processing and analysis.

### Preprocessing

The toolbox includes basic preprocessing methods such as:
  - *Resampling*: EEG data can be resampled to a new target sampling frequency.
  - *Filtering*: Bandpass filtering and notch filtering are supported to remove noise, such as powerline interference and unwanted frequency components.
  - *Normalization*: Z-score, min-max normalization, and mean centering can be applied on a per-channel basis to standardize the signals for analysis.

### Spectral Analysis

Using the Fourier transform, the toolbox computes the frequency spectrum of EEG signals. It also calculates the average power spectrum across channels to facilitate interpretation of dominant rhythms and spectral characteristics.

### Event Detection

A method is provided to detect graphoelements (distinctive EEG patterns) using short-time Fourier transform (STFT). The detection focuses on elevated energy in the 3–8 Hz band and identifies dominant rhythms (e.g., theta or delta waves) based on energy across predefined frequency bands.

### Visualization

Multiple visualization utilities are included:
  - *EEG overview plotting*: Time-domain plots of selected EEG channels.
  - *FFT spectrum plotting*: Visualization of the mean power spectrum.
  - *Event segment plotting*: Graphical display of EEG segments around detected graphoelements, highlighting their temporal and rhythmic context.

Authors: Veronika Szabolcsi, Dorka Kecskés, Huba Kukor
