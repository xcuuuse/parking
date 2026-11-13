from src.domain.entities.parking_space import ParkingSpace
class Recommendation:
    def __init__(self, mark: float, reason: str):
        self.__mark = mark
        self.__reason = reason

    @property
    def mark(self):
        return self.__mark

    @property
    def reason(self):
        return self.__reason

    def rate_space(self) -> float:
        pass

