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

class results():
    def __init__(self, predictions, labels, indices, model_config,
                 train_config):
        """ Instantiates the results object

        Args:
            predictions: np array of the predictions
            labels: np array of the labels
            indices: np array of the indicies of the samples
            model_config: dictionary containing the model config
            train_config: dictionary containing the training config

        Returns:
            - self: Results object

        Exception:
            None
        """
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
        self.__predictions = np.argmax(self.__predictions, axis=2)
        self.__labels = np.array(self.__labels)
        self.__accuracy_list = [
            accuracy_score(p, l)
            for p, l in zip(self.__predictions, self.__labels)
        ]
        self.__accuracy = sum(self.__accuracy_list) / len(self.__accuracy_list)
        return self.__accuracy

    @property
    def std_error(self):
        self.__std_error = scipy.stats.sem(self.__accuracy_list)
        return self.__std_error
