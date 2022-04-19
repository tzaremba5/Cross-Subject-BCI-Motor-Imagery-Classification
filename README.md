# Cross Subject BCI Motor Imagery Classification

## Introduction
In this paper, we propose a method of assimilating all the subject's data across three datasets: BCI Competition IV Dataset I, IIa and BCI competition III Dataset IVa. After, we get a baseline accuracy using the single-trial framework to prove that the assimilation step did not drastically alter that subject's data. After this, we use the data to pretrain other subjects both within the same dataset (CSWD) and with subjects across the other datasets (CSCD). Our hypothesis is that a unique pattern in the EEG data would allow a model to correctly classify MI tasks for most people with this extra data.

The source code in src contains the following
- Data: scripts for loading the data and generating the STFT features
- Experiments: scripts for running and analyzing the single-trial, CSCD, and CSWD experiments

-------
## Datasets

### BCI Competition IV: https://www.bbci.de/competition/iv/#datasets
- BCI Competition IV Dataset IIa
- BCI Competition IV Dataset I

### BCI Competition III https://www.bbci.de/competition/iii/
- BCI Competition III Dataset IVa


-------
## Requirements
All of the scripts are run using python3 and the following dependencies and versions are recomended. 

- mne 1.0.0
- scipy 1.7.0
- tensorflow 2.8.0
- scikit-learn 1.0.2
- keras 2.8.0
- keras-tuner 1.1.2
- numpy 1.22.3
- pickleshare 0.7.5
- argcomplete 1.12.0
- pandas 1.4.1

-------
## Usage
1. Download both the training and the evaluation data from the above links and put it into three seperate in their corresponding competition. Set the path of these folders as IV_IIa, IV_I, III_IVa or change the paths names in the makefile. 

WARNING: Do not change the names of the subject folders.

2. Run to download the necessary libraries
```bash
$ make setup
```

3. Run to generate the epochs 
```bash
$ make load-data-all
```

4. Run to generate the STFT features
```bash
$ make build-features-all
```

5. Run the single-trial experiments
```bash
$ make run-single-trial-all
```

6. Run the CSWD experiments
```bash
$ make run-cswd-all
```

7. Run the CSCD experiments
```bash
$ make run-cscd-all
```

Optional steps:

Change the hyperparameters saved in ./Experiments/Configurations json files

Tune the model's hyperparameters
```bash
$ make run-tune-model
```

-------
## Accessing the results
Calculate the accuracy and std error for all the experiments and save them to src as a csv for each experiment
```bash
$ make display-results
```
