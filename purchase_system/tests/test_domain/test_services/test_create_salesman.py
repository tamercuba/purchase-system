import pytest
from adapters.repositories.in_memory_repo import SalesmanRepository
from domain.entities import Salesman
from domain.services import CreateSalesman, CreateSalesmanRequest
from shared.exceptions import RepeatedEntry


class TestCreateSalesmanService:
    def setup(self):
        self.salesman_data = {
            'cpf': '123',
            'name': 'Adriano Imperador',
            'email': 'didico@flamengo.com',
            'password': 'a',
        }
        self.salesman = Salesman(**self.salesman_data)
        repo = SalesmanRepository(initial_values=[self.salesman])
        self.service = CreateSalesman(salesman_repository=repo)

    def test_create_salesman(self):
        new_salesman = CreateSalesmanRequest(
            cpf='456', name='a', email='aa@gmail.com', password='a'
        )

        result = self.service.handle(new_salesman)

        assert result['cpf'] == new_salesman['cpf']
        assert result['id']

    def test_create_repeated_salesman(self):
        with pytest.raises(RepeatedEntry) as e:
            self.service.handle(self.salesman_data)
            assert e.id == self.salesman.id

    def test_create_wrong_request(self):
        with pytest.raises(KeyError):
            self.service.handle(request={'a': 1})
