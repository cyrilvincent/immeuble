import tensorflow.keras as keras
import tensorflow

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

feature = "RevetementVetuste"
# feature = "TraceHumidite"
# feature = "ChateauMoulureOrnement"
# feature = "FissureFacade"
# feature = "CablePendantEnSurface"
# feature = "BatimentVide"
# feature = "VoletVetutste"
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
        model.add(keras.layers.Dense(500))
        model.add(keras.layers.Activation('relu'))
        model.add(keras.layers.Dropout(0.4))
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
        # shear_range=0.2,
        # zoom_range=0.2,
        # width_shift_range=0.2,
        horizontal_flip=True
                                                            )

    batchSize = 16

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

    # model = keras.models.load_model(f'data/{feature}/cholletmodel-63.h5')
    # model.optimizer = keras.optimizers.SGD(1e-3,nesterov=True)

    model.fit(
            trainGenerator,
            epochs=10,
            validation_data=validationGenerator,
    )

    score = model.evaluate(validationGenerator)
    model.save(f'data/{feature}/cholletmodel-{score[1]*100:.0f}.h5')

    # RevetementVetuste
    # 0.64

    # TraceHumidite
    # DataAugmentation * 4 + batch=2
    # 10 * 96s 30ms/step - loss: 0.6854 - accuracy: 0.6128 - val_loss: 0.7453 - val_accuracy: 0.5932

    # ChateauMoulureOrnement
    # DataAugmentation * 4 + batch=8
    # 10 * 32s 63ms/step - loss: 0.6932 - accuracy: 0.5252 - val_loss: 0.6920 - val_accuracy: 0.5229

    # FissureFacade
    # DataAugmentation * 4 + batch=8
    # 32s 62ms/step - loss: 0.6354 - accuracy: 0.6508 - val_loss: 0.6157 - val_accuracy: 0.6676

    # CablePendantEnSurface
    # 102s 94ms/step - loss: 0.4663 - accuracy: 0.9356 - val_loss: 0.2569 - val_accuracy: 0.9374

    # BatimentVide
    # 13s 105ms/step - loss: 0.6908 - accuracy: 0.5530 - val_loss: 0.7049 - val_accuracy: 0.5166

    # VoletVetutste
    # 16s 63ms/step - loss: 0.6740 - accuracy: 0.6010 - val_loss: 0.6138 - val_accuracy: 0.6621

    # PanneauAVendre
    # 18s 61ms/step - loss: 0.6902 - accuracy: 0.5386 - val_loss: 0.6715 - val_accuracy: 0.6007

if __name__ == '__main__':
    train()








