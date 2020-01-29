import tensorflow.keras as keras
import tensorflow
import numpy as np
import random

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

feature = "RevetementVetuste"
feature = "TraceHumidite"
feature = "ChateauMoulureOrnement"
feature = "FissureFacade"
feature = "CablePendantEnSurface"
feature = "BatimentVide"
feature = "VoletVetutste"
# feature = "PanneauAVendre"
# feature = "BardageBoisAcierFacade"
# feature = "JardinExterieurNonEntretenu"
# feature = "MauvaisEtatToiture"
# feature = "MultipleGraffitis"
# feature = "BatimentMitoyenVetuste"
# feature = "BatimentInnocupe"
# feature = "CommerceEnRdcVideFerme"
# feature = "MauvaisEtatGoutiere"
# feature = "PorteFenetreMurees"
# feature = "PresenceActiviteSuivantes"

# seed = 1
# tensorflow.random.set_seed(seed)
# np.random.seed(seed)
# random.seed(seed)

def train():
    model = tensorflow.keras.applications.resnet_v2.ResNet152V2(include_top=False, weights="imagenet", input_shape=(224, 224, 3))
    model.summary()

    x = model.output
    x = keras.layers.Flatten()(x)
    x = keras.layers.Dropout(0.5)(x)
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
        # shear_range=0.2,
        # zoom_range=0.2,
        # width_shift_range=0.2,
        # horizontal_flip=True
                                                            )

    batchSize = 16

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
            epochs=50,
            validation_data=validationGenerator,
    )

    model.save(f'data/{feature}/resnet_retrain_model.h5')

if __name__ == '__main__':
    train()








