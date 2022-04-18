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
## Feature Generation


-------
## Model


-------
## Requirements


-------
## Usage
1. Download both the training and the evaluation data from the above links and put it into three seperate in their corresponding competition. Set the path of these folders as IV_IIa, IV_I, III_IVa or change the paths names in the makefile. WARNING: Do not change the names of the subject folders.

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


-------
## Accessing the results

