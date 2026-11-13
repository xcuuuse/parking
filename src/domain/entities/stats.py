class Stats:
    def __init__(
            self,
            period: str,
            avg_workload: float,
            booking_amount: int
    ):
        self.__period = period
        self.__avg_workload = avg_workload
        self.__booking_amount = booking_amount

    @property
    def period(self):
        return self.__period

    @property
    def avg_workload(self):
        return self.__avg_workload

    @property
    def booking_amount(self):
        return self.__booking_amount

    def count_workload(self) -> float:
        pass

    def make_report(self) -> None:
        pass
