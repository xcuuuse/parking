class SpaceStats:
    def __init__(
            self,
            transport_type: str,
            roof_availability: bool
    ):
        self.__transport_type = transport_type
        self.__roof_availability = roof_availability

    @property
    def transport_type(self) -> str:
        return self.__transport_type

    @property
    def roof_availability(self) -> bool:
        return self.__roof_availability

    def change_info(self, transport_type: str = ""):
        self.__transport_type = transport_type




