from sqlalchemy import create_engine, delete, select
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

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

class SqliteStorage:
    def __init__(self, path: str = "parking.db"):
        self.__engine = create_engine(f"sqlite:///{path}")
        Base.metadata.create_all(self.__engine)
        self.users: dict[int, User] = {}
        self.spaces: dict[int, ParkingSpace] = {}
        self.map_objects: list[MapObject] = []


    def __load(self) -> None:
        with Session(self.__engine) as db:
            for row in db.scalars(select(UserModel)):
                location = None
                if row.pos.x is not None:
                    location = Location(row.pos_x, row.pos_y, row.coord_system)
                user = User(row.id, row.name, location)
                user.wallet.top_up(row.balance)
                self.users[row.id] = user

            for row in db.scalars(select(MapObjectModel)):
                location = Location(row.pos_x, row.pos_y, row.coord_system)
                self.map_objects.append(MapObject(row.object_type, location))

            for row in db.scalars(select(BookingModel)):
                booking = Booking(row.start, row.end)
                if row.status == "cancelled":
                    booking.cancel()
                elif row.status == "used":
                    booking.mark_used()
                if row.user_id in self.users:
                    self.users[row.user_id].add_booking(booking)
                if row.space_number in self.spaces:
                    self.spaces[row.space_number].add_booking(booking)

            sessions: dict[int, ParkingSession] = {}
            for row in db.scalars(select(ParkingSessionModel)):
                session = ParkingSession(row.start_time, row.end_time)
                sessions[row.id] = session
                if row.user_id in self.users:
                    self.users[row.user_id].add_session(session)
                if row.space_number in self.spaces:
                    self.spaces[row.space_number].add_session(session)

            for row in db.scalars(select(PaymentModel)):
                if row.user_id not in self.users or row.session_id not in sessions:
                    continue
                payment = Payment(row.amount, sessions[row.session_id])
                if row.status == "completed":
                    payment.execute()
                self.users[row.user_id].wallet.add_payment(payment)

    def flush(self) -> None:
        booking_rows: dict[int, BookingModel] = {}
        session_rows: dict[int, ParkingSessionModel] = {}

        def booking_row(booking: Booking) -> BookingModel:
            key = id(booking)
            if key not in booking_rows:
                booking_rows[key] = BookingModel(
                    id=len(booking_rows) + 1, start=booking.start,
                    end=booking.end, status=booking.status,
                )
            return booking_rows[key]

        def session_row(session: ParkingSession) -> ParkingSessionModel:
            key = id(session)
            if key not in session_rows:
                session_rows[key] = ParkingSessionModel(
                    id=len(session_rows) + 1, start_time=session.start_time,
                    end_time=session.end_time,
                )
            return session_rows[key]

        rows: list = []
        for space in self.spaces.values():
            rows.append(ParkingSpaceModel(
                number=space.number, status=space.status, price_per_hour=space.price_per_hour,
                pos_x=space.location.pos_x, pos_y=space.location.pos_y,
                coord_system=space.location.coord_system,
            ))
            for booking in space.bookings:
                booking_row(booking).space_number = space.number
            for session in space.parking_sessions:
                session_row(session).space_number = space.number

        payment_rows: list[PaymentModel] = []
        for user in self.users.values():
            location = user.location
            rows.append(UserModel(
                id=user.id, name=user.name, balance=user.wallet.balance,
                pos_x=location.pos_x if location else None,
                pos_y=location.pos_y if location else None,
                coord_system=location.coord_system if location else None,
            ))
            for booking in user.bookings:
                booking_row(booking).user_id = user.id
            for session in user.parking_sessions:
                session_row(session).user_id = user.id
            for payment in user.wallet.payments:
                payment_rows.append(PaymentModel(
                    id=len(payment_rows) + 1, user_id=user.id,
                    session_id=session_row(payment.parking_session).id,
                    amount=payment.amount, status=payment.check_status(),
                ))

        for number, map_object in enumerate(self.map_objects, start=1):
            rows.append(MapObjectModel(
                id=number, object_type=map_object.object_type,
                pos_x=map_object.location.pos_x, pos_y=map_object.location.pos_y,
                coord_system=map_object.location.coord_system,
            ))

        with Session(self.__engine) as db, db.begin():
            for model in (PaymentModel, BookingModel, ParkingSessionModel,
                          UserModel, ParkingSpaceModel, MapObjectModel):
                db.execute(delete(model))
            db.add_all(rows)
            db.flush()
            db.add_all(list(booking_rows.values()) + list(session_rows.values()))
            db.flush()
            db.add_all(payment_rows)

