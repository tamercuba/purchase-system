import pytest
from adapters.repositories.in_memory_repo import (
    SaleRepository,
    SalesmanRepository,
)
from domain.entities import Sale, Salesman
from domain.services import UpdateSale
from domain.services.exceptions import CantBeUpdated
from shared.exceptions import EntityNotFound


class TestUpdateSale:
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

        self.service = UpdateSale(
            sale_repository=self.sale_repo,
            salesman_repository=self.salesman_repo,
        )

    def test_update_wrong_status(self):
        new_sale_data = {
            'code': 'a',
            'value': 10,
            'date': '1997-09-01',
            'salesman_cpf': '123',
            'status': 'repproved',
        }
        new_sale = Sale(**new_sale_data)

        self.sale_repo.new(new_sale)

        with pytest.raises(CantBeUpdated) as e:
            self.service.handle(
                {
                    'sale_id': new_sale.id,
                    'salesman_id': self.salesman.id,
                    'sale': new_sale_data,
                }
            )

            assert 'status' in e

    def test_update_wrong_cpf(self):
        new_salesman_data = {**self.salesman_data, 'cpf': '456'}
        new_salesman = Salesman(**new_salesman_data)

        self.salesman_repo.new(new_salesman)

        with pytest.raises(CantBeUpdated) as e:
            self.service.handle(
                {
                    'sale_id': self.sale.id,
                    'salesman_id': new_salesman.id,
                    'sale': self.sale_data,
                }
            )

            assert 'permission' in e

    def test_update_wrong_is_stuff_with_wrong_cpf(self):
        new_salesman_data = {
            **self.salesman_data,
            'cpf': '789',
            'is_stuff': True,
        }
        new_salesman = Salesman(**new_salesman_data)

        updated_sale_data = {**self.sale_data, 'code': 'B'}

        self.salesman_repo.new(new_salesman)

        result = self.service.handle(
            {
                'sale_id': self.sale.id,
                'salesman_id': new_salesman.id,
                'sale': updated_sale_data,
            }
        )

        assert result == self.sale
        assert result.dict() != self.sale.dict()

    def test_update_right_cpf(self):
        updated_sale_data = {**self.sale_data, 'code': 'B'}

        result = self.service.handle(
            {
                'sale_id': self.sale.id,
                'salesman_id': self.salesman.id,
                'sale': updated_sale_data,
            }
        )

        assert result == self.sale
        assert result.dict() != self.sale.dict()

    def test_update_nonexistent_sale(self):
        updated_sale_data = {**self.sale_data, 'code': 'B'}

        with pytest.raises(EntityNotFound):
            self.service.handle(
                {
                    'sale_id': '93939393939393',
                    'salesman_id': self.salesman.id,
                    'sale': updated_sale_data,
                }
            )
