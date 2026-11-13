class WorkloadData:
    def __init__(self, empty_places: int, occupied_places: int):
        self.__empty_places = empty_places
        self.__occupied_places = occupied_places

    @property
    def empty_places(self):
        return self.__empty_places

    @property
    def occupied_places(self):
        return self.__occupied_places

    def count_workload(self) -> float:
        return self.__occupied_places / (self.__empty_places + self.__occupied_places)
