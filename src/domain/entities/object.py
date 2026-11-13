from src.domain.entities.location import Location

class Object:
    def __init__(
            self,
            object_id: int,
            location: Location
    ):
        self.__object_id = object_id
        self.__location = location

    @property
    def object_id(self):
        return self.__object_id

    @property
    def location(self):
        return self.__location

    def find_closest(self):
        pass