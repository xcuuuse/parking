from src.domain.entities.location import Location
from src.domain.entities.wallet import Wallet
from src.domain.entities.parking_session import ParkingSession
from src.domain.entities.booking import Booking

class User:
    def __init__(
            self,
            user_id: int,
            name: str,
            location: Location,
            wallet: Wallet,

    ):
        self.__id = id
        self.__name = name
        self.__location = location
        self.__wallet = wallet
        self.__parking_sessions: list[ParkingSession] = []
        self.__bookings: list[Booking] = []

    def update_location(self):
        pass

