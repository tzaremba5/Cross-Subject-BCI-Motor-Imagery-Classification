################################################################################
#
# CSCD.py
#
# Runs all the CSCD (across all subjects with matching classes) experiments
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

from CSWD import Cross_Subject
from create_datasets import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSWD')

    # Gets the arguments to pick the subject
    parser.add_argument('Competition',
                        nargs=1,
                        help='BCI Competition (IV_IIa, IV_I, III_IVa')
    parser.add_argument(
        'Subject',
        nargs=1,
        help='Subject has to be from the competition listed above')
    parser.add_argument(
        'Model_Config',
        nargs=1,
        help='Subject has to be from the competition listed above')
    parser.add_argument(
        'Train_Config',
        nargs=1,
        help='Subject has to be from the competition listed above')
    parser.add_argument(
        'Config_Label',
        nargs=1,
        help='Subject has to be from the competition listed above')
    args = parser.parse_args()

    competition = args.Competition[0]
    subject = args.Subject[0]
    model_config_fname = args.Model_Config[0]
    train_config_fname = args.Train_Config[0]
    config_label = args.Config_Label[0]

    with open(model_config_fname, 'r') as infile:
        model_config = json.loads(infile.read())

    with open(train_config_fname, 'r') as infile:
        train_config = json.loads(infile.read())

    assert competition in competition_names, "Enter a competition name"
    assert subject in competitions[competition][
        'subjects'], "Enter a subject id from the given competition"

    # Creates the datasets
    X_main, Y_main, X_other, Y_other, num_classes, class_weights = create_dataset_CSCD(
        competition, subject)
    X_main = np.array(X_main)
    Y_main = np.array(Y_main)
    X_other = np.array(X_other)
    Y_other = np.array(Y_other)

    # Collects the results
    weights_initial_path = f'./checkpoints/{competition}_{subject}_CSCD_initial_checkpoint'
    results_zero, results_fifty = Cross_Subject(X_main, Y_main, X_other,
                                                Y_other, num_classes,
                                                class_weights,
                                                weights_initial_path,
                                                model_config, train_config)

    # Saves the results 
    results_path = f'./CSCD_results/{competition}/{subject}'
    try:
        os.makedirs(results_path)
    except:
        pass

    with open(f'{results_path}/results_zero_{config_label}.pk1',
              'wb') as results_file_zero:
        pickle.dump(results_zero, results_file_zero)

    with open(f'{results_path}/results_fifty_{config_label}.pk1',
              'wb') as results_file_fifty:
        pickle.dump(results_fifty, results_file_fifty)
