import tensorflow.keras as keras
import tensorflow
import keras_ocr
import os

import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

feature = "PanneauAVendre"

seed = 1
tensorflow.random.set_seed(seed)

pipeline = keras_ocr.pipeline.Pipeline()


def _predict(path):
    images = [keras_ocr.tools.read(url) for url in [path]]
    prediction_groups = pipeline.recognize(images)
    res = [p[0] for p in prediction_groups[0]]
    l = list(dict.fromkeys(res))
    return " ".join(l)

def predict(path):
    with open(f"{path}/ocr.csv","w") as f:
        f.write("path,ok,ocr\n")
        for file in os.listdir(path):
            if file.lower().endswith(".jpg"):
                s = _predict(f"{path}/{file}").strip().upper()
                found = "VEN" in s or "LOU" in s or "LOC" in s or "ORPI" in s or "AGENC" in s or "DISP" in s or "ENDRE" in s or "OUER" in s
                print(f"{file},{found},{s}")
                f.write(f"{file},{found},{s}\n")

if __name__ == '__main__':
    predict("data/PanneauAVendre/1")








