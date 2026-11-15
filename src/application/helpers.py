import math
from typing import Optional

from domain.entities.booking import Booking
from domain.entities.map_object import MapObject
from domain.entities.parking_session import ParkingSession
from domain.entities.parking_space import ParkingSpace
from domain.repositories.parking_space_repository import ParkingSpaceRepository
from src.domain.entities.user import User

BASE_POINT = (0.0, 0.0)

def count_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

def find_active_booking(user: User) -> Optional[Booking]:
    for i in user.bookings:
        if i.status == "active":
            return i

    return None

def find_active_session(user: User) -> Optional[ParkingSession]:
    for i in user.parking_sessions:
        if i.end_time is None:
            return i
    return None

def find_by_booking(repo: ParkingSpaceRepository, object: MapObject):
    pass #idk help


def session_price(session: ParkingSession):
    return session.count_duration() * 0.01




