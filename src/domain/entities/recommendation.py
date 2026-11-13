from src.domain.entities.parking_space import ParkingSpace
from src.domain.entities.booking import Booking
class Recommendation:
    def __init__(
            self,
            score: float,
            reason: str,
            parking_space: ParkingSpace
    ):
        self.__score = score
        self.__reason = reason
        self.__parking_space = parking_space


    @property
    def reason(self):
        return self.__reason

    @property
    def parking_space(self):
        return self.__parking_space

    def rate_space(self) -> float:
        return self.__score

