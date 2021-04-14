from abc import ABC
from typing import Generic, TypedDict, TypeVar

IRequest = TypeVar('IRequest', bound=TypedDict)
IResponse = TypeVar('IResponse', bound=TypedDict)


class IService(ABC, Generic[IRequest, IResponse]):
    async def handle(self, request: IRequest, **kwargs) -> IResponse:
        pass
