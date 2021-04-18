import pytest

from purchase_system.adapters.repositories.in_memory_repo import (
    SaleRepository,
    SalesmanRepository,
)
from purchase_system.domain.entities import Sale, Salesman
from purchase_system.domain.services import GetSalesmanCashback
from purchase_system.shared.exceptions import EntityNotFound


class TestGetSalesmanCashback:
    def setup(self):
        self.sales_data = [
            {
                'code': 'a',
                'value': 1000,
                'date': '1997-09-01',
                'salesman_cpf': '456',
            },
            {
                'code': 'b',
                'value': 2000,
                'date': '1995-09-01',
                'salesman_cpf': '456',
            },
            {
                'code': 'c',
                'value': 3000,
                'date': '1295-09-01',
                'salesman_cpf': '789',
            },
        ]
        self.sales = [Sale(**data) for data in self.sales_data]

        self.salesmans_data = [
            {
                'cpf': '123',
                'name': 'Adriano Imperador',
                'email': 'didico@flamengo.com',
                'password': 'a',
            },
            {
                'cpf': '456',
                'name': 'Tamer',
                'email': 'bbb@aa.com',
                'password': 'ac',
            },
        ]
        self.salesmans = [Salesman(**data) for data in self.salesmans_data]

        self.sale_repo = SaleRepository(initial_values=self.sales)
        self.salesman_repo = SalesmanRepository(initial_values=self.salesmans)

        self.service = GetSalesmanCashback(
            sale_repository=self.sale_repo,
            salesman_repository=self.salesman_repo,
        )

    def test_get_right_cashback(self):
        total = self.service.handle({'salesman_id': self.salesmans[-1].id})
        assert total == 500

    def test_get_cashback_salesman_with_no_sale(self):
        total = self.service.handle({'salesman_id': self.salesmans[0].id})
        assert total == 0

    def test_get_cashback_wrong_salesman_id(self):
        with pytest.raises(EntityNotFound):
            self.service.handle({'salesman_id': 'aaa'})
