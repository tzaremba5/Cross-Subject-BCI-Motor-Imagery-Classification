MODEL_CONFIGURATION:=Experiments/Configurations/model_config1.json
TRAIN_CONFIGURATION:=Experiments/Configurations/training_config1.json
CONFIG_LABEL:= config_1
TUNE_COMPETITION:= IV_IIa
TUNE_SUBJECT:= A01

setup: requirements.txt
	pip install -r requirements.txt

load-data-all:
	python3 Data/load_data.py raw/IV_IIa raw/IV_I raw/III_IVa

build-features-all:
	python3 Data/build_features.py IV_IIa A01
	python3 Data/build_features.py IV_IIa A02
	python3 Data/build_features.py IV_IIa A03
	python3 Data/build_features.py IV_IIa A04
	python3 Data/build_features.py IV_IIa A05
	python3 Data/build_features.py IV_IIa A06
	python3 Data/build_features.py IV_IIa A07
	python3 Data/build_features.py IV_IIa A08
	python3 Data/build_features.py IV_IIa A09

	python3 Data/build_features.py IV_I a
	python3 Data/build_features.py IV_I b
	python3 Data/build_features.py IV_I c
	python3 Data/build_features.py IV_I d
	python3 Data/build_features.py IV_I e
	python3 Data/build_features.py IV_I f
	python3 Data/build_features.py IV_I g

	python3 Data/build_features.py III_IVa aa
	python3 Data/build_features.py III_IVa al
	python3 Data/build_features.py III_IVa av
	python3 Data/build_features.py III_IVa aw
	python3 Data/build_features.py III_IVa ay

run-tune-model:
	python3 Experiments/tuner.py ${TUNE_COMPETITION} ${TUNE_SUBJECT}

run-single-trial-all:
	python3 Experiments/single_trial.py IV_IIa A01 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py IV_IIa A02 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py IV_IIa A03 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py IV_IIa A04 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py IV_IIa A05 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py IV_IIa A06 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py IV_IIa A07 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py IV_IIa A08 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py IV_IIa A09 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}

	python3 Experiments/single_trial.py IV_I a ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py IV_I b ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py IV_I c ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py IV_I d ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py IV_I e ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py IV_I f ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py IV_I g ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}

	python3 Experiments/single_trial.py III_IVa aa ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py III_IVa al ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py III_IVa av ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py III_IVa aw ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/single_trial.py III_IVa ay ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}

	-rm -r checkpoints

run-cswd-all: 
	python3 Experiments/CSWD.py IV_IIa A01 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py IV_IIa A02 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py IV_IIa A03 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py IV_IIa A04 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py IV_IIa A05 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py IV_IIa A06 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py IV_IIa A07 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py IV_IIa A08 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py IV_IIa A09 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}

	python3 Experiments/CSWD.py IV_I a ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py IV_I b ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py IV_I c ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py IV_I d ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py IV_I e ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py IV_I f ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py IV_I g ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}

	python3 Experiments/CSWD.py III_IVa aa ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py III_IVa al ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py III_IVa av ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py III_IVa aw ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSWD.py III_IVa ay ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}

	-rm -r checkpoints

run-cscd-all:
	python3 Experiments/CSCD.py IV_IIa A01 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py IV_IIa A02 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py IV_IIa A03 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py IV_IIa A04 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py IV_IIa A05 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py IV_IIa A06 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py IV_IIa A07 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py IV_IIa A08 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py IV_IIa A09 ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}

	python3 Experiments/CSCD.py IV_I a ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py IV_I b ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py IV_I c ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py IV_I d ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py IV_I e ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py IV_I f ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py IV_I g ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}

	python3 Experiments/CSCD.py III_IVa aa ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py III_IVa al ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py III_IVa av ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py III_IVa aw ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}
	python3 Experiments/CSCD.py III_IVa ay ${MODEL_CONFIGURATION} ${TRAIN_CONFIGURATION} ${CONFIG_LABEL}

	-rm -r checkpoints

display-results: 
	python3 Experiments/display_results.py ${CONFIG_LABEL}

clean:
	-rm -r epochs
	-rm -r features
	-rm -r single-trial_results
	-rm -r CSWD_results
	-rm -r CSCD_results
	-rm -r checkpoints
	-rm -r tuner_results