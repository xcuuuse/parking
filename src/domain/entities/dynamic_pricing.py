from src.domain.entities.workload_data import WorkloadData

class DynamicPricing:
    def __init__(
            self,
            current_price: float = 0.0
    ):
        self.__current_price = current_price

    @property
    def current_price(self):
        return self.__current_price

    def count_price(self, data: WorkloadData):
        pass # ???

