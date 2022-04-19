################################################################################
# create_dataset.py
#
# stores the functions for creating the dataset
#

from single_trial import *

def create_dataset(competition, subject, tasks = None):
    """ Creates the dataset for a given subject

    Args: 
        - competition: string
        - subject: string
        - tasks: string denoting which task to load

    Returns:
        - X: list of STFT representations
        - Y: labels

    Exception:
        None
     """

    # If the tasks aren't specificed then it gathers all the tasks for that subject
    if tasks == None:
        tasks = competitions[competition][subject].keys()

    num_classes = len(tasks)

    # Gets the path to open the features
    STFT_path = f'./features/{competition}/{subject}/'

    X, Y = [], []
    class_number = 0 # used to label the data
    for task in tasks:
        infile_STFT = open(STFT_path + f'{task}.pk1', 'rb')
        X_task = pickle.load(infile_STFT)
        X += X_task
        Y += [class_number] * len(X_task) # length of X_task = number of samples
        class_number += 1

    return X, Y, num_classes


def create_dataset_CSWD(competition, subject):
    """ Creates the main and pretraining datasets for a given subject under the CSWD paradigm

    Args: 
        - competition: string denoting the main competition
        - subject: string denoting the main subject

    Returns:
        - X_main: list of STFT samples for the main subject
        - Y_main: labels for main subject's data
        - X_other: list of STFT samples for the other subject
        - Y_other: labels for other subjects
        - num_classes: number of classes
        - class_weights: class weights for the pretraining dataset

    Exception:
        None
     """

    tasks = competitions[competition][subject].keys()
    num_classes = len(tasks)

    X_main = []
    Y_main = []
    X_other = []
    Y_other = []

    # Fills the main and other datsets
    class_number = 0
    for task in tasks:
        for other_subject in competitions[competition][task]:                
            X, Y, z = create_dataset(competition, other_subject, tasks = [task])

            if other_subject == subject:
                X_main += X
                Y_main += [class_number] * len(X)
            else:
                X_other += X
                Y_other += [class_number] * len(X)

        class_number += 1

    # Finds the weights for the classes of the other subjects
    class_weights = {}
    for class_number in range(num_classes):
        class_weights[class_number] = len(Y_other) / Y_other.count(class_number)

    return X_main, Y_main, X_other, Y_other, num_classes, class_weights


def create_dataset_CSCD(competition, subject):
    """ Creates the main and pretraining datasets for a given subject under the CSCD paradigm

    Args: 
        - competition: string denoting the main competition
        - subject: string denoting the main subject

    Returns:
        - X_main: list of STFT samples for the main subject
        - Y_main: labels for main subject's data
        - X_other: list of STFT samples for the other subject
        - Y_other: labels for other subjects
        - num_classes: number of classes
        - class_weights: class weights for the pretraining dataset

    Exception:
        None
     """

    tasks = competitions[competition][subject].keys()
    num_classes = len(tasks)

    X_main = []
    Y_main = []
    X_other = []
    Y_other = []

    # Fills the main and other datsets
    class_number = 0
    for task in tasks:
        for other_competition in competition_names:
            for other_subject in competitions[other_competition][task]:                
                X, Y, z = create_dataset(other_competition, other_subject, tasks = [task])

                if other_subject == subject and other_competition == competition:
                    X_main += X
                    Y_main += [class_number] * len(X)
                else:
                    X_other += X
                    Y_other += [class_number] * len(X)

        class_number += 1

    # Finds the weights for the classes of the other subjects
    class_weights = {}
    for class_number in range(num_classes):
        class_weights[class_number] = len(Y_other) / Y_other.count(class_number)

    return X_main, Y_main, X_other, Y_other, num_classes, class_weights