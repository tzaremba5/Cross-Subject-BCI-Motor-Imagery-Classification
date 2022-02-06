######################################################################
# build_features.py
#
# Loads in the data from BCI Competition IV Dataset IIa, BCI 
# Competition IV Dataset I, and BCI Competition III Dataset IVa
#
# WARNING: this file will save the preprocessed EEG data
#

# Imports
import argparse

# load_BCI_Competition_IV_Dataset_IIa
#
#
def load_BCI_Competition_IV_Dataset_IIa(IV_IIa_path):
	print(IV_IIa_path)

# load_BCI_Competition_IV_Dataset_I
#
#
def load_BCI_Competition_IV_Dataset_I(IV_I_path):
	print(IV_I_path)

# load_BCI_Competition_IV_Dataset_IIa(
#
#
def load_BCI_Competition_IV_Dataset_IIa(III_IVa_path):
	print(III_IVa_path)

if __name__ == '__main__':
	# Gets the name of the directories to load the raw data 
	# and save the preprocessed data
	parser = argparse.ArgumentParser(description='Load Data')
	parser.add_argument('IV_IIa_path', nargs = 1, 
		help='BCI Competition IV Dataset IIa raw path or $ to skip')
	parser.add_argument('IV_I_path', nargs = 1, 
		help='BCI Competition IV Dataset I raw path or $ to skip')
	parser.add_argument('III_IVa_path', nargs = 1,
	 help='BCI Competition III Dataset IVa raw path or $ to skip')
	args = parser.parse_args()

	# Loads all the competition data, stores the preprocessed data
	if args.IV_IIa_path[0] != '$':
		load_BCI_Competition_IV_Dataset_IIa(args.IV_IIa_path[0])
	if args.IV_I_path[0] != '$':	
		load_BCI_Competition_IV_Dataset_I(args.IV_I_path[0])
	if args.III_IVa_path[0] != '$':
		load_BCI_Competition_IV_Dataset_IIa(args.III_IVa_path[0])