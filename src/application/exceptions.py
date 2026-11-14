class ApplicationError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class UserNotFoundError(ApplicationError):
    def __init__(self, message: str):
        super().__init__(message)

class ValidationError(ApplicationError):
    def __init__(self, message: str):
        super().__init__(message)

