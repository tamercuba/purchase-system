import asyncio

import pytest
from adapters.repositories.in_memory_repo import SalesmanRepository
from core.entities import Salesman


@pytest.mark.asyncio
class TestSalesmanRepo:
    def setup(self):
        self.repo = SalesmanRepository()
        self.new_salesman = Salesman(
            **{
                'cpf': '123',
                'name': 'Adriano Imperador',
                'email': 'didico@flamengo.com',
                'password': 'a',
            }
        )

        asyncio.run(self.repo.new(self.new_salesman))

    async def test_get_by_cpf(self):
        result = await self.repo.get_by_cpf(self.new_salesman.cpf)

        assert result
        assert result == self.new_salesman

    @pytest.mark.parametrize('cpf', [
        ('111'), (1), (False)
    ])
    async def test_get_by_wrong_cpf(self, cpf):
        result = await self.repo.get_by_cpf(cpf)

        assert result is None
