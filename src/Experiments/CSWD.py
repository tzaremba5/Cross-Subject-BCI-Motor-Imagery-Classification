################################################################################
#
# CSWD.py
#
# Runs all the CSWD (across subjects - within dataset) experiments
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


# Cross_Subject
#
#
def Cross_Subject(X_main, Y_main, X_other, Y_other, num_classes, class_weights,
                  weights_initial, model_config, train_config):
    es = keras.callbacks.EarlyStopping(monitor='val_loss',
                                       mode='min',
                                       verbose=1,
                                       patience=train_config['patience'])
    model = STFTModel(num_classes, **model_config)

    ############## Runs the zero trial experiment ##############
    ztp = []
    ztl = []

    X_other, Y_other = sklearn.utils.shuffle(X_other, Y_other)
    model.fit(X_other,
              Y_other,
              validation_data=(X_main, Y_main),
              epochs=train_config['epochs'],
              batch_size=train_config['batch_size'],
              class_weight=class_weights,
              callbacks=[es],
              verbose=1)
    model.save_weights(weights_initial)

    ztp.append(model.predict(X_main).tolist())
    ztl.append(Y_main.tolist())

    ztr = results(ztp, ztl, [], model_config, train_config)

    ############## Runs the 50% trial experiment ##############
    indices = []
    predictions = []
    labels = []
    for iteration in range(3):
        sss = sklearn.model_selection.StratifiedShuffleSplit(n_splits=2)
        sss.get_n_splits(X_main, Y_main)

        for train_index, test_index in sss.split(
                X_main, Y_main):  # gets the train and test indecies
            model.load_weights(
                weights_initial)  # Restores the model to the inital weights

            train_index.astype(int, copy=False)
            test_index.astype(int, copy=False)

            X_train, X_test = X_main[train_index], X_main[test_index]
            y_train, y_test = Y_main[train_index], Y_main[test_index]

            model.fit(X_train,
                      y_train,
                      validation_data=(X_test, y_test),
                      epochs=train_config['epochs'],
                      batch_size=train_config['batch_size'],
                      callbacks=[es],
                      verbose=1)
            fold_predictions = model.predict(X_test)

            # saves the predictions
            indices.append(X_test.tolist())
            predictions.append(fold_predictions.tolist())
            labels.append(y_test.tolist())

    r = results(predictions, labels, indices, model_config, train_config)
    return ztr, r


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='CSWD')

    ############## Gets the arguments to pick the subject ##############
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

    # Loads in the config files
    with open(model_config_fname, 'r') as infile:
        model_config = json.loads(infile.read())

    with open(train_config_fname, 'r') as infile:
        train_config = json.loads(infile.read())

    assert competition in competition_names, "Enter a competition name"
    assert subject in competitions[competition][
        'subjects'], "Enter a subject id from the given competition"

    ############## Creates the datasets ##############
    X_main, Y_main, X_other, Y_other, num_classes, class_weights = create_dataset_CSCD(
        competition, subject)
    X_main = np.array(X_main)
    Y_main = np.array(Y_main)
    X_other = np.array(X_other)
    Y_other = np.array(Y_other)

    ############## Collects the results ##############
    weights_initial_path = f'./checkpoints/{competition}_{subject}_CSWD_initial_checkpoint'
    results_zero, results_fifty = Cross_Subject(X_main, Y_main, X_other,
                                                Y_other, num_classes,
                                                class_weights,
                                                weights_initial_path,
                                                model_config, train_config)

    ############## Saves the results ##############
    results_path = f'./CSWD_results/{competition}/{subject}'
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
