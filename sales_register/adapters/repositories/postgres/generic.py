from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Union

from pydantic import BaseModel
from shared.entities import Entity
from shared.mapper import GenericEntityMapper
from sqlalchemy import orm
from sqlalchemy.sql.dml import Delete, Update
from sqlalchemy.sql.selectable import Select

IEntity = TypeVar('IEntity', bound=Union[Entity, BaseModel])


class PostgresRepository(ABC, Generic[IEntity]):
    @property
    @abstractmethod
    def mapper(self) -> GenericEntityMapper:
        pass

    def __init__(self, Session: orm.sessionmaker):
        self._Session = Session

    def _run_get(self, query: Select) -> Entity:
        with self._Session() as session:
            result = session.execute(query).scalars().one_or_none()
            session.commit()

            return self.mapper.to_entity(result) if result else None

    def _run_delete(self, query: Delete) -> None:
        with self._Session() as session:
            session.execute(query)
            session.commit()

    def _run_new(self, entity: Entity) -> Entity:
        with self._Session() as session:
            model = self.mapper.to_model(entity)
            session.add(model)
            session.commit()
            return entity

    def _run_list(self, query: Select) -> list[Entity]:
        with self._Session() as session:
            result_raw = session.execute(query).scalars()

            return [self.mapper.to_entity(model) for model in result_raw]

    def _run_update(self, query: Update) -> None:
        with self._Session() as session:
            session.execute(query)
            session.commit()
