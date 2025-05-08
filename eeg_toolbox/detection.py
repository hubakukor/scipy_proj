import numpy as np
from scipy.signal import stft, find_peaks

def detect_graphoelements(data, sfreq, bands, duration_sec = 60):
    stop_sample = int(duration_sec * sfreq)
    nperseg = int(1.0 * sfreq)
    noverlap = int(0.9 * sfreq)
    results = []
    
    for c_index in range(data.shape[0]):
        eeg = data[c_index, :stop_sample]
        f, t_stft, Zxx = stft(eeg, fs=sfreq, nperseg=nperseg, noverlap=noverlap)
        power = np.abs(Zxx)
        low_band_energy = np.sum(power[(f >= 3) & (f <= 8), :], axis = 0)
        threshold = np.percentile(low_band_energy, 95)
        peaks, _ = find_peaks(low_band_energy, height=threshold)
        
        for peak_id in peaks:
            window_power = power[:, peak_id]
            band_energies = {
                band: np.sum(window_power[(f >= fmin) & (f < fmax)])
                for band, (fmin, fmax) in bands.items()
            }
            dominant = max(band_energies, key=band_energies.get)
            results.append({
                "channel_index": c_index,
                "time_sec": t_stft[peak_id],
                "energy_3_8Hz": low_band_energy[peak_id],
                "dominant_rhythm": dominant,
                **band_energies
                })
    return results