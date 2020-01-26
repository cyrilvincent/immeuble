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

def train():
    model = tensorflow.keras.applications.inception_resnet_v2.ResNet152V2(include_top=False, weights="imagenet", input_shape=(224, 224, 3))
    model.summary()

    for layer in model.layers:
        layer.trainable = False

    x = model.output
    x = keras.layers.Flatten()(x)
    x = keras.layers.Dense(4096, activation="relu")(x)
    x = keras.layers.Dropout(0.5)(x)
    x = keras.layers.Dense(1024, activation="relu")(x)
    x = keras.layers.Dropout(0.5)(x)
    x = keras.layers.Dense(1, activation="sigmoid")(x)

    model = keras.models.Model(inputs=model.input, outputs=x)

    model.summary()

    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])


    trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255, validation_split=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        width_shift_range=0.2,
        horizontal_flip=True
                                                            )

    batchSize = 4

    trainGenerator = trainset.flow_from_directory(
            f'data/{feature}',
            target_size=(224, 224),
            subset = 'training',
            class_mode="binary",
            batch_size=batchSize)

    validationGenerator = trainset.flow_from_directory(
            f'data/{feature}',
            target_size=(224, 224),
            class_mode="binary",
            subset = 'validation',
            batch_size=batchSize)

    model.fit(
            trainGenerator,
            epochs=20,
            validation_data=validationGenerator,
    )

    model.save(f'data/{feature}/resnetmodel.h5')
    # batch=4
    # 5 * 26s 86ms/step - loss: 0.6482 - accuracy: 0.6644 - val_loss: 0.6246 - val_accuracy: 0.6831
    # DataAugmentation * 4
    # 10 * 36s 121ms/step - loss: 0.6572 - accuracy: 0.6233 - val_loss: 0.6356 - val_accuracy: 0.6407

if __name__ == '__main__':
    train()








