from typing import Any, Dict, TypedDict

from domain.ports.authentication_handler import (
    AuthenticationRequest,
    IAuthenticationHandler,
)
from domain.ports.repositories import ISalesmanRepository
from shared.service import IService


class AuthenticateResponse(TypedDict):
    token: Dict[str, Any]


class Authenticate(IService[AuthenticationRequest, AuthenticateResponse]):
    def __init__(
        self,
        salesman_repository: ISalesmanRepository,
        authentication_handler: IAuthenticationHandler,
    ):
        self._repo = salesman_repository
        self._authentication_handler = authentication_handler

    def handle(self, request: AuthenticationRequest) -> AuthenticateResponse:
        return self._authentication_handler.authenticate(
            request=request, salesman_repository=self._repo
        )
