import pytest
from adapters.repositories.in_memory_repo import SaleRepository
from domain.entities import Sale, Salesman
from domain.services import ListSalesService


class TestListSales:
    @pytest.fixture(autouse=True)
    def injector(self, multiple_sales_data, multiple_salesmans_data):
        self.sales_data = multiple_sales_data
        self.sales = [Sale(**data) for data in self.sales_data]

        self.salesmans_data = multiple_salesmans_data
        self.salesmans = [Salesman(**data) for data in self.salesmans_data]

        self.sale_repo = SaleRepository(initial_values=self.sales)

        self.service = ListSalesService(sale_repository=self.sale_repo)

    def test_empty_sales(self):
        result = self.service.handle(self.salesmans[0])

        assert not result

    def test_list_valid_salesman(self):
        result = self.service.handle(self.salesmans[1])

        assert len(result) == 2
