import pytest
from core.entities.salesman import Salesman, SaleDTO


@pytest.fixture
def salesman_data():
    return {
        'cpf': '123',
        'name': 'Adriano Imperador',
        'email': 'didico@flamengo.com',
        'senha': 'a'
    }

@pytest.fixture
def salesman(salesman_data):
    return Salesman(**salesman_data)

class TestSalesmanEntity:
    def test_create_new_sale(self, salesman):
        new_sale_data: SaleDTO = {
            'code': 'AA',
            'value': 100,
            'date': '2020-09-01',
        }
        sale = salesman.new_sale(**new_sale_data)

        assert sale
        assert sale.salesman_cpf == salesman.cpf