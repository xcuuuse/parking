from datetime import datetime

class MonitoringRec:
    def __init__(self, time: datetime, state: str):
        self.__time = time
        self.__state = state

    @property
    def time(self):
        return self.__time

    def get_state(self) -> str:
        return self.__state

