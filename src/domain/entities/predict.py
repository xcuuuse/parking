from datetime import date

class Prediction:
    def __init__(self, prediction_date: date, expected_prediction: float):
        self.__prediction_date = date
        self.__expected_prediction = expected_prediction

    @property
    def predict_date(self):
        return self.__prediction_date

    @property
    def expected_prediction(self):
        return self.__expected_prediction

    def predict_workload(self) -> float:
        pass


