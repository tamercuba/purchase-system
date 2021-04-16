from domain.ports.authentication_handler import (
    AuthenticationRequest,
    IAuthenticationHandler,
)
from domain.ports.repositories import ISalesmanRepository
from shared.exceptions import EntityNotFound


class DummyAuthenticationHandler(IAuthenticationHandler[bool]):
    def authenticate(
        self,
        request: AuthenticationRequest,
        salesman_repository: ISalesmanRepository,
    ) -> bool:
        try:
            salesman = salesman_repository.get_by_email(request['email'])
            return (
                request['email'] == salesman.email
                and request['password'] == salesman.password
            )
        except (EntityNotFound, KeyError):
            return False
