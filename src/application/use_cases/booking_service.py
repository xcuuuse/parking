from datetime import datetime

from application.exceptions import ValidationError, SpaceUnavailableError

from infrastructure.repositories.in_memory_parking_space_repository import InMemoryParkingSpaceRepository
from infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository
from src.domain.entities.booking import Booking
from src.domain.entities.parking_space import ParkingSpace


class BookingService:
    def __init__(
            self,
            user_repo: InMemoryUserRepository,
            parking_repo: InMemoryParkingSpaceRepository
    ):
        self.__user_repo = user_repo
        self.__parking_repo = parking_repo

    def book(
            self,
            user_id: int,
            space_number: int,
            start: datetime,
            end: datetime
    ):
        if start >= end:
            raise ValidationError("Start time can not be more than end time")
        user = self.__user_repo.get_by_id(user_id)
        space = self.__parking_repo.get_by_number(space_number)
        if user.bookings:
            raise ValueError("User already has active bookings")
        if space.status != "free":
            raise SpaceUnavailableError("Parking space is not free")
        booking = Booking(start, end)
        user.add_booking(booking), space.add_booking(booking)
        space.status = "booked"
        self.__user_repo.save(user), self.__parking_repo.save(space)

    def extend(self, user_id: int) -> Booking:
        pass #помоги тут везде где пасс

    def cancel(self, user_id: int) -> None:
        pass

    def current_booking(self, user_id: int) -> tuple[ParkingSpace, Booking] | None:
        pass





