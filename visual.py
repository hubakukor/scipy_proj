import mne
from load import load_edf_data
from fourier_of_data import data_fourier
import matplotlib.pyplot as plt
import numpy as np

edf_path = r"C:\Users\veron\scipy_project\scipy_proj-1\PN00-1.edf"

data, ch_names, sfreq = load_edf_data(edf_path)

ft_magnitudes, mean_fft = data_fourier(data)

np.info(data)

times = np.arange(data.shape[1]) / sfreq
#plt.plot(times, data[0])
#plt.title(f"Channel {ch_names[0]}")
#plt.xlabel("Time (s)")
#plt.ylabel("Amplitude (µV)")
#plt.tight_layout()
#plt.show()

# plot the first 5 channel with vertical offset
plt.figure(figsize=(14, 6))
offset = 100 # microvolt offset for visibility
scale_factor = 1e6  # convert from Volts to μV if needed
data = data * scale_factor

for i in range(5):
    plt.plot(times, data[i] + i * offset, label=ch_names[i])

plt.xlabel("Time (s)")
plt.ylabel("Amplitude + Offset (µV)")
plt.title("EEG Channels")
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()

freqs = np.fft.fftfreq(data.shape[1], 1 / sfreq)
plt.plot(freqs[:len(freqs)//2], mean_fft[:len(freqs)//2])
plt.title("Mean FFT Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.ylim(0, 1)
plt.grid(True)
plt.tight_layout()
plt.show()