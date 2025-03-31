from datetime import datetime
from models.user import User
from models.model import Model
from models.prediction import Prediction
from models.transaction_history import TransactionHistory
from models.prediction_history import PredictionHistory

class MLService:
    def __init__(self,model: Model, transaction_history: TransactionHistory, prediction_history: PredictionHistory):
        self._model = model.name
        self._transaction_history = transaction_history
        self._prediction_history = prediction_history


    def process_prediction_request(self, user: User, model: Model, data):
        model = model()
        valid_data = model.validate(data)
        
        if user.get_balance() < model.get_cost_per_prediction():
            raise ValueError("Insufficient funds!")
        
        predictions = model.predict(valid_data)
        user.update_balance_action(amount=model.get_cost_per_prediction(), transaction_history=self._transaction_history)
        p_id = self._prediction_history.get_last_prediction() + 1
        self._prediction_history.add_prediction(Prediction(prediction_id=str(p_id), user_id=user._user_id, 
                                                           date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                                                           data=data, prediction=predictions))
        
        return predictions