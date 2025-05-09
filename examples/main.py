import matplotlib.pyplot as plt
import numpy as np
from eeg_toolbox.load import load_edf_data
from eeg_toolbox.fourier_of_data import data_fourier
from eeg_toolbox.processing import notch_filter


data, ch_names, sfreq = load_edf_data('PN00-1.edf')


# Processing steps
data = notch_filter(data, fs = sfreq, filter_freq=50)
#data = resample_data(data, sfreq, new_sfreq = 100)
#data = bandpass_filter(data, freq=sfreq, lowcut=50, highcut=150, order=5)

ft_magnitudes, mean_fft = data_fourier(data)

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

# Plot mean FFT spectrum
freqs = np.fft.fftfreq(data.shape[1], 1 / sfreq)
plt.plot(freqs[:len(freqs)//2], mean_fft[:len(freqs)//2])
plt.title("Mean FFT Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.ylim(0, 1)
plt.grid(True)
plt.tight_layout()
plt.show()