from load import load_edf_data
from fourier_of_data import data_fourier
import matplotlib.pyplot as plt
import numpy as np

# path to the EDF file
edf_path = r"C:\Users\Kecskés Dorka\Documents\Pazmany\Scientific Python\PN00-1.edf"

data, ch_names, sfreq = load_edf_data(edf_path)

ft_magnitudes, mean_fft = data_fourier(data)

np.info(data) #show information about the loaded data

print(f"Channel names: {ch_names}")

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