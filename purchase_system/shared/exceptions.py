from typing import Any, Dict, Optional


class InvalidEntityType(Exception):
    pass


class EntityAttributeDoesntExist(Exception):
    def __init__(self, entity: Any, attr: str):
        self.entity = entity
        self.attr = attr
        super().__init__(f'{attr} doesnt exist in {entity}')


class _EntityException(Exception):
    def __init__(self, message: str, info: Optional[Dict[str, Any]] = None):
        self.info = info
        super().__init__(message)


class RepeatedEntry(_EntityException):
    pass


class EntityNotFound(_EntityException):
    pass
