.. EEG Toolbox documentation master file, created by
   sphinx-quickstart on Thu May  8 17:59:03 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

EEG Toolbox documentation
=========================

This toolbox provides EEG data loading, filtering, normalization,
visualization, detection of EEG bands and Fourier analysis.

Source code available at `https://github.com/hubakukor/scipy_proj`.

A demo notebook showcasing the toolbox is available at `https://github.com/hubakukor/scipy_proj/blob/master/examples/demo.ipynb`.


Introduction
-------
eeg_toolbox is a standardized Python toolkit for processing, analyzing, and visualizing long-term EEG signals. The package allows for the preprocessing of raw EEG data (filtering, resampling), extraction of time-frequency-based features (FFT, STFT), and automatic detection of abnormal brain activity (graphoelements).
The algorithms use open-format EDF files as input and provide a transparent, modular way to evaluate clinically relevant patterns derived from EEG data. The methods used for detection (e.g., spectral peak analysis, frequency band-based dominance) enable the temporal localization and classification of slow waves and unusual activities.
As a result, the package offers a reliable, customizable, and easily expandable solution for analyzing EEG signals for research and educational purposes.

Installation
-------
Install with ``pip install git+https://github.com/hubakukor/scipy_proj.git``

Requirements
-------
Python == 3.10

scipy==1.15.2

matplotlib==3.10.1

mne==1.9.0

numpy==2.2.5

The required libraries are automatically downloaded with the PIP install.

Description
-------

.. image:: figure.png
   :alt: Example pipeline
   :width: 400px

The following steps are implemented in the EEG processing toolbox:

Loading EEG data
~~~~~~~~~~
The toolbox supports the loading of EEG signals from .edf (European Data Format) files using the mne library. The raw data is returned in NumPy array format along with the sampling frequency and channel names, enabling further processing and analysis.

Preprocessing
~~~~~~~~~~
The toolbox includes basic preprocessing methods such as:
  - *Resampling*: EEG data can be resampled to a new target sampling frequency.
  - *Filtering*: Bandpass filtering and notch filtering are supported to remove noise, such as powerline interference and unwanted frequency components.
  - *Normalization*: Z-score, min-max normalization, and mean centering can be applied on a per-channel basis to standardize the signals for analysis.

Spectral Analysis
~~~~~~~~~~
Using the Fourier transform, the toolbox computes the frequency spectrum of EEG signals. It also calculates the average power spectrum across channels to facilitate interpretation of dominant rhythms and spectral characteristics.

Event Detection
~~~~~~~~~~
A method is provided to detect graphoelements (distinctive EEG patterns) using short-time Fourier transform (STFT). The detection focuses on elevated energy in the 3–8 Hz band and identifies dominant rhythms (e.g., theta or delta waves) based on energy across predefined frequency bands.

Visualization
~~~~~~~~~~
Multiple visualization utilities are included:
  - *EEG overview plotting*: Time-domain plots of selected EEG channels.
  - *FFT spectrum plotting*: Visualization of the mean power spectrum.
  - *Event segment plotting*: Graphical display of EEG segments around detected graphoelements, highlighting their temporal and rhythmic context.

This toolbox is intended to support lightweight, scriptable EEG analysis pipelines for research and prototyping, particularly in scenarios where standard EDF EEG files are used as input.

.. image:: grapho_elements.png
   :alt: Example pipeline
   :width: 400px

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Authors: Veronika Szabolcsi, Dorka Kecskés, Huba Kukor