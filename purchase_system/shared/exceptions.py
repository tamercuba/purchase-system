class InvalidEntityType(Exception):
    pass


class RepeatedEntry(Exception):
    def __init__(self, message: str, _id: str):
        self.id = _id
        super().__init__(message)
