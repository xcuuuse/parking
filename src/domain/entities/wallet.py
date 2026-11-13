from src.domain.entities.payment import Payment

class Wallet:
    def __init__(self, balance: float = 0.0):
        self.__balance = 0.0
        self.__payments: list[Payment] = []

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def payments(self) -> list[Payment]:
        return self.__payments.copy()

    def top_up(self, amount: float) -> None:
        self.__balance += amount

    def debit_funds(self, amount: float) -> bool:
        if self.__balance <= amount:
            return False
        self.__balance -= amount
        return True



