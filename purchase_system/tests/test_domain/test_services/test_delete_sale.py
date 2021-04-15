import pytest
from adapters.repositories.in_memory_repo import (
    SaleRepository,
    SalesmanRepository,
)
from domain.entities import Sale, Salesman, SaleStatus
from domain.services import DeleteSaleService
from domain.services.exceptions import CantBeDeleted
from shared.exceptions import EntityNotFound


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

    def test_delete_wrong_status(self):
        new_sale_data = {
            'code': 'a',
            'value': 10,
            'date': '1997-09-01',
            'salesman_cpf': '123',
            'status': SaleStatus.REPPROVED,
        }
        new_sale = Sale(**new_sale_data)

        self.sale_repo.new(new_sale)

        with pytest.raises(CantBeDeleted) as e:
            self.service.handle(
                {'sale_id': new_sale.id, 'salesman_id': self.salesman.id}
            )

            assert 'status' in e

    def test_delete_wrong_cpf(self):
        new_salesman_data = {**self.salesman_data, 'cpf': '456'}
        new_salesman = Salesman(**new_salesman_data)

        self.salesman_repo.new(new_salesman)

        with pytest.raises(CantBeDeleted) as e:
            self.service.handle(
                {'sale_id': self.sale.id, 'salesman_id': new_salesman.id}
            )

            assert 'permission' in e

    def test_delete_wrong_is_staff_with_wrong_cpf(self):
        new_salesman_data = {
            **self.salesman_data,
            'cpf': '789',
            'is_staff': True,
        }
        new_salesman = Salesman(**new_salesman_data)

        self.salesman_repo.new(new_salesman)

        self.service.handle(
            {'sale_id': self.sale.id, 'salesman_id': new_salesman.id}
        )

        total = self.sale_repo.count()

        assert not total

    def test_delete_right_cpf(self):
        total_before = self.sale_repo.count()

        self.service.handle(
            {'sale_id': self.sale.id, 'salesman_id': self.salesman.id}
        )

        total_after = self.sale_repo.count()

        assert total_after == total_before - 1

    def test_delete_nonexistent_sale(self):
        with pytest.raises(EntityNotFound):
            self.service.handle(
                {
                    'sale_id': '93939393939393',
                    'salesman_id': self.salesman.id,
                }
            )
