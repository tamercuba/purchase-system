class InvalidEntityType(Exception):
    pass


class _EntityException(Exception):
    def __init__(self, message: str, _id: str):
        self.id = _id
        super().__init__(message)


class RepeatedEntry(_EntityException):
    pass


class EntityNotFound(_EntityException):
    pass
