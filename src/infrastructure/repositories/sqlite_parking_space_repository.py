from typing import Optional

from domain.entities.parking_space import ParkingSpace
from src.infrastructure.database.sqlite_storage import SqliteStorage
from src.domain.repositories.parking_space_repository import ParkingSpaceRepository


class SqliteParkingSpaceRepository(ParkingSpaceRepository):
    def __init__(self, storage: SqliteStorage):
        self.__storage = storage

    def get_all(self) -> list[ParkingSpace]:
        return list(self.__storage.spaces.values())

    def get_by_number(self, number: int) -> Optional[ParkingSpace]:
        return self.__storage.spaces.get(number)

    def save(self, space: ParkingSpace) -> None:
        self.__storage.spaces[space.number] = space
        self.__storage.flush()