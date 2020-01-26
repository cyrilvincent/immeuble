import tensorflow.keras as keras
import tensorflow
import numpy as np
import random

# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

feature = "RevetementVetuste"

# seed = 1
# tensorflow.random.set_seed(seed)
# np.random.seed(seed)
# random.seed(seed)

def Chollet():
        model = keras.models.Sequential()
        model.add(keras.layers.Conv2D(32, (3, 3), input_shape=(150, 150, 3)))
        model.add(keras.layers.Activation('relu'))
        model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        # 32, 32, 32

        model.add(keras.layers.Conv2D(32, (3, 3)))
        model.add(keras.layers.Activation('relu'))
        model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        # 16, 16, 32

        model.add(keras.layers.Conv2D(64, (3, 3)))
        model.add(keras.layers.Activation('relu'))
        model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        # 8, 8, 64

        #Dense
        model.add(keras.layers.Flatten())
        # 4096
        model.add(keras.layers.Dense(64))
        model.add(keras.layers.Activation('relu'))
        model.add(keras.layers.Dropout(0.5))
        model.add(keras.layers.Dense(1))
        model.add(keras.layers.Activation('sigmoid'))
        return model

def train():
    model = Chollet()
    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
    model.summary()

    trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255, validation_split=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        width_shift_range=0.2,
        horizontal_flip=True
                                                            )

    batchSize = 2

    trainGenerator = trainset.flow_from_directory(
            f'data/{feature}',
            target_size=(150, 150),
            subset = 'training',
            class_mode="binary",
            batch_size=batchSize)

    validationGenerator = trainset.flow_from_directory(
            f'data/{feature}',
            target_size=(150, 150),
            class_mode="binary",
            subset = 'validation',
            batch_size=batchSize)

    model.fit(
            trainGenerator,
            epochs=10,
            validation_data=validationGenerator,
    )

    model.save(f'data/{feature}/cholletmodel.h5')
    # batch=16
    # 5 * 17s 58ms/step - loss: 0.5966 - accuracy: 0.6862 - val_loss: 0.6466 - val_accuracy: 0.6271

    # batch=2
    # 3 * 38s 16ms/step - loss: 0.6937 - accuracy: 0.5969 - val_loss: 0.6489 - val_accuracy: 0.6186

    # DataAugmentation * 4
    # 10 * 36s 121ms/step - loss: 0.6572 - accuracy: 0.6233 - val_loss: 0.6356 - val_accuracy: 0.6407

if __name__ == '__main__':
    train()








