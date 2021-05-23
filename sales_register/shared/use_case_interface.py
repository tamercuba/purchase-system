from abc import ABC
from typing import Generic, TypeVar

from pydantic import BaseModel

IRequest = TypeVar('IRequest', bound=BaseModel)
IResponse = TypeVar('IResponse', bound=BaseModel)


class IUseCase(ABC, Generic[IRequest, IResponse]):
    def handle(self, request: IRequest) -> IResponse:
        pass
