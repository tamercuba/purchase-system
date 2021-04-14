from abc import ABC
from typing import Any, Generic, List, Optional, TypeVar, get_args

from shared.entity import Entity
from shared.exceptions import InvalidEntityType

IEntity = TypeVar('IEntity', bound=Entity)


class GenericInMemoryRepository(ABC, Generic[IEntity]):
    def __init__(self, initial_values: List[IEntity] = None):
        initial_storage = (
            {e.id: e for e in initial_values} if initial_values else {}
        )
        self._storage = initial_storage

    async def new(self, entity: IEntity) -> None:
        self.check_entity_type(entity)
        self._storage[entity.id] = entity

    async def get_by_id(self, _id: str) -> Optional[IEntity]:
        result = self._storage.get(_id, None)
        return result

    async def count(self) -> int:
        return len(self._storage)

    def check_entity_type(self, entity: Any) -> None:
        if not isinstance(entity, self._entity_type):
            raise InvalidEntityType(
                f'{entity.__class__.__name__} must '
                f'be {self._entity_type.__name__} type'
            )

    @property
    def _entity_type(self):
        return get_args(self.__class__.__orig_bases__[0])[0]
