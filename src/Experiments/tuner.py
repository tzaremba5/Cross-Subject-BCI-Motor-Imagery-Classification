################################################################################
#
# keras_tuner.py
#
# Tunes the model testing across 5 folds for the single-trial experiments

import kerastuner as kt

import os
import pickle
import random
import argparse
from dataset_descriptions import *
from create_datasets import *
import keras

from sklearn import model_selection

num_classes = -1


# CVTuner
#
# Tests a given set of hyperparameters against a 5-fold cross validatioon
#
class CVTuner(kt.engine.tuner.Tuner):

    def run_trial(self, trial, x, y, batch_size=4, epochs=500):
        es = keras.callbacks.EarlyStopping(monitor='val_loss',
                                           mode='min',
                                           verbose=1,
                                           patience=50)

        cv = model_selection.KFold(5, shuffle=True)
        val_accuracies = []

        for train_indices, test_indices in cv.split(x):
            x_train, x_test = x[train_indices], x[test_indices]
            y_train, y_test = y[train_indices], y[test_indices]
            model = self.hypermodel.build(trial.hyperparameters)

            model.fit(x_train,
                      y_train,
                      validation_data=(x_test, y_test),
                      batch_size=batch_size,
                      epochs=epochs,
                      callbacks=[es])
            val_accuracies.append(model.evaluate(x_test, y_test)[1])

        self.oracle.update_trial(trial.trial_id,
                                 {'val_accuracy': np.mean(val_accuracies)})
        # self.save_model(trial.trial_id, model)


def model_builder(hp):

    ############## Sets the parameters to be tuned ##############
    hp_f1 = hp.Int('Filter_1', min_value=1, max_value=10, step=1)
    hp_k1x = hp.Int('Kernel_1x', min_value=1, max_value=45, step=1)  #
    hp_k1y = hp.Int('Kernel_1y', min_value=1, max_value=13, step=1)  #
    hp_a1 = hp.Choice('Activation 1', ['sigmoid', 'tanh', 'relu', 'elu'])

    hp_p1x = hp.Int('Max_1x', min_value=1, max_value=10, step=1)  #
    hp_p1y = hp.Int('Max_1y', min_value=1, max_value=10, step=1)  #

    hp_f2 = hp.Int('Filter_2', min_value=1, max_value=10, step=1)
    hp_k2x = hp.Int('Kernel_2x', min_value=1, max_value=45, step=1)  #
    hp_k2y = hp.Int('Kernel_2y', min_value=1, max_value=13, step=1)  #
    hp_a2 = hp.Choice('Activation 2', ['sigmoid', 'tanh', 'relu', 'elu'])

    hp_units1 = hp.Int('Dense Units', min_value=10, max_value=2000, step=10)
    hp_r1 = hp.Float('Dropout Rate',
                     min_value=0.1,
                     max_value=0.9,
                     default=0.2,
                     step=0.05)
    a3 = 'sigmoid'
    o1 = {'class_name': 'adam', 'config': {'lr': 0.0001}}
    l1 = 'sparse_categorical_crossentropy'
    m1 = 'accuracy'

    # Model
    model = STFTModel(NUM_CLASSES, hp_f1, (hp_k1x, hp_k1y), hp_a1,
                      (hp_p1x, hp_p1y), hp_f2, (hp_k2x, hp_k2y), hp_a2,
                      hp_units1, hp_r1, a3, o1, l1, m1)
    return model


if __name__ == '__main__':
    #########################################
    # Gets the arguments to get the given subject

    parser = argparse.ArgumentParser(description='Single Trial')

    # Parameters to pick the subject
    parser.add_argument('Competition',
                        nargs=1,
                        help='BCI Competition (IV_IIa, IV_I, III_IVa')
    parser.add_argument(
        'Subject',
        nargs=1,
        help='Subject has to be from the competition listed above')

    args = parser.parse_args()

    # Gets all the arguments
    competition = args.Competition[0]
    subject = args.Subject[0]

    assert competition in competition_names, "Enter a competition name"
    assert subject in competitions[competition][
        'subjects'], "Enter a subject id from the given competition"

    # Creates the dataset
    X, Y, NUM_CLASSES = create_dataset(competition, subject)
    X = np.array(X)
    Y = np.array(Y)

    tuner = CVTuner(hypermodel=model_builder,
                    oracle=kt.oracles.BayesianOptimization(
                        objective='val_accuracy', max_trials=1),
                    project_name='tuner_results')

    tuner.search(X, Y, batch_size=50, epochs=1)
    best_model = tuner.get_best_hyperparameters(num_trials=1)[0].get_config()

    ############## Saves the best hyperparameters ##############
    best_model_hp = best_model['values']

    with open(f'./tuner_results/{competition}_{subject}_best_model.json',
              'w') as outfile:
        json.dump(best_model_hp, outfile)
