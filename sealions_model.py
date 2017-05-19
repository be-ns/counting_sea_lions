from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.applications import vgg16

def make_model()
    model = vgg16.VGG16(include_top=False, weights='imagenet', input_tensor=None, input_shape=(3328, 4992, 3))

    model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
    model.add(Dense(64))
    model.add(Activation('relu'))
    # model.add(Dropout(0.5))
    model.add(Dense(5))
    model.add(Activation('relu'))

    model.compile(loss='binary_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])
