class Model():
    def __init__(self, name: str, cost_per_prediction: float, description: str):
        self._name = name
        self._cost_per_prediction = cost_per_prediction
        self._description = description

    def validate(self, data):
        pass

    def predict(self, valid_data):
        pass

    def get_cost_per_prediction(self) -> float:
        return self._cost_per_prediction