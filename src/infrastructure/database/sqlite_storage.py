from sqlalchemy import create_engine, delete, select
from sqlalchemy.orm import Session

from src.domain.entities.booking import Booking
from src.domain.entities.location import Location
from src.domain.entities.map_object import MapObject
from src.domain.entities.parking_session import ParkingSession
from src.domain.entities.parking_space import ParkingSpace
from src.domain.entities.payment import Payment
from src.domain.entities.user import User
from src.infrastructure.database.models import (
    Base, BookingModel, MapObjectModel, ParkingSessionModel,
    ParkingSpaceModel, PaymentModel, UserModel,
)