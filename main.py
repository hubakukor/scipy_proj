from load import load_edf_data
import matplotlib.pyplot as plt
import numpy as np

# path to the EDF file
edf_path = r"D:\downloads\PN00-1.edf"

data, ch_names, sfreq = load_edf_data(edf_path)

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