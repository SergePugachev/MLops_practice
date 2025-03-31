from models.transaction import Transaction


class TransactionHistory:
    def __init__(self):
        self._transactions = []

    def add_transaction(self, transaction: Transaction) -> None:
        self._transactions.append(transaction)

    def get_transactions_by_user(self, user_id: str) -> list[Transaction]:
        return [t for t in self._transactions if t._user_id == user_id]

    def get_all_transactions(self) -> list[Transaction]:
        return self._transactions.copy()
    
    def get_last_transaction(self) -> int:
        return max([int(t._transaction_id) for t in self._transactions])