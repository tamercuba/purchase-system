from purchase_system.adapters.authentication import DummyAuthenticationHandler
from purchase_system.adapters.repositories.in_memory_repo import (
    SalesmanRepository,
)
from purchase_system.domain.entities import Salesman
from purchase_system.domain.services import Authenticate


class TestAuthenticate:
    def setup(self):
        self.salesmans_data = [
            {
                'cpf': '123',
                'name': 'Adriano Imperador',
                'email': 'didico@flamengo.com',
                'password': 'a',
            },
            {
                'cpf': '345',
                'name': 'Tamer',
                'email': 'tamercuba@gmail.com',
                'password': 'b',
            },
        ]
        self.salesmans = [Salesman(**data) for data in self.salesmans_data]
        repo = SalesmanRepository(initial_values=self.salesmans)
        authentication_handler = DummyAuthenticationHandler()
        self.service = Authenticate(
            salesman_repository=repo,
            authentication_handler=authentication_handler,
        )

    def test_successfull_authentication(self):
        assert self.service.handle(
            {
                'email': self.salesmans[0].email,
                'password': self.salesmans[0].password.get_secret_value(),
            }
        )

    def test_wrong_email(self):
        assert not self.service.handle(
            {
                'email': 'wrong@email.com',
                'password': '',
            }
        )

    def test_wrong_password(self):
        assert not self.service.handle(
            {
                'email': self.salesmans[0].email,
                'password': 'x',
            }
        )

    def test_empty_payload(self):
        assert not self.service.handle({})
