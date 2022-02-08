######################################################################
# load_data.py
#
# Loads in the data from BCI Competition IV Dataset IIa, BCI 
# Competition IV Dataset I, and BCI Competition III Dataset IVa
#
# WARNING: this file will save the preprocessed EEG data
#

# Imports
import argparse
import os

# preprocess_pipeline
#
# Preprocesses the EEG data by
# - picking the 21 common channels
# - downsamples to 250 Hz
# - common average referencing
# - surface laplacian
# - bandpass filter (0.5 - 100 Hz)
# - segment the data into epochs
#
# Input: MNE Raw Object
# Output: MNE Epochs Object
#
def preprocess_pipeline(raw_EEG):

	# Picks 21 Common Channels
	raw.pick_channels(['Fz', 'FC3', 'FC1', 'FCz', 'FC2', 'FC4', 'C5',
		'C3', 'C1', 'Cz', 'C2', 'C4', 'C6', 'CP3', 'CP1', 'CPz', 
		'CP2', 'CP4', 'P1', 'Pz', 'P2'], ordered = True)

	# Downsamples to 250 Hz
	raw_data.resample(250)

	# Common average referencing
	mne.set_eeg_reference(raw_data, ref_channels='average', 
		copy = False)

	# Surface Laplacian Filter
	raw_data.set_montage('standard_1020')
	mne.preprocessing.compute_current_source_density(raw_data,
		sphere='auto', lambda2=1e-05, stiffness=4,
		n_legendre_terms=50, copy=False)

	# Bandpass filter between .5 Hz and 100 Hz 
	raw_data.filter(.5, 100., fir_window='hamming')

	# Segment data into epochs
	all_events, all_event_id = mne.events_from_annotations(raw_data)
	epochs = mne.Epochs(raw = raw_data, 
		tmin = 0, tmax= 3.5, events = all_events, event_id=event_dict, 
		event_repeated = 'merge', baseline = (None, None), 
		preload = True)

	return epochs

# load_BCI_Competition_IV_Dataset_IIa
#
# Loads in the data, prepreprocesses and saves it to out_path
# Input: IV_IIa_path, out_path
# Output: None
#
def load_BCI_Competition_IV_Dataset_IIa(IV_IIa_path, out_path):
	print(IV_IIa_path)
	print(out_path)

# load_BCI_Competition_IV_Dataset_I
#
# Loads in the data, prepreprocesses and saves it to out_path
# Input: IV_I_path, out_path
# Output: None
#
def load_BCI_Competition_IV_Dataset_I(IV_I_path, out_path):
	print(IV_I_path)

# load_BCI_Competition_IV_Dataset_IIa
#
# Loads in the data, prepreprocesses and saves it to out_path
# Input: III_IVa_path, out_path
# Output: None
#
def load_BCI_Competition_III_Dataset_IVa(III_IVa_path, out_path):
	print(III_IVa_path)

if __name__ == '__main__':
	# Gets the name of the directories to load the raw data 
	# and save the preprocessed data
	parser = argparse.ArgumentParser(description='Load Data')
	parser.add_argument('IV_IIa_path', nargs = 1, 
		help='BCI Competition IV Dataset IIa raw path or $ to skip')
	parser.add_argument('IV_I_path', nargs = 1, 
		help='BCI Competition IV Dataset I raw path or $ to skip')
	parser.add_argument('III_IVa_path', nargs = 1,
	 help='BCI Competition III Dataset IVa raw path or $ to skip')
	args = parser.parse_args()

	# Sets the out_path to store all the preprocessed data
	cwd = os.getcwd()
	out_path = os.path.join(cwd, '{competition}')

	# Loads all the competition data, stores the preprocessed data
	if args.IV_IIa_path[0] != '$':
		load_BCI_Competition_IV_Dataset_IIa(args.IV_IIa_path[0], 
			out_path.format(competition = "IV_IIa"))
	if args.IV_I_path[0] != '$':	
		load_BCI_Competition_IV_Dataset_I(args.IV_I_path[0],
			out_path.format(competition = "IV_I"))
	if args.III_IVa_path[0] != '$':
		load_BCI_Competition_III_Dataset_IVa(args.III_IVa_path[0],
			out_path.format(competition = "III_IVa"))
