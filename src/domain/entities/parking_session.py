from datetime import datetime

class ParkingSession:
    def __init__(self, start_time: datetime, end_time: datetime):
        self.__start_time = start_time
        self.__end_time = end_time

    @property
    def start_time(self):
        return self.__start_time

    @property
    def end_time(self):
        return self.__end_time