from domain.entities import SaleDTO


class TestSalesmanEntity:
    def test_create_new_sale(self, salesman):
        new_sale_dto = SaleDTO(
            **{
                'code': 'AA',
                'value': 100,
                'date': '2020-09-01',
            }
        )
        sale = salesman.new_sale(new_sale_dto)

        assert sale
        assert sale.salesman_cpf == salesman.cpf
