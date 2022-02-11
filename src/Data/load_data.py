################################################################################
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
import mne
import scipy

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
	raw.pick_channels(['Fz', 'FC3', 'FC1', 'FCz', 'FC2', 'FC4', 'C5', 'C3',
		'C1', 'Cz', 'C2', 'C4', 'C6', 'CP3', 'CP1', 'CPz', 'CP2', 'CP4',
		'P1', 'Pz', 'P2'], ordered = True)

	# Downsamples to 250 Hz
	raw_data.resample(250)

	# Common average referencing
	mne.set_eeg_reference(raw_data, ref_channels='average', copy = False)

	# Surface Laplacian Filter
	raw_data.set_montage('standard_1020')
	mne.preprocessing.compute_current_source_density(raw_data, sphere='auto',
		lambda2=1e-05, stiffness=4, n_legendre_terms=50, copy=False)

	# Bandpass filter between .5 Hz and 100 Hz 
	raw_data.filter(.5, 100., fir_window='hamming')

	# Segment data into epochs
	all_events, all_event_id = mne.events_from_annotations(raw_data)
	epochs = mne.Epochs(raw = raw_data, tmin = 0, tmax= 3.5, events = all_events,
		event_id=event_dict, event_repeated = 'merge', baseline = (None, None), 
		preload = True)

	return epochs

# save_subject_epochs
# 
# Stores the epochs for a subject
#
# Input: MNE Epochs Object, Path to store the epochs
# Output: None
#
def save_subject_epochs(epochs, path):

	# Clears any previous epochs
	try:
		os.remove(out_path_subject)
	except:
		pass

	# Creates and fills file to store epochs
	outfile = open(out_path_subject, 'wb')
	pickle.dump(epochs, outfile)
	outfile.close()

# load_BCI_Competition_IV_Dataset_IIa
#
# Loads in the data, prepreprocesses and saves it to out_path
# Input: IV_IIa_path, out_path
# Output: None
#
def load_BCI_Competition_IV_Dataset_IIa(IV_IIa_path, out_path):
	# Makes the directory to store the epochs
	try:
		os.makedirs(out_path)
	except:
		pass

	for subject in competitions['IV_IIa']['subjects']:

		# Loads in a subject's data and their labels
		raw = mne.io.read_raw_gdf(os.path.join(IV_IIa_path, f'{subject}T.gdf',
		 preload = True))
		raw_E = mne.io.read_raw_gdf(os.path.join(IV_IIa_path, f'{subject}E.gdf',
		 preload = True))
		labels = scipy.io.loadmat(os.path.join(IV_IIa_path, f'{subject}E.mat'))

		# Labels the eval data
		eval_description = raw_E.annotations.description
		eval_labels = labels['classlabel']

		description_dict = {1 : '769', 2 : '770', 3 : '771', 4 : '772'}
		j = 0
		for i in range(eval_description.shape[0]):
			if eval_description[i] == '783':
				eval_description[i] = description_dict[eval_labels[j][0]]
				j += 1

		eval_annotations = mne.Annotations(raw_E.annotations.onset,
			raw_E.annotations.duration, eval_description)

		# Merges the two datasets into one
		raw.append(raw_E)

		# Renames the channels to the standard 10-20 labels
		channel_names = {'EEG-Fz' : 'Fz', 'EEG-0' : 'FC3', 'EEG-1' : 'FC1',
		'EEG-2' : 'FCz', 'EEG-3' : 'FC2', 'EEG-4' : 'FC4', 'EEG-5' : 'C5',
		'EEG-C3' : 'C3', 'EEG-6' : 'C1', 'EEG-Cz' : 'Cz', 'EEG-7' : 'C2',
		'EEG-C4' : 'C4', 'EEG-8' : 'C6', 'EEG-9' : 'CP3', 'EEG-10' : 'CP1',
		'EEG-11' : 'CPz', 'EEG-12' : 'CP2', 'EEG-13' : 'CP4', 'EEG-14' : 'P1',
		'EEG-Pz' : 'Pz', 'EEG-15' : 'P2', 'EEG-16' : 'POz' }
		mne.rename_channels(info = raw.info, mapping = channel_names,
			allow_duplicates=False, verbose=None)

		# Preprocesses the raw data
		epochs = preprocess_pipeline(raw_EEG = raw)

		# Saves the epochs
		out_path_subject = os.path.join(out_path, f'{subject}.pk1')
		save_subject_epochs(epochs, out_path_subject)

