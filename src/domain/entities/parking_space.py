from src.domain.entities.booking import Booking
from src.domain.entities.parking_session import ParkingSession
from src.domain.entities.location import Location
from src.domain.entities.dynamic_pricing import DynamicPricing
from src.domain.entities.space_stat import SpaceStats
from src.domain .entities.monitoring_rec import MonitoringRec
from src.domain.entities.stats import Stats

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
        self.dynamic_pricing: DynamicPricing = DynamicPricing()
        self.space_stats: SpaceStats = SpaceStats("", True)
        self.monitoring_record: list[MonitoringRec] = []
        self.stats: list[Stats] = []
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

    @property
    def location(self):
        return self.__location

    def occupy(self) -> None:
        self.__status = "occupied"

    def release(self) -> None:
        self.__status = "free"

    def change_state(self, state_id: int):
        pass

    def get_stats(self, period):
        pass #?????????

    

