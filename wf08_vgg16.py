import tensorflow.keras as keras
import tensorflow
import numpy as np
import random

# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

feature = "RevetementVetuste"
# feature = "TraceHumidite"
# feature = "ChateauMoulureOrnement"
# feature = "FissureFacade"
# feature = "CablePendantEnSurface"
# feature = "BatimentVide"
# feature = "VoletVetuste"
# # feature = "PanneauAVendre"
# # feature = "BardageBoisAcierFacade"
# # feature = "JardinExterieurNonEntretenu"
# feature = "MauvaisEtatToiture"
# # feature = "MultipleGraffitis"
# feature = "BatimentMitoyenVetuste"
# # feature = "BatimentInnocupe"
# feature = "CommerceEnRdcVideFerme"
# feature = "MauvaisEtatGoutiere"
# feature = "PorteFenetreMurees"
# feature = "PresenceActiviteSuivantes"

seed = 1
tensorflow.random.set_seed(seed)
# np.random.seed(seed)
# random.seed(seed)

def train():
    model = keras.applications.vgg16.VGG16(include_top=False, weights="imagenet", input_shape=(224, 224, 3))
    model.summary()

    for layer in model.layers:
        layer.trainable = False

    x = model.output
    x = keras.layers.Flatten()(x)
    x = keras.layers.Dense(8000, activation="relu")(x)
    x = keras.layers.Dropout(0.5)(x)
    x = keras.layers.Dense(2000, activation="relu")(x)
    x = keras.layers.Dropout(0.5)(x)
    x = keras.layers.Dense(1, activation="sigmoid")(x)

    model = keras.models.Model(inputs=model.input, outputs=x)

    model.summary()

    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])


    trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255, validation_split=0.2,
        # shear_range=0.1,
        # zoom_range=0.1,
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

    model = keras.models.load_model(f'data/{feature}/vgg16model-66.h5')
    model.optimizer = keras.optimizers.SGD(1e-3,nesterov=True)

    model.fit(
            trainGenerator,
            epochs=10,
            validation_data=validationGenerator,
    )

    score = model.evaluate(validationGenerator)
    model.save(f'data/{feature}/vgg16model-{score[1]*100:.0f}.h5')
    # RevetementVetuste
    # batch=16
    # 5 * 26s 86ms/step - loss: 0.6482 - accuracy: 0.6644 - val_loss: 0.6246 - val_accuracy: 0.6831
    # DataAugmentation * 4
    # 15 * 60s 202ms/step - loss: 0.6491 - accuracy: 0.6346 - val_loss: 0.6557 - val_accuracy: 0.6398

if __name__ == '__main__':
    train()








