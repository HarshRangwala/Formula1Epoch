import tensorflow as tf
import numpy as np
#import matplotlib
#from matplotlib.pyplot import imshow
from keras.models import Model, load_model, Sequential
from keras.optimizers import Adam
from keras.layers import Input, Convolution2D, MaxPooling2D, Activation, Dropout, Flatten, Dense

def model():
    # model with 3 hidden layers
    img = Input(shape = (672, 376, 3), name = 'img')

    x = Convolution2D(8, 3, 3)(img)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)

    x = Convolution2D(16, 3, 3)(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)

    x = Convolution2D(32, 3, 3)(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)

    merged = Flatten()(x)

    x = Dense(128)(merged)
    x = Activation('linear')(x)
    x = Dropout(.3)(x)


    jstk = Dense(1, name='jstk')(x)

    steerNet = Model(input=[img], output=[jstk])
    steerNet.compile(optimizer='adam', loss='mean_squared_error')
    print(steerNet.summary())
    return steerNet

def trainModel(model, imgIn, jstkOut):
    #trains predefined model with verbose logging
    model.fit(self, x=imgIn, y=jstkOut, batch_size=32, epochs=100, verbose=2, callbacks=None, validation_split=0.2, shuffle=True, initial_epoch=0)
    modelName = raw_input("Please enter the trained models filename")
    modelName = modelName + ".h5"
    model.save(modelName)
    print("Saved as %s" %(modelName) )

def testModel(testX, testY):
    # Test model and evauluate accuracy
    scores = model.evaluate(testX, testY)
    print("\nAccuracy: " + model.metrics_name[1], scores[1]*100)

model()