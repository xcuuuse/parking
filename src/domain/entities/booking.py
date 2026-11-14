from datetime import datetime, timedelta


class Booking:
    EXTENSION_TIME = timedelta(minutes=30)

    def __init__(
            self,
            start: datetime,
            end: datetime
    ):
        self.__start = start
        self.__end = end
        self.__status: str = "idk change it please claude"

    @property
    def start(self) -> datetime:
        return self.__start

    @property
    def end(self) -> datetime:
        return self.__end

    def cancel(self) -> None:
        self.__status = ""

    def extend(self) -> None:
        self.__end += self.EXTENSION_TIME
