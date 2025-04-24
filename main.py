from load import load_data

edf_path = r"D:\downloads\PN00-1.edf"


X = load_data(edf_path)

# raw = mne.io.read_raw_edf(edf_path, preload=True)
# print(raw.info)