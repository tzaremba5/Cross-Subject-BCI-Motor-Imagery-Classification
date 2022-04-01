################################################################################
# build_features.py
#
# Loads in the epochs generated from the epochs_path
#
# WARNING: this file will save the STFT features
#

# Imports
import os
import numpy as np
import pickle
import scipy.signal
import mne
import argparse
from dataset_descriptions import *

# STFT_stacked
#
# Takes the epochs and generates STFT representations
#
# Input: MNE Epochs array
# Output: List of numpy arrays containing the features
#
def STFT_stacked(epochs):

	num_samples = epochs.shape[0]
	num_channels = epochs.shape[1]

	# Iterates through, generating a STFT spectogram for every 1 epoch
	samples = []
	for e in range(num_samples):
		stacked = []
		for c in range(num_channels):
			STFT = scipy.signal.spectrogram(epochs[e][c], fs=250, window='hann',
				nperseg=250, noverlap=225, nfft=500, scaling='spectrum')[2][16:61]
			stacked.append(STFT)
		samples.append(np.vstack(stacked))

	return samples

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Single Trial')

	# Parameters to pick the subject
	parser.add_argument('Competition', nargs = 1, help='BCI Competition (IV_IIa, IV_I, III_IVa')
	parser.add_argument('Subject', nargs = 1, help='Subject has to be from the competition listed above')
	args = parser.parse_args()

	# Gets all the arguments
	competition = args.Competition[0]
	subject = args.Subject[0]

	assert competition in competition_names, "Enter a valid competition name"
	assert subject in competitions[competition]['subjects'], "Enter a valid subject id from the given competition"


	# Makes the directory to store the features
	out_path_dir = f'./features/{competition}/{subject}'
	try:
		os.makedirs(out_path_dir)
	except:
		pass

	# Loads in the epochs
	epochs_path = f'./epochs/{competition}/{subject}.fif'
	epochs = mne.read_epochs(fname = epochs_path, preload = True)

	# Picks the 12 channels for MI classification
	twelve_channels = ['C1','C2','C3','C4','C5','C6','CP3','CP4',
	'Cz','FC3','FC4','Fz']
	epochs = epochs.pick_channels(twelve_channels, ordered = True)

	# Generates the STFT representations
	for task in epochs.event_id.keys():
		epochs_task = epochs[task].get_data()
		STFT = STFT_stacked(epochs_task)

		out_path_task = f'{out_path_dir}/{task}.pk1'

		# Removes all representation data from previous runs
		try:
			os.remove(out_path_task)
		except:
			pass

		# Saves the features
		STFT_file = open(out_path_task, 'wb')
		pickle.dump(STFT, STFT_file)