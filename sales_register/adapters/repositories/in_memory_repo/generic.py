from abc import ABC
from typing import Any, Generic, List, TypeVar, get_args

from shared.entities import Entity
from shared.exceptions import (
    EntityAttributeDoesntExist,
    EntityNotFound,
    InvalidEntityType,
)

IEntity = TypeVar('IEntity', bound=Entity)


class GenericInMemoryRepository(ABC, Generic[IEntity]):
    def __init__(self, initial_values: List[IEntity] = []):
        initial_storage = (
            {str(e.id): e for e in initial_values} if initial_values else {}
        )
        self._storage = initial_storage

    def new(self, entity: IEntity) -> IEntity:
        self.check_entity_type(entity)
        self._storage[entity.id] = entity

        return entity

    def get_by_id(self, _id: str) -> IEntity:
        try:
            result = self._storage[_id]
            return result
        except KeyError:
            raise EntityNotFound(
                f'Cant found {self._entity_type} with id: {_id}',
                info={'id': _id},
            )

    def count(self) -> int:
        return len(self._storage)

    def delete(self, _id: str) -> None:
        try:
            if _id not in self._storage:
                raise KeyError
            del self._storage[_id]
        except KeyError:
            print('aaaaaaaaaaa')
            raise EntityNotFound(
                f'Cant found {self._entity_type} with id: {_id}',
                info={'id': _id},
            )

    def update(self, entity: IEntity) -> IEntity:
        try:
            if entity.id not in self._storage:
                raise KeyError
            self._storage[entity.id] = entity
        except KeyError:
            raise EntityNotFound(
                f'Cant found {self._entity_type} with id: {entity.id}',
                info={'id': entity.id},
            )

        return entity

    def check_entity_type(self, entity: Any) -> None:
        if not isinstance(entity, self._entity_type):
            raise InvalidEntityType(
                f'{entity.__class__.__name__} must '
                f'be {self._entity_type.__name__} type'
            )

    def _get_by_attribute(self, attr_name: str, attr_value: Any) -> IEntity:
        # breakpoint()
        if not self._entity_type.hasattr(attr_name):
            raise EntityAttributeDoesntExist(
                entity=self._entity_type, attr=attr_name
            )

        for entity in self._storage.values():
            if getattr(entity, attr_name) == attr_value:
                return entity

        raise EntityNotFound(
            f'Cant found {self._entity_type} with {attr_name}: {attr_value}'
        )

    @property
    def _entity_type(self):
        # breakpoint()
        return get_args(self.__class__.__orig_bases__[0])[0]
