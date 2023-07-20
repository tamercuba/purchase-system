import pytest
from adapters.repositories.in_memory_repo import SalesmanRepository
from domain.entities import Salesman
from domain.use_cases import (
    CreateSalesmanUseCase,
    CreateSalesmanUseCaseRequest,
)
from shared.exceptions import RepeatedEntry


class TestCreateSalesman:
    @pytest.fixture(autouse=True)
    def injector(self, salesman_data):
        self.salesman_data = salesman_data
        self.salesman = Salesman(**self.salesman_data)
        repo = SalesmanRepository(initial_values=[self.salesman])
        self.use_case = CreateSalesmanUseCase(salesman_repository=repo)

    @pytest.mark.parametrize(
        '_request',
        [
            (
                CreateSalesmanUseCaseRequest(
                    **{
                        'cpf': '11111',
                        'name': 'a',
                        'email': 'a@gmail.com',
                        'password': 'a',
                    }
                )
            ),
            (
                CreateSalesmanUseCaseRequest(
                    **{
                        'cpf': '22222',
                        'name': 'b',
                        'email': 'b@gmail.com',
                        'password': 'a',
                        'is_staff': True,
                    }
                )
            ),
            (
                CreateSalesmanUseCaseRequest(
                    **{
                        'cpf': '33333',
                        'name': 'c',
                        'email': 'c@gmail.com',
                        'password': 'a',
                        'is_staff': False,
                    }
                )
            ),
            (
                CreateSalesmanUseCaseRequest(
                    **{
                        'cpf': '44444',
                        'name': 'd',
                        'email': 'd@gmail.com',
                        'password': 'a',
                    }
                )
            ),
        ],
    )
    def test_create_salesman(self, _request):
        result = self.use_case.handle(_request)

        assert result.cpf == _request.cpf
        assert result.id

    @pytest.mark.parametrize(
        '_request',
        [
            (
                CreateSalesmanUseCaseRequest(
                    **{
                        'cpf': '123',
                        'name': 'a',
                        'email': 'a@a.com',
                        'password': 'a',
                    }
                )
            ),
            (
                CreateSalesmanUseCaseRequest(
                    **{
                        'cpf': '000',
                        'name': 'b',
                        'email': 'didico@flamengo.com',
                        'password': 'a',
                    }
                )
            ),
        ],
    )
    def test_create_repeated_salesman(self, _request):
        with pytest.raises(RepeatedEntry):
            self.use_case.handle(_request)
