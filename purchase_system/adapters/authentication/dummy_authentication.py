from purchase_system.domain.ports.authentication_handler import (
    AuthenticationRequest,
    IAuthenticationHandler,
)
from purchase_system.domain.ports.repositories import ISalesmanRepository
from purchase_system.shared.exceptions import EntityNotFound


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
                and request['password'] == salesman.password.get_secret_value()
            )
        except (EntityNotFound, KeyError):
            return False
