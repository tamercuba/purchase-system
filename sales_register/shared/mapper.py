from abc import ABC, abstractclassmethod
from typing import Generic, TypeVar, Union

from pydantic import BaseModel

from .entities import Entity

IEntity = TypeVar('IEntity', bound=Union[Entity, BaseModel])
IModel = TypeVar('IModel')


class IEntityMapper(ABC, Generic[IModel, IEntity]):
    MODEL: IModel
    ENTITY: IEntity

    @abstractclassmethod
    def to_entity(cls, model):
        return cls.ENTITY(**model.dict())

    @abstractclassmethod
    def to_model(cls, entity):
        return cls.MODEL(**entity.dict_with_secrets())
