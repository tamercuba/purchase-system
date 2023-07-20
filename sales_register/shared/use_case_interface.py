from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from pydantic import BaseModel

IRequest = TypeVar('IRequest', bound=BaseModel)
IResponse = TypeVar('IResponse', bound=Any)


class IUseCase(ABC, Generic[IRequest, IResponse]):
    @abstractmethod
    def handle(self, request: IRequest) -> IResponse:
        pass
