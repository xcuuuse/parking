from infrastructure.repositories.in_memory_user_repository import InMemoryUserRepository


class OccupancyService:
    def __init__(
            self,
            user_repo: InMemoryUserRepository,
    ):