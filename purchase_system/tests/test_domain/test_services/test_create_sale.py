import pytest
from adapters.repositories.in_memory_repo import SaleRepository
from domain.entities import SaleDTO, Salesman, SaleStatus
from domain.services import CreateSaleRequest, CreateSaleService
from pydantic import ValidationError


class TestCreateSale:
    def setup(self):
        self.salesman_data = {
            'cpf': '123',
            'name': 'Adriano Imperador',
            'email': 'didico@flamengo.com',
            'password': 'a',
        }
        self.salesman = Salesman(**self.salesman_data)
        self.staff_data = {
            'cpf': '456',
            'name': 'Ronaldinho Bruxo',
            'email': 'aaaa@aa.com',
            'password': 'ab',
            'is_staff': True,
        }
        self.staff = Salesman(**self.staff_data)

        self.sale_repo = SaleRepository()

        self.service = CreateSaleService(
            sale_repository=self.sale_repo,
        )

    def test_create_new_sale(self):
        sale_data: SaleDTO = {'code': 'ABC', 'value': 30, 'date': '2020-02-02'}
        request: CreateSaleRequest = {
            'salesman': self.salesman,
            'sale': sale_data,
        }

        result = self.service.handle(request)

        assert result.code == sale_data['code']
        assert result.status == SaleStatus.VALIDATING

    def test_staff_create_new_sale(self):
        sale_data: SaleDTO = {'code': 'ABC', 'value': 30, 'date': '2020-02-02'}
        request: CreateSaleRequest = {
            'salesman': self.staff,
            'sale': sale_data,
        }

        result = self.service.handle(request)

        assert result.code == sale_data['code']
        assert self.staff.is_staff
        assert result.status == SaleStatus.APPROVED

    def test_create_sale_wrong_arg_type(self):
        sale_data: SaleDTO = {
            'code': 'ABC',
            'value': 'a',
            'date': '2020-02-02',
        }
        request: CreateSaleRequest = {
            'salesman': self.salesman,
            'sale': sale_data,
        }

        with pytest.raises(ValidationError):
            self.service.handle(request)
