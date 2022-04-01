################################################################################
# create_dataset.py
#
# stores the functions for creating the dataset
#

from single_trial import *

# create_dataset
#
# Creates the dataset for a given subject
# - competition
# - subject
#
# Output: Numpy array shape (n_samples, sample_size)
# 
def create_dataset(competition, subject, tasks = None):

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

# create_dataset_CSWD
#
# FInds the other subjects that have the same tasks within that subject's dataset
# and adds those tasks to X_other and the labels associated with those subjects to Y_other
# also returns the class weights in case X_other is not symmetric
#
def create_dataset_CSWD(competition, subject):

    ##############
    tasks = competitions[competition][subject].keys()
    num_classes = len(tasks)

    ##############
    X_main = []
    Y_main = []
    X_other = []
    Y_other = []

    ############## Fills the main and other datsets ##############
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

    ############## Finds the weights for the classes of the other subjects ##############
    class_weights = {}
    for class_number in range(num_classes):
        class_weights[class_number] = len(Y_other) / Y_other.count(class_number)

    return X_main, Y_main, X_other, Y_other, num_classes, class_weights

# create_dataset_CSCD
#
# FInds the other subjects that have the same tasks across all three datasets 
# and adds those tasks to X_other and the labels associated with those subjects to 
# Y_other and also returns the class weights in case X_other is not symmetric
#
def create_dataset_CSCD(competition, subject):

    ##############
    tasks = competitions[competition][subject].keys()
    num_classes = len(tasks)

    ##############
    X_main = []
    Y_main = []
    X_other = []
    Y_other = []

    ############## Fills the main and other datsets ##############
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

    ############## Finds the weights for the classes of the other subjects ##############
    class_weights = {}
    for class_number in range(num_classes):
        class_weights[class_number] = len(Y_other) / Y_other.count(class_number)

    return X_main, Y_main, X_other, Y_other, num_classes, class_weights