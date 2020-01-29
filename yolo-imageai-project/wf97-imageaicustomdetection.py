from imageai.Prediction.Custom import CustomImagePrediction

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("../gitimmeuble/data/yolo/models/model_ex-001_acc-0.419118.h5")
prediction.setJsonPath("../gitimmeuble/data/yolo/json/model_class.json")
prediction.loadModel(num_objects=3)

predictions, probabilities = prediction.predictImage("../gitimmeuble/data/VoletVetutste/1/A01368071457898000001_001_201804.jpg", result_count=5)
#predictions, probabilities = prediction.predictImage("../gitimmeuble/data/VoletVetutste/0/A15989101235332000002_003_201810.jpg", result_count=5)

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(str(eachPrediction) + " : " + str(eachProbability))