import pytest
from adapters.repositories.in_memory_repo import SaleRepository
from domain.entities import Sale, Salesman
from domain.services import GetSalesmanCashback
from shared.exceptions import InvalidOperation


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
                'is_staff': True,
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

        self.service = GetSalesmanCashback(
            sale_repository=self.sale_repo,
        )

    def test_get_right_cashback(self):
        total = self.service.handle(
            {
                'salesman': self.salesmans[-1],
                'salesman_cpf': self.salesmans[-1].cpf,
            }
        )
        assert total == 500

    def test_get_cashback_salesman_with_no_sale(self):
        total = self.service.handle(
            {
                'salesman': self.salesmans[0],
                'salesman_cpf': self.salesmans[0].cpf,
            }
        )
        assert total == 0

    def test_staff_getting_other_cpf_cashback(self):
        total = self.service.handle(
            {
                'salesman': self.salesmans[0],
                'salesman_cpf': self.salesmans[-1].cpf,
            }
        )
        assert total == 500

    def test_non_staff_getting_other_cpf_cashback(self):
        with pytest.raises(InvalidOperation):
            self.service.handle(
                {
                    'salesman': self.salesmans[-1],
                    'salesman_cpf': self.salesmans[0].cpf,
                }
            )
