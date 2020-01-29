from imageai.Detection import ObjectDetection
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("../gitimmeuble/res/yolo.h5")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="../gitimmeuble/res/A03118081749280000002_002_201904.jpg", output_image_path="../gitimmeuble/res/result.jpg", minimum_percentage_probability=30)

# import tensorflow as tf
# tf.executing_eagerly()

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")