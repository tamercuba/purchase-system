from abc import ABC, abstractclassmethod
from typing import ClassVar


class IEntityMapper(ABC):
    MODEL: ClassVar
    ENTITY: ClassVar

    @abstractclassmethod
    def to_entity(cls, model):
        return cls.ENTITY(**model.dict())

    @abstractclassmethod
    def to_model(cls, entity):
        return cls.MODEL(**entity.dict_with_secrets())
