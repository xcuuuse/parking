from src.domain.entities.parking_space import ParkingSpace

class Operator:
    def __init__(self, operator_id: int, name: str):
        self.__operator_id = operator_id
        self.__name = name
        self.__parking_spaces: list[ParkingSpace] = []


    @property
    def operator_id(self):
        return self.__operator_id

    @property
    def name(self):
        return self.__name

    @property
    def parking_spaces(self):
        return self.__parking_spaces.copy()

    def add_parking_space(self, parking_space: ParkingSpace) -> None:
        self.__parking_spaces.append(parking_space)

    def change_space_info(self, parking_space_id: int) -> None:
        pass # мб тут подать на вход словарь чтобы инфа заполнялась новой
