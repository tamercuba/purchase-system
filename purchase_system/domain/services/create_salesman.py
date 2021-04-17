from typing import TypedDict

from purchase_system.domain.entities import Salesman
from purchase_system.domain.ports.repositories import ISalesmanRepository
from purchase_system.shared.exceptions import EntityNotFound, RepeatedEntry
from purchase_system.shared.service import IService


class CreateSalesmanRequest(TypedDict):
    cpf: str
    name: str
    email: str
    password: str


class CreateSalesmanResponse(CreateSalesmanRequest):
    id: str


class CreateSalesman(IService[CreateSalesmanRequest, CreateSalesmanResponse]):
    def __init__(self, salesman_repository: ISalesmanRepository):
        self._repo = salesman_repository

    def handle(self, request: CreateSalesmanRequest) -> CreateSalesmanResponse:
        try:
            self._repo.get_by_cpf(request['cpf'])
        except EntityNotFound:
            new_salesman = Salesman(**request)
            self._repo.new(new_salesman)
            response: CreateSalesmanResponse = self.get_response(new_salesman)

            return response

        raise RepeatedEntry('This salesman already exists')

    def get_response(self, salesman: Salesman) -> CreateSalesmanResponse:
        return {
            'id': salesman.id,
            'cpf': salesman.cpf,
            'name': salesman.name,
            'email': salesman.email,
            'password': salesman.password,
        }
