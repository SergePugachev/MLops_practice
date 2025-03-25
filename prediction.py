from datetime import datetime


class Prediction:
    def __init__(self, prediction_id: str, user_id: str, date: datetime, data, prediction):
        self._prediction_id = prediction_id
        self._user_id = user_id
        self._date = date
        self._data = data
        self._prediction = prediction