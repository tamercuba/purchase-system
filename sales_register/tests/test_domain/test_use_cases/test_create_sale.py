import pytest
from adapters.repositories.in_memory_repo import SaleRepository
from domain.entities import SaleDTO, Salesman, SaleStatus
from domain.use_cases import CreateSaleUseCase, CreateSaleUseCaseRequest


class TestCreateSale:
    @pytest.fixture(autouse=True)
    def injector(self, salesman_data):
        self.salesman_data = salesman_data
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

        self.use_case = CreateSaleUseCase(
            sale_repository=self.sale_repo,
        )

    def test_create_new_sale(self):
        sale_data = SaleDTO(
            **{'code': 'ABC', 'value': 30, 'date': '2020-02-02'}
        )
        request = CreateSaleUseCaseRequest(
            **{
                'salesman': self.salesman,
                'sale': sale_data,
            }
        )

        result = self.use_case.handle(request)

        assert result.code == sale_data.code
        assert result.status == SaleStatus.VALIDATING

    def test_staff_create_new_sale(self):
        sale_data = SaleDTO(
            **{'code': 'ABC', 'value': 30, 'date': '2020-02-02'}
        )
        request = CreateSaleUseCaseRequest(
            **{
                'salesman': self.staff,
                'sale': sale_data,
            }
        )

        result = self.use_case.handle(request)

        assert result.code == sale_data.code
        assert self.staff.is_staff
        assert result.status == SaleStatus.APPROVED
