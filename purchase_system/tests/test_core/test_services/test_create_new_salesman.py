import pytest
from adapters.repositories.in_memory_repo import SalesmanRepository
from core.entities import Salesman
from core.services import (
    CreateNewSalesman,
    NewSalesmanRequest,
)
from shared.exceptions import RepeatedEntry


@pytest.mark.asyncio
class TestCreateNewSalesmanService:
    def setup(self):
        self.salesman_data = {
            'cpf': '123',
            'name': 'Adriano Imperador',
            'email': 'didico@flamengo.com',
            'password': 'a',
        }
        self.salesman = Salesman(**self.salesman_data)
        repo = SalesmanRepository(initial_values=[self.salesman])
        self.service = CreateNewSalesman(salesmanRepository=repo)

    async def test_create_new_salesman(self):
        new_salesman = NewSalesmanRequest(
            cpf='456', name='a', email='a', password='a'
        )

        result = await self.service.handle(new_salesman)

        assert result['cpf'] == new_salesman['cpf']
        assert result['id']

    async def test_create_repeated_salesman(self):
        with pytest.raises(RepeatedEntry) as e:
            await self.service.handle(self.salesman_data)
            assert e.id == self.salesman.id

    async def test_create_wrong_request(self):
        with pytest.raises(KeyError):
            await self.service.handle(request={'a': 1})
