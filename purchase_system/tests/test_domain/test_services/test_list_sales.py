import pytest
from adapters.repositories.in_memory_repo import (
    SaleRepository,
    SalesmanRepository,
)
from domain.entities import Sale, Salesman
from domain.services import ListSales
from shared.exceptions import EntityNotFound


class TestListSales:
    def setup(self):
        self.sales_data = [
            {
                'code': 'a',
                'value': 10,
                'date': '1997-09-01',
                'salesman_cpf': '456',
            },
            {
                'code': 'b',
                'value': 20,
                'date': '1995-09-01',
                'salesman_cpf': '456',
            },
            {
                'code': 'c',
                'value': 30,
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
                'email': 'b',
                'password': 'ac',
            },
        ]
        self.salesmans = [Salesman(**data) for data in self.salesmans_data]

        self.sale_repo = SaleRepository(initial_values=self.sales)
        self.salesman_repo = SalesmanRepository(initial_values=self.salesmans)

        self.service = ListSales(
            sale_repository=self.sale_repo,
            salesman_repository=self.salesman_repo,
        )

    def test_empty_sales(self):
        result = self.service.handle({'salesman_id': self.salesmans[0].id})

        assert not result

    def test_list_valid_salesman(self):
        result = self.service.handle({'salesman_id': self.salesmans[1].id})

        assert len(result) == 2

    def test_invalid_user(self):
        with pytest.raises(EntityNotFound):
            self.service.handle({'salesman_id': 'aaa'})
