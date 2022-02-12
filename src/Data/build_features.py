################################################################################
# build_features.py
#
# Loads in the epochs generated from the epochs_path
#
# WARNING: this file will save the STFT features
#

# Imports
import os
import pickle
import numpy as np
import scipy
import mne

# STFT_stacked
#
# Takes the epochs and generates all the STFT representations
#
# Input: MNE Epochs array
# Output: List of numpy arrays containing the features
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

# load_competition
#
# Loads all the epochs for a gvien competition, generates features, and saves
# them
#
# Input: Competition
# Output: None
#
def load_competition(competition):
	for subject in competitions[competition]['subjects']:
		epochs_path = os.path.join(cwd, 'epochs', f'{competition}', f'{subject}.pk1')

		twelve_channels = ['C1','C2','C3','C4','C5','C6','CP3','CP4',
		'Cz','FC3','FC4','Fz']

		infile = open(epochs_path, 'rb')
		epochs = pickle.load(infile)

		epochs = epochs.pick_channels(twelve_channels, ordered = True)

		out_path = os.path.join(cwd, 'features', competition, subject)

		# Makes the outpath to store the features
		try:
			os.makedirs(out_path)
		except:
			pass


if __name__ == '__main__':
	epochs_path = os.path.join(cwd, 'epochs', '{}')

	cwd = os.getcwd()

	for competition in ['IV_IIa', 'IV_I', 'III_IVa']:

















