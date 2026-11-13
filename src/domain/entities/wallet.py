from src.domain.entities.payment import Payment

class Wallet:
    def __init__(self):
        self.__balance = 0.0
        self.__payments: list[Payment] = []

    @property
    def balance(self):
        return self.__balance

    @property
    def payments(self):
        return self.__payments.copy()

    def top_up(self, amount: float):
        self.__balance += amount

    def debit_funds(self, amount: float) -> bool:
        if self.__balance <= amount:
            return False
        self.__balance -= amount
        return True



