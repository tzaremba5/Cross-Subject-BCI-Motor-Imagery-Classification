################################################################################
#
# single-trial.py
#
# Runs all the single-trial (within one subject) experiments
#

# Test

# create_dataset
#
#
# 
def create_dataset(subject):
	tasks = competitions[subject].keys()
	num_classes = len(tasks)

	X, Y = [], []
	task_number = 0
	for task in tasks:
		X_task = pickle.load(STFT_path.format(competition, subject, task), 'rb')
		X += X_task
		Y += [task_count] * len(X_task)
		task_count += 1

	return X, Y, num_classes

# single_trial
#
#
# 
def single_trial(X, Y, num_classes):
	sss = StratifiedShuffleSplit(n_splits=5, random_state=0)
  	es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=50)

  	# TODO GET PREDICTION INDECIES
  	 for iteration in range(3):
    sss.get_n_splits(X, Y)
    for train_index, test_index in sss.split(X, Y): # gets the train and test indecies
      model.load_weights('./checkpoints/my_checkpoint')

      train_index.astype(int, copy = False)
      test_index.astype(int, copy = False)

      X_train, X_test = X[train_index], X[test_index]
      y_train, y_test = Y[train_index], Y[test_index]

      model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = 1000, batch_size = 50, callbacks = [es], verbose = 0)
      fold_predictions = model.predict(X_test)

      # saves the predictions
      indices += X_test.tolist()
      predictions += fold_predictions.tolist()
      labels += y_test.tolist()

  results = {'indices':indices, 'predictions':predictions, 'labels':labels}
  return results

if __name__ == '__main__':
	# TO-DO: Get path to load the data
	STFT_path = """FILL IN PATH HERE"""

	for competition in ['IV_IIa', 'IV_I', 'III_IVa']
		for subject in competitions[competition]['subjects']:
			X, Y, num_classes = create_dataset(competition, subject)
			single_tria(X, Y, num_classes)
	
