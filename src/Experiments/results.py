################################################################################
#
# results.py
#

from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from dataset_descriptions import *
import scipy

from sklearn.metrics import accuracy_score
import numpy as np

# results
#
# This class holds the predictions across all the folds for each experiment
# and functions that will analyze the predictions
#
# It also allows the user to display the results as a csv for all the subjects
# for a given config label
#
class results():

	def __init__(self, predictions, labels, indices, model_config, train_config):
		self.__predictions = predictions
		self.__labels = labels
		self.__indices = indices
		self.__model_config = model_config
		self.__train_config = train_config
		self.__accuracy_list = []
		self.__accuracy = -1
		self.__std_error = -1

	@property
	def indices(self):
		return self.__indices

	@property
	def model_config(self):
		return self.__model_config

	@property
	def train_config(self):
		return self.__train_config

	@property
	def accuracy(self):
		self.__predictions = np.array(self.__predictions)
		self.__predictions = np.argmax(self.__predictions, axis = 2)
		self.__labels = np.array(self.__labels)
		self.__accuracy_list = [accuracy_score(p, l) for p, l in zip(self.__predictions, self.__labels)]
		self.__accuracy = sum(self.__accuracy_list) / len(self.__accuracy_list)
		return self.__accuracy

	@property
	def std_error(self):
		self.__std_error = scipy.stats.sem(self.__accuracy_list)
		return self.__std_error
