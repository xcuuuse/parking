import sys

from PyQt6.QtWidgets import QApplication

from src.application.use_cases.account_service import AccountService
from src.application.use_cases.booking_service import BookingService
from src.application.use_cases.map_service import MapService
from src.application.use_cases.occupancy_service import OccupancyService
from src.application.use_cases.payment_service import PaymentService
from src.application.use_cases.route_service import RouteService
from src.infrastructure.database.sqlite_storage import SqliteStorage
from src.infrastructure.repositories.sqlite_map_object_repository import SqliteMapObjectRepository
from src.infrastructure.repositories.sqlite_parking_space_repository import SqliteParkingSpaceRepository
from src.infrastructure.repositories.sqlte_user_repository import SqliteUserRepository
from src.infrastructure.seed_data import DEFAULT_USER_ID, create_map_objects, seed_parking_spaces, seed_users
from src.presentation.windows.main_window import MainWindow


def main() -> None:
    storage = SqliteStorage("parking.db")
    user_repo = SqliteUserRepository(storage)
    parking_repo = SqliteParkingSpaceRepository(storage)
    map_object_repo = SqliteMapObjectRepository(storage)
    if storage.is_empty():
        seed_users(user_repo)
        seed_parking_spaces(parking_repo)
        storage.add_map_objects(create_map_objects())


    map_service = MapService(user_repo, parking_repo, map_object_repo)
    booking_service = BookingService(user_repo, parking_repo)
    occupancy_service = OccupancyService(user_repo, parking_repo)
    payment_service = PaymentService(user_repo, parking_repo)
    route_service = RouteService(user_repo)
    account_service = AccountService(user_repo)

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow(
        DEFAULT_USER_ID,
        map_service, booking_service, occupancy_service,
        payment_service, route_service, account_service,
    )
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
