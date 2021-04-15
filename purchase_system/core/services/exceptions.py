class CantBeDeleted(Exception):
    def __init__(self, entity: type, reason: str):
        self.entity = entity
        super().__init__(reason)
