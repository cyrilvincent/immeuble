import tensorflow.keras as keras
import tensorflow

# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

feature = "RevetementVetuste"
# feature = "TraceHumidite"
# feature = "ChateauMoulureOrnement"
# feature = "FissureFacade"
# feature = "CablePendantEnSurface"
# feature = "BatimentVide"
# feature = "VoletVetuste"
# feature = "PanneauAVendre"
# feature = "BardageBoisAcierFacade"
# feature = "JardinExterieurNonEntretenu"
# # feature = "MauvaisEtatToiture"
# feature = "MultipleGraffitis"
# # feature = "BatimentMitoyenVetuste"
# feature = "BatimentInnocupe"
# # feature = "CommerceEnRdcVideFerme"
# feature = "MauvaisEtatGoutiere"
# feature = "PorteFenetreMurees"
# feature = "PresenceActiviteSuivantes"

seed = 1
tensorflow.random.set_seed(seed)
# np.random.seed(seed)
# random.seed(seed)

def Cyril():
    model = keras.models.Sequential()
    model.add(keras.layers.Conv2D(32, (3, 3), input_shape=(224, 224, 3), padding="same"))
    model.add(keras.layers.Activation('relu'))
    model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
    # 112, 112, 32

    model.add(keras.layers.Conv2D(64, (3, 3)))
    model.add(keras.layers.Activation('relu'))
    model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
    # 56, 56, 64

    model.add(keras.layers.Conv2D(128, (3, 3)))
    model.add(keras.layers.Activation('relu'))
    model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
    # 28, 28, 128

    model.add(keras.layers.Conv2D(128, (3, 3)))
    model.add(keras.layers.Activation('relu'))
    model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
    # 14, 14, 128

    # Dense
    model.add(keras.layers.Flatten())
    # 25088
    model.add(keras.layers.Dense(8000))
    model.add(keras.layers.Activation('relu'))
    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(2000))
    model.add(keras.layers.Activation('relu'))
    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(1))
    model.add(keras.layers.Activation('sigmoid'))
    return model

def train():
    model = Cyril()
    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
    model.summary()

    trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255, validation_split=0.2,
        # shear_range=0.2,
        # zoom_range=0.2,
        # width_shift_range=0.2,
        horizontal_flip=True
                                                            )

    batchSize = 1

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


    model = keras.models.load_model(f'data/{feature}/cyrilmodel-61.h5')
    model.optimizer = keras.optimizers.SGD(1e-4,nesterov=True)

    model.fit(
            trainGenerator,
            epochs=40,
            validation_data=validationGenerator,
    )

    score = model.evaluate(validationGenerator)
    model.save(f'data/{feature}/cyrilmodel-{score[1]*100:.0f}.h5')



if __name__ == '__main__':
    train()








