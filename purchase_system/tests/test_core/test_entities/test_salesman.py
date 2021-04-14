import pytest
from core.entities import SaleDTO
from pydantic import ValidationError


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

    def test_create_new_sale_wrong_data(self, salesman):
        wrong_data = {
            'code': 'A',
            'value': 'Errado',
            'date': '2020-09-01',
        }

        with pytest.raises(ValidationError) as e:
            salesman.new_sale(**wrong_data)
            assert 'value is not a valid float' in e
