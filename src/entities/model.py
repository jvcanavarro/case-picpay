import joblib
import pandas as pd
from datetime import datetime


class ModelPredictor:
    def __init__(self):
        self.model = None
        self.history = pd.DataFrame(columns=["timestamp", "input", "prediction"])

    def load(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, X):
        predictions = self.model.predict(X)

        # Armazenar o histórico com timestamp
        for i in range(len(X)):
            self.history = self.history.append(
                {
                    "timestamp": datetime.now(),
                    "input": X[i],
                    "prediction": predictions[i],
                },
                ignore_index=True,
            )

        return predictions

    def save_history(self, filename):

        self.history.to_csv(filename, index=False)

    def get_history(self):
        return self.history
