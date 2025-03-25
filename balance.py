class Balance:
    def __init__(self, user_id: str, amount: float):
        self._user_id = user_id
        self._amount = amount

    def update_balance(self, amount: float) -> None:
        self._amount += amount

    @property
    def balance(self) -> float:
        return self._amount