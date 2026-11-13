from datetime import datetime


class Booking:
    def __init__(
            self,
            start: datetime,
            end: datetime
    ):
        self.__start = start
        self.__end = end

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    def cancel(self):
        pass

    def extend(self):
        pass
