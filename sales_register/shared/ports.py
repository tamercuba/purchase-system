from typing import TypedDict, TypeVar

IRequest = TypeVar('IRequest', bound=TypedDict)
IResponse = TypeVar('IResponse', bound=TypedDict)
