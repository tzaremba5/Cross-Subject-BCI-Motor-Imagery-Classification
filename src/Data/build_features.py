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

# load_competition
#
# For all competitions, subjects it Loads all the corresponding epochs,
# generates features, and saves them to out_path_task
#
# Input: Competition
# Output: None
#
def load_competition(competition):

	cwd = os.getcwd()

	for subject in competitions[competition]['subjects']:

		# Makes the directory to store the features
		out_path_dir = os.path.join(cwd, 'features', competition, subject)
		try:
			os.makedirs(out_path_dir)
		except:
			pass

		# Loads in the epochs
		epochs_path = os.path.join(cwd, 'epochs', f'{competition}', f'{subject}.pk1')
		infile = open(epochs_path, 'rb')
		epochs = pickle.load(infile)

		# Picks the 12 channels for MI classification
		twelve_channels = ['C1','C2','C3','C4','C5','C6','CP3','CP4',
		'Cz','FC3','FC4','Fz']
		epochs = epochs.pick_channels(twelve_channels, ordered = True)

		# Generates the STFT representations
		for task in epochs.event_id.keys():
			epochs_task = epochs[task].get_data()
			STFT = STFT_Stacked(epochs_task)

			out_path_task = os.path.join(out_path_dir, f'{task}.pk1')

			# Removes all representation data from previous runs
			try:
				os.remove(out_path_task)
			except:
				pass

			# Saves them
			STFT_file = open(out_path_task, 'wb')
			pickle.dump(STFT, STFT_file)



if __name__ == '__main__':

	for competition in ['IV_IIa', 'IV_I', 'III_IVa']:
		load_competition(competition)

















