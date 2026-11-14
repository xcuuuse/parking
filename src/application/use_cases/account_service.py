from src.application.exceptions import UserNotFoundError, ValidationError
from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository

class AccountService:
    def __init__(
            self,
            user_repository: UserRepository
    ):
        self.__user_repository = user_repository

    def get_user(self, user_id: int) -> User:
        user = self.__user_repository.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError("User not found")
        return user

    def change_name(self, user_id: int, new_name: str) -> None:
        new_name = new_name.strip()
        if not new_name:
            raise ValidationError("Name can not be empty")
        user = self.get_user(user_id)
        user.change_name(new_name)
        self.__user_repository.save(user)

    def get_balance(self, user_id: int) -> float:
        user = self.get_user(user_id)
        return user.wallet.balance

    def top_up_wallet(self, user_id: int, amount: float) -> float:
        if amount <= 0:
            raise ValidationError("sum has to be more than 0")
        user = self.get_user(user_id)
        user.wallet.top_up(amount)
        self.__user_repository.save(user)
        return user.wallet.balance

    