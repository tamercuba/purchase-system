import pytest
from adapters.repositories.in_memory_repo import (
    SaleRepository,
    SalesmanRepository,
)
from core.entities import Sale, Salesman
from core.services import DeleteSaleService
from core.services.exceptions import CantBeDeleted


@pytest.mark.asyncio
class TestDeleteSale:
    def setup(self):
        self.sale_data = {
            'code': 'a',
            'value': 10,
            'date': '1997-09-01',
            'salesman_cpf': '123',
        }
        self.sale = Sale(**self.sale_data)

        self.salesman_data = {
            'cpf': '123',
            'name': 'Adriano Imperador',
            'email': 'didico@flamengo.com',
            'password': 'a',
        }
        self.salesman = Salesman(**self.salesman_data)

        self.sale_repo = SaleRepository(initial_values=[self.sale])
        self.salesman_repo = SalesmanRepository(initial_values=[self.salesman])

        self.service = DeleteSaleService(
            sale_repository=self.sale_repo,
            salesman_repository=self.salesman_repo,
        )

    async def test_delete_wrong_status(self):
        new_sale_data = {
            'code': 'a',
            'value': 10,
            'date': '1997-09-01',
            'salesman_cpf': '123',
            'status': 'repproved'
        }
        new_sale = Sale(**new_sale_data)

        await self.sale_repo.new(new_sale)

        with pytest.raises(CantBeDeleted) as e:
            await self.service.handle(
                {'sale_id': new_sale.id, 'salesman_id': self.salesman.id}
            )

            assert 'status' in e

    async def test_delete_wrong_cpf(self):
        new_salesman_data = {**self.salesman_data, 'cpf': '456'}
        new_salesman = Salesman(**new_salesman_data)

        await self.salesman_repo.new(new_salesman)

        with pytest.raises(CantBeDeleted) as e:
            await self.service.handle(
                {'sale_id': self.sale.id, 'salesman_id': new_salesman.id}
            )

            assert 'permission' in e

    async def test_delete_wrong_is_stuff_with_wrong_cpf(self):
        new_salesman_data = {
            **self.salesman_data,
            'cpf': '789',
            'is_stuff': True,
        }
        new_salesman = Salesman(**new_salesman_data)

        await self.salesman_repo.new(new_salesman)

        await self.service.handle(
            {'sale_id': self.sale.id, 'salesman_id': new_salesman.id}
        )

        total = await self.sale_repo.count()

        assert not total

    async def test_delete_right_cpf(self):
        total_before = await self.sale_repo.count()

        await self.service.handle({
            'sale_id': self.sale.id, 'salesman_id': self.salesman.id
        })

        total_after = await self.sale_repo.count()


        assert total_after == total_before - 1
