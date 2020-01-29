import tensorflow.keras as keras
import tensorflow

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

feature = "RevetementVetuste"

# seed = 1
# tensorflow.random.set_seed(seed)
# np.random.seed(seed)
# random.seed(seed)

def train():
    model = tensorflow.keras.applications.inception_v3.InceptionV3(include_top=False, weights="imagenet", input_shape=(299, 299, 3))
    model.summary()

    x = model.output
    x = keras.layers.Flatten()(x)
    x = keras.layers.Dropout(0.2)(x)
    x = keras.layers.Dense(1280, activation="relu")(x)
    x = keras.layers.Dropout(0.2)(x)
    x = keras.layers.Dense(1, activation="sigmoid")(x)

    model = keras.models.Model(inputs=model.input, outputs=x)

    model.summary()

    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])


    trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255, validation_split=0.2,
        # shear_range=0.2,
        # zoom_range=0.2,
        # width_shift_range=0.2,
        # horizontal_flip=True
                                                            )

    batchSize = 16

    trainGenerator = trainset.flow_from_directory(
            f'data/{feature}',
            target_size=(299, 299),
            subset = 'training',
            class_mode="binary",
            batch_size=batchSize)

    validationGenerator = trainset.flow_from_directory(
            f'data/{feature}',
            target_size=(299, 299),
            class_mode="binary",
            subset = 'validation',
            batch_size=batchSize)

    model.fit(
            trainGenerator,
            epochs=20,
            validation_data=validationGenerator,
    )

    model.save(f'data/{feature}/mobilenetmodel.h5')
    # batch=16
    # 594s 2s/step - loss: 0.5676 - accuracy: 0.7245 - val_loss: 11.1504 - val_accuracy: 0.5237

if __name__ == '__main__':
    train()








