from datetime import datetime
from models.user import User
from models.transaction import Transaction
from models.transaction_history import TransactionHistory
from models.prediction import Prediction
from models.prediction_history import PredictionHistory



class AdminUser(User):
    def __init__(self, user_id: str, mail: str, password: str):
        super().__init__(user_id, mail, password, role='admin')

    def replenish_user_balance(self, user: User, amount: float, transaction_history: TransactionHistory) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        t_id = transaction_history.get_last_transaction() + 1
        transaction_history.add_transaction(Transaction(transaction_id=t_id, user_id=user._user_id, amount=amount, 
                                                       date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                                                       transaction_type='replenish_user_balance_by_admin'))
        self._balance.update_balance(amount)


    def view_all_transactions(self, transaction_history: TransactionHistory) -> list[Transaction]:
        return transaction_history.get_all_transactions()
    
    def view_user_transactions(self, user_id: str, transaction_history: TransactionHistory) -> list[Transaction]:
        return transaction_history.get_transactions_by_user(user_id=user_id)
    
    def view_all_predictions(self, prediction_history: PredictionHistory) -> list[Prediction]:
        return prediction_history.get_all_predictions()
    
    def view_user_predictions(self, user_id: str, prediction_history: PredictionHistory) -> list[Prediction]:
        return prediction_history.get_predictions_by_user(user_id=user_id)