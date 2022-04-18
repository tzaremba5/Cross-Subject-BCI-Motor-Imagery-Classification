################################################################################
#
# display_results.py
#
# Shows all the results and downloads them as one .csv for each experiment
#

from results import *
import argparse
import pandas as pd
import pickle


# load_results
#
#
def load_results(results_path):
    with open(results_path, 'rb') as infile:
        results = pickle.load(infile)
    return results.accuracy, results.std_error


def avg_real(scores):
    scores_no_none = [x for x in scores if x != None]
    if len(scores_no_none) == 0:
        return None
    else:
        return sum(scores_no_none) / len(scores_no_none)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display Results')

    ############## Gets the config label ##############
    parser.add_argument(
        'Config_Label',
        nargs=1,
        help='Subject has to be from the competition listed above')
    args = parser.parse_args()
    config_label = args.Config_Label[0]

    results_path_single_trial = './single_trial_results'
    results_path_CSWD = './CSWD_results'
    results_path_CSCD = './CSCD_results'

    ############## Iterates through all of the subjects and makes a csv of their results ##############
    Accuracies_Single_Trial = []
    Errors_Single_Trial = []

    Accuracies_CSWD_0 = []
    Errors_CSWD_0 = []
    Accuracies_CSWD_50 = []
    Errors_CSWD_50 = []

    Accuracies_CSCD_0 = []
    Errors_CSCD_0 = []
    Accuracies_CSCD_50 = []
    Errors_CSCD_50 = []

    for competition in competition_names:
        for subject in competitions[competition]['subjects']:
            try:
                infile_path_single_trial = f'./single-trial_results/{competition}/{subject}/{config_label}.pk1'
                acc, err = load_results(infile_path_single_trial)
                Accuracies_Single_Trial.append(acc)
                Errors_Single_Trial.append(err)
            except Exception as e:
                print(e)
                Accuracies_Single_Trial.append(None)
                Errors_Single_Trial.append(None)
                print(
                    f'Single trial not tests complete for {subject} in competition {competition}'
                )

            try:
                infile_path_CSWD_0 = f'./CSWD_results/{competition}/{subject}/results_zero_{config_label}.pk1'
                acc_0, err_0 = load_results(infile_path_CSWD_0)
                Accuracies_CSWD_0.append(acc_0)
                Errors_CSWD_0.append(err_0)

                infile_path_CSWD_50 = f'./CSWD_results/{competition}/{subject}/results_fifty_{config_label}.pk1'
                acc_50, err_50 = load_results(infile_path_CSWD_50)
                Accuracies_CSWD_50.append(acc_50)
                Errors_CSWD_50.append(err_50)
            except Exception as e:
                print(e)
                Accuracies_CSWD_0.append(None)
                Errors_CSWD_0.append(None)
                Accuracies_CSWD_50.append(None)
                Errors_CSWD_50.append(None)
                print(
                    f'CSWD tests not complete for {subject} in competition {competition}'
                )

            try:
                infile_path_CSCD_0 = f'./CSCD_results/{competition}/{subject}/results_zero_{config_label}.pk1'
                acc_0, err_0 = load_results(infile_path_CSCD_0)
                Accuracies_CSCD_0.append(acc_0)
                Errors_CSCD_0.append(err_0)

                infile_path_CSCD_50 = f'./CSCD_results/{competition}/{subject}/results_fifty_{config_label}.pk1'
                acc_50, err_50 = load_results(infile_path_CSCD_50)
                Accuracies_CSCD_50.append(acc_50)
                Errors_CSCD_50.append(err_50)
            except Exception as e:
                print(e)
                Accuracies_CSCD_0.append(None)
                Errors_CSCD_0.append(None)
                Accuracies_CSCD_50.append(None)
                Errors_CSCD_50.append(None)
                print(
                    f'CSCD tests not complete for {subject} in competition {competition}'
                )

        if competition != 'III_IVa':  # Adds a blank for the competition for every competition except the last
            Accuracies_Single_Trial.append(None)
            Errors_Single_Trial.append(None)

            Accuracies_CSWD_0.append(None)
            Errors_CSWD_0.append(None)
            Accuracies_CSWD_50.append(None)
            Errors_CSWD_50.append(None)

            Accuracies_CSCD_0.append(None)
            Errors_CSCD_0.append(None)
            Accuracies_CSCD_50.append(None)
            Errors_CSCD_50.append(None)

    labels = []
    for competition_name in competition_names:
        labels.append(competition_name)
        for subject in competitions[competition_name]['subjects']:
            labels.append(subject)

    labels.append('Average')

    ############## Makes the dataframe for single trial ##############
    Accuracies_Single_Trial.append(avg_real(Accuracies_Single_Trial))
    Errors_Single_Trial.append(avg_real(Errors_Single_Trial))

    dict_single_trial = {
        labels[0]: labels[1:],
        'Accuracy': Accuracies_Single_Trial,
        'STD Error': Errors_Single_Trial
    }
    df = pd.DataFrame.from_dict(dict_single_trial)
    df.to_csv('./single-trial_results/Single_Trial_Results.csv')

    ############## Makes the dataframe for CSWD ##############
    Accuracies_CSWD_0.append(avg_real(Accuracies_CSWD_0))
    Errors_CSWD_0.append(avg_real(Errors_CSWD_0))
    Accuracies_CSWD_50.append(avg_real(Accuracies_CSWD_50))
    Errors_CSWD_50.append(avg_real(Errors_CSWD_50))

    dict_CSWD = {
        labels[0]: labels[1:],
        'Accuracy Zero Trial': Accuracies_CSWD_0,
        'STD Error Zero Trial': Errors_CSWD_0,
        'Accuracy 50% Trial': Accuracies_CSWD_50,
        'STD Error 50% Trial': Errors_CSWD_50
    }
    df = pd.DataFrame.from_dict(dict_CSWD)
    df.to_csv('./CSWD_results/CSWD_Results.csv')

    ############## Makes the dataframe for CSCD ##############
    Accuracies_CSCD_0.append(avg_real(Accuracies_CSCD_0))
    Errors_CSCD_0.append(avg_real(Errors_CSCD_0))
    Accuracies_CSCD_50.append(avg_real(Accuracies_CSCD_50))
    Errors_CSCD_50.append(avg_real(Errors_CSCD_50))

    dict_CSCD = {
        labels[0]: labels[1:],
        'Accuracy Zero Trial': Accuracies_CSCD_0,
        'STD Error Zero Trial': Errors_CSCD_0,
        'Accuracy 50% Trial': Accuracies_CSCD_50,
        'STD Error 50% Trial': Errors_CSCD_50
    }
    df = pd.DataFrame.from_dict(dict_CSCD)
    df.to_csv('./CSCD_results/CSCD_Results.csv')
