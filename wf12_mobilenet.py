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
# feature = "VoletVetuste"
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

seed = 1
tensorflow.random.set_seed(seed)
# np.random.seed(seed)
# random.seed(seed)

def train():
    model = tensorflow.keras.applications.mobilenet_v2.MobileNetV2(include_top=False, weights="imagenet", input_shape=(224, 224, 3))
    model.summary()

    for layer in model.layers:
        layer.trainable = False

    x = model.output
    x = keras.layers.Flatten()(x)
    x = keras.layers.Dense(2000, activation="relu")(x)
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
        horizontal_flip=True
                                                            )

    batchSize = 8

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

    model = keras.models.load_model(f'data/{feature}/mobilenetmodel-66.h5')
    #model.optimizer = keras.optimizers.SGD(1e-3,nesterov=False)

    model.fit(
            trainGenerator,
            epochs=10,
            validation_data=validationGenerator,
    )

    score = model.evaluate(validationGenerator)
    model.save(f'data/{feature}/mobilenetmodel-{score[1]*100:.0f}.h5')
    # batch=16
    # 594s 2s/step - loss: 0.5676 - accuracy: 0.7245 - val_loss: 11.1504 - val_accuracy: 0.5237

if __name__ == '__main__':
    train()








