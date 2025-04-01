from datetime import datetime


class Transaction:
    def __init__(self, transaction_id: str, user_id: str, amount: float, date: datetime, transaction_type: str):
        self._transaction_id = transaction_id
        self._user_id = user_id
        self._amount = amount
        self._date = date
        self._transaction_type = transaction_type

        