from typing import Optional

from src.infrastructure.database.sqlite_storage import SqliteStorage
from src.domain.repositories.user_repository import UserRepository
from src.domain.entities.user import User


class SqliteUserRepository(UserRepository):
    def __init__(self, storage: SqliteStorage):
        self.__storage = storage

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.__storage.users.get(user_id)

    def save(self, user: User) -> None:
        self.__storage.users[user.id] = user
        self.__storage.flush()

        