from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    balance: Mapped[float] = mapped_column(Float, default=0.0)
    pos_x: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    pos_y: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    coord_system: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)


class ParkingSpaceModel(Base):
    __tablename__ = "parking_spaces"
    number: Mapped[int] = mapped_column(Integer, primary_key=True)
    status: Mapped[str] = mapped_column(String(10))
    price_per_hour: Mapped[float] = mapped_column(Float)
    pos_x: Mapped[Optional[float]] = mapped_column(Float)
    pos_y: Mapped[Optional[float]] = mapped_column(Float)
    coord_system: Mapped[str] = mapped_column(String(20))

class ParkingSessionModel(Base):
    __tablename__ = "parking_sessions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"), nullable=True)
    space_number: Mapped[Optional[int]] = mapped_column(ForeignKey("parking_spaces.number"), nullable=True)
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


class PaymentModel(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    session_id: Mapped[int] = mapped_column(ForeignKey("parking_sessions.id"))
    amount: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(20))


class MapObjectModel(Base):
    __tablename__ = "map_objects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    object_type: Mapped[str] = mapped_column(String(30))
    pos_x: Mapped[float] = mapped_column(Float)
    pos_y: Mapped[float] = mapped_column(Float)
    coord_system: Mapped[str] = mapped_column(String(20))

class BookingModel(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"), nullable=True)
    space_number: Mapped[Optional[int]] = mapped_column(ForeignKey("parking_spaces.number"), nullable=True)
    start: Mapped[datetime] = mapped_column(DateTime)
    end: Mapped[datetime] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String(20))

