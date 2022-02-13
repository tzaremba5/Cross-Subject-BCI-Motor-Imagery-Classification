################################################################################
# dataset_description.py
#
# Stores all the class information about each of the subjects
#

competition_names = ['IV_IIa', 'IV_I', 'III_IVa']

competitions = {
	'IV_IIa': {
		'subjects':['A01', 'A02', 'A03', 'A04'. 'A05', 'A06', 'A07', 'A08', 'A09'],
		'left': ['A01', 'A02', 'A03', 'A04'. 'A05', 'A06', 'A07', 'A08', 'A09'],
		'right': ['A01', 'A02', 'A03', 'A04'. 'A05', 'A06', 'A07', 'A08', 'A09'],
		'foot': ['A01', 'A02', 'A03', 'A05', 'A06', 'A07', 'A08', 'A09'],
		'A01':{'left': 7, 'right': 8, 'foot': 9},
		'A02':{'left': 7, 'right': 8, 'foot': 9}, 
		'A03':{'left': 7, 'right': 8, 'foot': 9},
        'A04':{'left': 7, 'right': 8},
        'A05':{'left': 7, 'right': 8, 'foot': 9},
        'A06':{'left': 7, 'right': 8, 'foot': 9}, 
		'A07':{'left': 7, 'right': 8, 'foot': 9}, 
		'A08':{'left': 7, 'right': 8, 'foot': 9},
		'A09':{'left': 7, 'right': 8, 'foot': 9}
	},
	'IV_I': {
		'subjects':['A', 'B', 'C', 'D', 'E', 'F', 'G'],
		'left':['A', 'B', 'C', 'D', 'E', 'F', 'G'],
		'right':['B', 'C', 'D', 'E', 'G'],
		'foot': ['A', 'F'],
		'A':{'left':1, 'foot':2},
		'B':{'left':1, 'right':2},
		'C':{'left':1, 'right':2}, 
		'D':{'left':1, 'right':2}, 
		'E':{'left':1, 'right':2},
		'F':{'left':1, 'foot':2},
		'G':{'left':1, 'right':2}
	},
	'III_IVa': {
		'subjects':['aa', 'al', 'av', 'aw', 'ay'],
		'left':[],
		'right':['aa', 'al', 'av', 'aw', 'ay'],
		'foot':['aa', 'al', 'av', 'aw', 'ay'],
		'aa':{'right': 1, 'foot': 2},
		'al':{'right': 1, 'foot': 2},
		'av':{'right': 1, 'foot': 2},
		'aw':{'right': 1, 'foot': 2}, 
        'ay':{'right': 1, 'foot': 2}
    }
}