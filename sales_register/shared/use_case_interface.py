from abc import ABC
from typing import Generic, TypedDict, TypeVar

IRequest = TypeVar('IRequest', bound=TypedDict)
IResponse = TypeVar('IResponse', bound=TypedDict)


class IUseCase(ABC, Generic[IRequest, IResponse]):
    def handle(self, request: IRequest) -> IResponse:
        pass
