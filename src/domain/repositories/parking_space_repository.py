from abc import ABC, abstractmethod
from src.domain.entities.parking_space import ParkingSpace

class ParkingSpaceRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[ParkingSpace]:
        pass

    @abstractmethod
    def get_by_number(self, number: int) -> ParkingSpace | None:
        pass

    @abstractmethod
    def save(self, space: ParkingSpace):
        pass

    