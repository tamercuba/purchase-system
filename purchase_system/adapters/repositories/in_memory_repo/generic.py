from abc import ABC
from typing import Generic, List, Optional, TypeVar

from shared.entity import Entity

IEntity = TypeVar('IEntity', bound=Entity)


class GenericInMemoryRepository(ABC, Generic[IEntity]):
    def __init__(self, initial_values: List[IEntity] = None):
        initial_storage = (
            {e.id: e for e in initial_values} if initial_values else {}
        )
        self._storage = initial_storage

    async def new(self, entity: IEntity) -> None:
        self._storage[entity.id] = entity

    async def get_by_id(self, _id: str) -> Optional[IEntity]:
        result = self._storage.get(_id, None)
        return result

    async def count(self) -> int:
        return len(self._storage)
