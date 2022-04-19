################################################################################
# model.py
#
# Stores the model that all the experiments run on
#

from tensorflow.keras import Model
from tensorflow.keras.layers import Input, Conv2D, MaxPool2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import deserialize


def STFTModel(num_classes, f1, k1, a1, p1, f2, k2, a2, units1, r1, a3, o1, l1,
              m1):
    """ Creates the model to classify the STFT features

    Args: 
        num_classes: int
        f1: filter size 1
        k1: kernel size 1 
        a1: activation 1
        p1: padding 1
        f2: filter size 2
        k2: kernel 
        a2: activation 2
        units1: dense units 1
        r1: dropout rate 1
        a3: activation 3
        o1: optimizer
        l1: loss function
        m1: metrics to optimize for

    Returns:
        - model: compiled tf.keras.model object

    Exception:
        None
     """
    input1 = Input(shape=(540, 26, 1))

    #########################################

    block1 = Conv2D(f1,
                    kernel_size=k1,
                    activation=a1,
                    padding='same',
                    input_shape=(540, 26, 1))(input1)
    block1 = MaxPool2D(pool_size=p1)(block1)
    block1 = Conv2D(f2,
                    kernel_size=k2,
                    activation=a2,
                    padding='same',
                    input_shape=(540, 26, 1))(block1)

    block2 = Flatten()(block1)
    block2 = Dense(units=units1)(block2)
    block2 = Dropout(r1)(block2)
    dense = Dense(units=num_classes, activation=a3)(block2)

    #########################################

    model = Model(inputs=input1, outputs=dense)
    model.compile(optimizer=deserialize(o1), loss=l1, metrics=m1)
    return model
