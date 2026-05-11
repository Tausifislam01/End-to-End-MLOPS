import joblib
import pandas as pd


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load("artifacts/model_trainer/model.joblib")

    def predict(self, data):
        data = pd.DataFrame([data])
        prediction = self.model.predict(data)
        return prediction