# load_BCI_Competition_IV_Dataset_I
#
# Loads in the data, prepreprocesses and saves it to out_path
# Input: IV_I_path, out_path
# Output: None
#
def load_BCI_Competition_IV_Dataset_I(IV_I_path, out_path):
	# Makes the directory to store the epochs
	try:
		os.makedirs(out_path)
	except:
		pass

	for subject in competitions['IV_I']['subjects']:

		# Loads in a subject's data and their labels
		data = scipy.loadmat(os.path.join(folder,
			f'BCICIV_calib_ds1{subject}_1000Hz'))
		eval_data = scipy.loadmat(os.path.join(folder, 
			f'BCICIV_eval_ds1{subject}_1000Hz.mat'))
		labels = scipy.loadmat(os.path.join(folder,
			f'BCICIV_eval_ds1{subject}_1000Hz_true_y.mat'))

		# creates the raw objects
		info = mne.create_info(ch_names = [ch_name[0] for ch_name in data['nfo']['clab'][0][0][0]],
			sfreq = 1000, ch_types='eeg')
		raw = mne.io.RawArray(data['cnt'].T, info = info, first_samp=0,
			copy='auto', verbose=None)
		raw_E = mne.io.RawArray(eval_data['cnt'].T, info = info, first_samp=0,
			copy='auto', verbose=None)

		onset = data['mrk']['pos'][0][0][0] / 1000
		duration = np.array([[1] * 200]).reshape(200,)
		description = data['mrk'][0][0][1][0]
		raw.annotations.append(onset = onset, duration = duration,
			description = description)

		# Labels the evaluation data
		true_y = labels['true_y']
		onset_E = []
		labels_E = []

		for i in range(1, true_y.shape[0]):
			if (true_y[i][0] != true_y[i-1][0] and not np.isnan(true_y[i])
				and true_y[i][0] in description):
				onset_E.append(i)
				labels_E.append(int(true_y[i][0]))

		# Merges the two datasets into one
		onset_E = np.array(onset_E) / 1000
		duration_E = np.array([[1] * len(onset_E)]).reshape(len(onset_E))
		description_E = np.array(labels_E)
		raw_E.annotations.append(onset = onset_E, duration = duration_E,
			description = description_E)
		raw.append(raw_E)

		# Preprocesses the raw data
		epochs = preprocess_pipeline(raw_EEG = raw)

		# Saves the epochs
		out_path_subject = os.path.join(out_path, f'{subject}.pk1')
		save_subject_epochs(epochs, out_path_subject)

# load_BCI_Competition_IV_Dataset_IIa
#
# Loads in the data, prepreprocesses and saves it to out_path
# Input: III_IVa_path, out_path
# Output: None
#
def load_BCI_Competition_III_Dataset_IVa(III_IVa_path, out_path):
	# Makes the directory to store the epochs
	try:
		os.makedirs(out_path)
	except:
		pass

	for subject in competitions['III_IVa']['subjects']:

		# Loads in a subject's data and their labels
		data = scipy.io.loadmat(os.path.join(folder, 
			f'data_set_IVa_a{subject}.mat'))
		labels = scipy.io.loadmat(os.path.join(folder, 
			f'true_labels_a{subject}.mat'))

		# Creates the raw object 
		info = mne.create_info(ch_names = [ch_name[0] for ch_name in data['nfo']['clab'][0][0][0]],
			sfreq = 1000, ch_types='eeg')
		raw = mne.io.RawArray(data['cnt'].T, info = info, first_samp=0,
			copy='auto', verbose=None)

		# Creates and attacthes the annotations to the raw object
		onset = data['mrk']['pos'][0][0][0] / 1000
		duration = np.array([[1] * 280]).reshape(280,)
		description = labels['true_y'][0]
		raw.annotations.append(onset = onset, duration = duration,
			description = description)

		# Preprocesses the raw data
		epochs = preprocess_pipeline(raw_EEG = raw)

		# Saves the epochs
		out_path_subject = os.path.join(out_path, f'{subject}.pk1')
		save_subject_epochs(epochs, out_path_subject)

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
	out_path = os.path.join(cwd, '{}')

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

