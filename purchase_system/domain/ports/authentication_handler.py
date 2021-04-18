from abc import ABC
from typing import Generic, TypedDict, TypeVar

from domain.ports.repositories import ISalesmanRepository

IResponse = TypeVar('IResponse')


class AuthenticationRequest(TypedDict):
    email: str
    password: str


class IAuthenticationHandler(ABC, Generic[IResponse]):
    def authenticate(
        self,
        request: AuthenticationRequest,
        salesman_repository: ISalesmanRepository,
    ) -> IResponse:
        pass
