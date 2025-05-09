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
Download the example notebook demo.ipynb and the example data file PN00-1.edf from examples folder in the repository.
The notebook can be run in Google Colab after uploading the data file and the notebook.

Authors: Veronika Szabolcsi, Dorka Kecskés, Huba Kukor
