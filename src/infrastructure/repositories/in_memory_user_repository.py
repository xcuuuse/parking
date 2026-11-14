from src.domain.repositories.user_repository import UserRepository, User


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.__users: dict[int, User] = {}

    def get_by_id(self, user_id: int) -> User | None:
        return self.__users[user_id]

    def save(self, user: User):
        self.__users[user.id] = user #?????? почему мы храним это в словаре, если у юзера есть свойство id






