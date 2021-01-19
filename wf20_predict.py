import tensorflow.keras as keras
import os
import numpy as np

feature = "RevetementVetuste"
model = keras.models.load_model(f"data/{feature}/vgg16model-66.h5")

def predict(path):
    image = keras.preprocessing.image.load_img(path, target_size=(224, 224))
    image = keras.preprocessing.image.img_to_array(image)
    image *= 1. / 255
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    #image = keras.applications.vgg16.preprocess_input(image)
    return model.predict(image)

def predicts(path, threshold=0.5):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    qs = []
    un = 0
    print(f"Scan {path}/1")
    files = os.listdir(f"{path}/1")
    for f in files :
        res = predict(f"{path}/1/{f}")[0][0]
        if res > threshold :
            tp += 1
            qs.append((res - 0.5) * 2)
        elif res > 1 - threshold:
            un += 1
        else:
            fp += 1
        if tp + tn + fp + fn != 0:
            print(f"Accuracy: {(tp + tn) / (tp + tn + fp + fn):.2f}, Unknown : {un / (tp + tn + fp + fn + un):.2f}")
    print(f"Scan {path}/0")
    files = os.listdir(f"{path}/0")
    for f in files:
        res = predict(f"{path}/0/{f}")[0][0]
        # print(res)
        if res < 1 - threshold:
            tn += 1
            qs.append((0.5 - res) * 2)
        elif res < threshold:
            un += 1
        else:
            fn += 1
        print(f"Accuracy: {(tp + tn) / (tp + tn + fp + fn):.2f}, Unknown : {un / (tp + tn + fp + fn + un):.2f}")
    return tp,tn,fp,fn,qs,un

if __name__ == '__main__':
    #res = predict("res/1.jpg")
    # res = predict("data/RevetementVetuste/1/A07079111281875000001_001_201808.jpg")
    # print(res)
    tp,tn,fp,fn,qs,un = predicts("data/RevetementVetuste", 0.52)
    print(f"Accuracy: {(tp + tn) / (tp + tn + fp + fn):.2f}") #0.70 (0.04 overfitting) 0.52=>0.75 (0.71 without overfitting)
    print(f"Precision: {(tp) / (tp + fp):.2f}") #0.62 0.52=>0.68
    print(f"Recall: {(tp) / (tp + fn):.2f}") #0.72 0.52=>0.75
    print(f"Unknown : {un / (tp + tn + fp + fn + un):.2f}") #0.52=>0.19
    print(np.mean(qs), np.std(qs), np.min(qs), np.max(qs)) #0.22 ? 0 1 0.52=>0.26 0.16 0.04 1
