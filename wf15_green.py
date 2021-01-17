# import tensorflow.keras as keras
# import tensorflow
import numpy as np
from PIL import Image

import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

img = "A02239111374727000001_001_201804.jpg"

# seed = 1
# tensorflow.random.set_seed(seed)

def analyze(path):
    im = Image.open(path)
    width, height = im.size
    im = im.crop((0, height // 2, width, height))
    rgb = np.array(im.convert("RGB"))
    hsv = np.array(im.convert("HSV"))
    h = hsv[:,:,0]
    s = hsv[:,:,1]
    lo,hi = 75,100
    smin = 20
    lo = int((lo * 255) / 360)
    hi = int((hi * 255) / 360)
    smin = int((smin * 255) / 360)
    notgreen = np.where((h > lo) & (h < hi) & (s > smin), False, True)
    rgb[notgreen] = [0,0,0]
    ratio = (rgb.shape[0]*rgb.shape[1] - notgreen.sum()) / (rgb.shape[0]*rgb.shape[1])
    # print(f"Count: {ratio*100:.1f}%")
    # im = Image.fromarray(rgb)
    # im.show()
    return ratio

def predict(path, threshold):
    with open(f"{path}/green.csv","w") as f:
        f.write("path,ok,green\n")
        ratios=[]
        for file in os.listdir(path):
            if file.lower().endswith(".jpg"):
                ratio = analyze(f"{path}/{file}")
                ratios.append(ratio)
                ok = ratio > threshold
                print(f"{file},{ok},{ratio}")
                f.write(f"{file},{ok},{ratio}\n")
        return np.array(ratios)

if __name__ == '__main__':
    path = "data/TraceHumidite/0"
    threshold = 0.004
    ratios = predict(path, threshold)
    print(np.mean(ratios), np.std(ratios), np.median(ratios), np.quantile(ratios, [0.25])) #0.025 0.039 0.012 0.004 vs0 0.035! 0.053 0.017! 0.006
    print(ratios.size, ratios[ratios > threshold].size, ratios[ratios > threshold].size/ratios.size) #8690 4918 0.56 vs0 0.85!








