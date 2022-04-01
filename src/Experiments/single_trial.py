################################################################################
#
# single-trial.py
#
# Runs all the single-trial (within one subject) experiments
#

import os
import pickle
import numpy as np
import argparse
import sklearn.model_selection
import keras.callbacks
import json
from results import *
from model import *
from dataset_descriptions import *
from create_datasets import *

# single_trial
#
# Runs 3 iterations of a 5-fold cross validation for each subject
# 
def single_trial(X, Y, num_classes, model_config, train_config, weights_initial_path):
	es = keras.callbacks.EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=train_config['patience'])
	model = STFTModel(num_classes, **model_config)
	model.save_weights(weights_initial_path) # Saves the empty weights rigth after the models created

	indices = []
	predictions = []
	labels = []
	for iteration in range(3):
		sss = sklearn.model_selection.StratifiedShuffleSplit(n_splits=5)
		sss.get_n_splits(X, Y)

		for train_index, test_index in sss.split(X, Y): # gets the train and test indecies
			model.load_weights(weights_initial_path) # Restores the model to the inital weights

			train_index.astype(int, copy = False)
			test_index.astype(int, copy = False)

			X_train, X_test = X[train_index], X[test_index]
			y_train, y_test = Y[train_index], Y[test_index]

			model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = train_config['epochs'], 
			batch_size = train_config['batch_size'], callbacks = [es], verbose = 1)
			fold_predictions = model.predict(X_test)

			# saves the predictions
			indices.append(X_test.tolist())
			predictions.append(fold_predictions.tolist())
			labels.append(y_test.tolist())

	r = results(predictions, labels, indices, model_config, train_config)
	return r

if __name__ == '__main__':

	#########################################
	# Gets the arguments to get the given subject

	parser = argparse.ArgumentParser(description='Single Trial')

	# Parameters to pick the subject
	parser.add_argument('Competition', nargs = 1, help='BCI Competition (IV_IIa, IV_I, III_IVa')
	parser.add_argument('Subject', nargs = 1, help='Subject has to be from the competition listed above')
	parser.add_argument('Model_Config', nargs = 1, help='Subject has to be from the competition listed above')
	parser.add_argument('Train_Config', nargs = 1, help='Subject has to be from the competition listed above')
	parser.add_argument('Config_Label', nargs = 1, help='Subject has to be from the competition listed above')

	args = parser.parse_args()

	# Gets all the arguments
	competition = args.Competition[0]
	subject = args.Subject[0]
	model_config_fname = args.Model_Config[0]
	train_config_fname = args.Train_Config[0]
	config_label = args.Config_Label[0]

	assert competition in competition_names, "Enter a competition name"
	assert subject in competitions[competition]['subjects'], "Enter a subject id from the given competition"

	# Loads in the config files
	with open(model_config_fname, 'r') as infile:
		model_config = json.loads(infile.read())

	with open(train_config_fname, 'r') as infile:
		train_config = json.loads(infile.read())

	# Runs the single-trial experiment
	X, Y, num_classes = create_dataset(competition, subject)

	# Turns them into a numpy array for the model
	X = np.array(X)
	Y = np.array(Y)

	weights_initial_path = f'./checkpoints/{competition}_{subject}_single-trial_initial_checkpoint'
	results = single_trial(X, Y, num_classes, model_config, train_config, weights_initial_path)

	#########################################
	# Saves the results
	results_path = f'./single-trial_results/{competition}/{subject}'
	try:
		os.makedirs(results_path)
	except:
		pass

	with open(f'{results_path}/{config_label}.pk1', 'wb') as results_file:
		pickle.dump(results, results_file)