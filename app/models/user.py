import bcrypt 
from models.balance import Balance
from datetime import datetime
from models.transaction import Transaction
from models.transaction_history import TransactionHistory


class User:
    def __init__(self, user_id: str, mail: str, password: str, role: str = 'user'):
        self._user_id = user_id
        self._mail = mail
        self._balance = Balance(user_id=user_id, amount=0)
        self._role = role

        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt() 
        hash = bcrypt.hashpw(bytes, salt)

        self._password = hash 
        

    def get_balance(self) -> float:
        return self._balance.balance()

    def update_balance(self, amount: float, transaction_history: TransactionHistory) -> None:
        t_id = transaction_history.get_last_transaction() + 1
        transaction_history.add_transaction(Transaction(transaction_id=str(t_id), user_id=self._user_id, amount=amount, 
                                                       date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                                                       transaction_type='replenish_user_balance_by_user'))
        self._balance.update_balance(amount)

    def update_balance_action(self, amount: float, transaction_history: TransactionHistory) -> None:
        t_id = transaction_history.get_last_transaction() + 1
        transaction_history.add_transaction(Transaction(transaction_id=str(t_id), user_id=self._user_id, amount=amount, 
                                                       date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                                                       transaction_type='model_prediction'))
        self._balance.update_balance(amount)


    def authenticate(self, mail: str, password: str) -> bool:
        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt() 
        hash = bcrypt.hashpw(bytes, salt)
        return (self._mail == mail and self._password == hash)

    @property
    def role(self) -> str:
        return self._role
    

    