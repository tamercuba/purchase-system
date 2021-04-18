from adapters.repositories.in_memory_repo import SaleRepository
from domain.entities import Sale, Salesman
from domain.services import ListSales


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
                'email': 'bbb@aa.com',
                'password': 'ac',
            },
        ]
        self.salesmans = [Salesman(**data) for data in self.salesmans_data]

        self.sale_repo = SaleRepository(initial_values=self.sales)

        self.service = ListSales(sale_repository=self.sale_repo)

    def test_empty_sales(self):
        result = self.service.handle(self.salesmans[0])

        assert not result

    def test_list_valid_salesman(self):
        result = self.service.handle(self.salesmans[1])

        assert len(result) == 2
