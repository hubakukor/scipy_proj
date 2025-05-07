import matplotlib.pyplot as plt
import numpy as np
from load import load_edf_data
from fourier_of_data import data_fourier
from processing import resample_data, notch_filter, bandpass_filter
from detection import detect_graphoelements
from visual import plot_eeg_overview, plot_fft_spectrum, plot_graph_segments

# path to the EDF file
#edf_path = r"D:\downloads\PN00-1.edf"
edf_path = r"C:\Users\veron\scipy_project\scipy_proj-1\PN00-1.edf"

data, ch_names, sfreq = load_edf_data(edf_path)


# Processing steps
data = notch_filter(data, fs = sfreq, filter_freq=50.0)
#data = resample_data(data, sfreq, new_sfreq = 100)
data = bandpass_filter(data, freq=sfreq, lowcut=1.0, highcut=30.0)

fft_magnitudes, mean_fft = data_fourier(data)

np.info(data) #show information about the loaded data

print(f"Channel names: {ch_names}")
print(f"Original sampling frequency: {sfreq} Hz")



#plot the first channel
times = np.arange(data.shape[1]) / sfreq
plt.plot(times, data[0])
plt.title(f"Channel {ch_names[0]}")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (µV)")
plt.tight_layout()
plt.show()

plot_eeg_overview(data, ch_names, sfreq)
plot_fft_spectrum(mean_fft, sfreq, data.shape[1])

bands = {
    "delta": (0.5, 4),
    "theta": (4, 8),
    "alpha": (8, 13),
    "beta": (13, 30),
    "gamma": (30, 80),
}
events = detect_graphoelements(data, sfreq, bands, duration_sec=60)
print(f"Detected events: {len(events)}")

plot_graph_segments(data, sfreq, events, ch_names, window_sec=1.5, n_show=5)