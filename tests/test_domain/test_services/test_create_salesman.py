import pytest

from purchase_system.adapters.repositories.in_memory_repo import (
    SalesmanRepository,
)
from purchase_system.domain.entities import Salesman
from purchase_system.domain.services import (
    CreateSalesman,
    CreateSalesmanRequest,
)
from purchase_system.shared.exceptions import RepeatedEntry


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

    @pytest.mark.parametrize(
        'salesman',
        [
            (
                {
                    'cpf': '123',
                    'name': 'a',
                    'email': 'a@a.com',
                    'password': 'a',
                }
            ),
            (
                {
                    'cpf': '000',
                    'name': 'b',
                    'email': 'didico@flamengo.com',
                    'password': 'a',
                }
            ),
        ],
    )
    def test_create_repeated_salesman(self, salesman):
        with pytest.raises(RepeatedEntry):
            self.service.handle(salesman)

    def test_create_wrong_request(self):
        with pytest.raises(KeyError):
            self.service.handle(request={'a': 1})
