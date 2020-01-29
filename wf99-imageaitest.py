from imageai.Prediction import ImagePrediction
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("C:/Users/conta/.keras/models/resnet50_weights_tf_dim_ordering_tf_kernels.h5")
prediction.loadModel()

predictions, probabilities = prediction.predictImage("data/PanneauAVendre/1/A10233849101504000003_001_201808.jpg", result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)