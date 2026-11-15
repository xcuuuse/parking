from application.exceptions import SpaceNotFoundError
from domain.entities.parking_space import ParkingSpace
from infrastructure.repositories.in_memory_map_object_repository import InMemoryMapObjectRepository
from infrastructure.repositories.in_memory_parking_space_repository import InMemoryParkingSpaceRepository
from infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from src.domain.entities.map_object import MapObject

class MapService:
    def __init__(
            self,
            user_repo: InMemoryUserRepository,
            parking_repo: InMemoryParkingSpaceRepository,
            map_object_repo: InMemoryMapObjectRepository
    ):
        self.__user_repo = user_repo
        self.__parking_repo = parking_repo
        self.__map_object_repo = map_object_repo

    def nearest_spaces(self, user_id: int, amount: int) -> list[ParkingSpace]:
        pass

    def is_location(self, user_id: int) -> bool:
        user = self.__user_repo.get_by_id(user_id)
        return user.location is not None

    def map_objects(self) -> list[MapObject]:
        return self.__map_object_repo.get_all()

    def space_info(self, number: int):
        if not self.__parking_repo.get_by_number(number):
            raise SpaceNotFoundError("Parking space not found")
        return self.__parking_repo.get_by_number(number)


