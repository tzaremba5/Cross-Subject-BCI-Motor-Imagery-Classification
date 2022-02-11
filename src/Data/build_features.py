################################################################################
# build_features.py
#
# Loads in the epochs generated from 
#

# STFT_stacked
#
#
def STFT_stacked(epochs):
	num_samples = epochs.shape[0]
	num_channels = epochs.shape[1]

	samples = []
	for e in range(num_samples):
		stacked = []
		for c in range(num_channels):
			STFT = scipy.signal.spectrogram(epochs[e][c], fs=250, window='hann',
				nperseg=250, noverlap=225, nfft=500, scaling='spectrum')[2][16:61]
			stacked.append(STFT)
		samples.append(np.vstack(stacked))

	return samples

def create_features(competition_path, out_path):



if __name__ == '__main__':
	epochs_path = os.path.join(cwd, 'epochs', '{}')

	cwd = os.getcwd()
	out_path = cwd

	for competition in ['IV_IIa', 'IV_I', 'III_IVa']:
		build

	out_path = os.path.join(cwd, '{}')