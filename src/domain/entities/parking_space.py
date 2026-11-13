from src.domain.entities.booking import Booking
from src.domain.entities.parking_session import ParkingSession
from src.domain.entities.location import Location

class ParkingSpace:
    def __init__(
            self,
            number: int,
            price_per_hour: float,
            location: Location,
            status: str = "free"
    ):
        self.__number = number
        self.__status = status
        self.__price_per_hour = price_per_hour
        self.__location = location
        self.__bookings: list[Booking] = []
        self.__parking_sessions: list[ParkingSession] = []

    @property
    def number(self):
        return self.__number

    @property
    def status(self):
        return self.__status

    @property
    def price_per_hour(self):
        return self.__price_per_hour

    @property
    def bookings(self):
        return self.__bookings.copy()

    @property
    def parking_sessions(self):
        return self.__parking_sessions.copy()

    def occupy(self):
        self.__status = "occupied"

    def release(self):
        self.__status = "free"

