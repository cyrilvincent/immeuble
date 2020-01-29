from imageai.Prediction.Custom import ModelTraining
model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory("../gitimmeuble/data/yolo")
model_trainer.trainModel(num_objects=3, num_experiments=50, enhance_data=True, batch_size=8, show_network_summary=True,)