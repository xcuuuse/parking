from domain.entities.map_object import MapObject
from src.infrastructure.database.sqlite_storage import SqliteStorage
from src.domain.repositories.map_object_repository import MapObjectRepository


class SqliteMapObjectRepository(MapObjectRepository):
    def __init__(self, storage: SqliteStorage):
        self.__storage = storage

    def get_all(self) -> list[MapObject]:
        return self.__storage.map_objects.copy()

    