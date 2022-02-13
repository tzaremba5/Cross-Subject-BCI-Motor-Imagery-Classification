################################################################################
# model.py
# 
# Stores the model that all the experiments are run on
#

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam

# model
# 
# Creates and returns the model to classify the STFT features
#w
def model(num_classes, input_shape):

	  model = Sequential()
	  model.add(Conv2D(4, kernel_size = (5, 5), activation='relu',
	  	padding='same', nput_shape=input_shape))

	  model.add(MaxPool2D((2,2)))

	  model.add(Conv2D(4, kernel_size = (5, 5), activation='relu',
	  	padding='same', input_shape=input_shape))

	  model.add(Flatten())
	  model.add(Dense(200, activation='relu'))
	  model.add(Dropout(0.9))
	  model.add(Dense(num_classes, activation='sigmoid'))

	  model.compile(Adam(0.0001), loss='sparse_categorical_crossentropy',
	  	metrics=['accuracy'])

	  return model