################################################################################
#
# results.py
#

# results
#
# This class holds the predictions across all the folds for each experiment
# and functions that will analyze the predictions
#
class results():

	def __init__(self, predictions, labels, indices, model_config, train_config):
		self.predictions = predictions
		self.labels = labels
		self.__indices = indices
		self.__model_config = model_config
		self.__train_config = train_config
		self.__accuracy = -1
		self.__std_error = -1

	def analysis(self):
		acc = 0
		std_error = 0

	@property
	def indices(self):
		return indices

	@property
	def model_config(self):
		return model_config

	@property
	def train_config(self):
		return train_config

	@property
	def accuracy(self):
		return self.__accuracy

	@property
	def std_error(self):
		return self.__std_error


if __name__ == '__main__':
	pass