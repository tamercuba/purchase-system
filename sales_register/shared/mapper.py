from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Union

from pydantic import BaseModel

from .entities import Entity

IEntity = TypeVar('IEntity', bound=Union[Entity, BaseModel])
IModel = TypeVar('IModel')


class GenericEntityMapper(ABC, Generic[IModel, IEntity]):
    MODEL: IModel
    ENTITY: IEntity

    @abstractmethod
    def to_entity(cls, model):
        return cls.ENTITY(**model.model_dump())

    @abstractmethod
    def to_model(cls, entity):
        return cls.MODEL(**entity.dict_with_secrets())
