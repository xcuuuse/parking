from typing import Optional
from datetime import datetime, timedelta


class ParkingSession:
    def __init__(
            self,
            start_time: datetime,
            end_time: Optional[datetime] = None
    ):
        self.__start_time = start_time
        self.__end_time = end_time

    @property
    def start_time(self) -> datetime:
        return self.__start_time

    @property
    def end_time(self) -> Optional[datetime]:
        return self.__end_time

    def complete(self) -> None:
        self.__end_time = datetime.now()

    def calculate_cost(self) -> float:
        return 0.0

    def count_duration(self) -> float:
        pass #????????

    

