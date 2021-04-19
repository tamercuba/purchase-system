import pytest
from adapters.repositories.in_memory_repo import SaleRepository
from domain.entities import Sale, Salesman
from domain.services import GetSalesmanCashback
from shared.exceptions import InvalidOperation


class TestGetSalesmanCashback:
    @pytest.fixture(autouse=True)
    def injector(self, multiple_sales_data, multiple_salesmans_data):
        self.sales_data = multiple_sales_data
        self.sales = [Sale(**data) for data in self.sales_data]

        self.salesmans_data = multiple_salesmans_data
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
