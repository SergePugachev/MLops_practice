from prediction import Prediction


class PredictionHistory:
    def __init__(self):
        self._predictions = []

    def add_prediction(self, prediction: Prediction) -> None:
        self._prediction.append(prediction)

    def get_predictions_by_user(self, user_id: str) -> list[Prediction]:
        return [t for t in self._predictions if t._user_id == user_id]

    def get_all_predictions(self) -> list[Prediction]:
        return self._predictions.copy()
    
    def get_last_prediction(self) -> int:
        return max([int(t._prediction_id) for t in self._predictions])