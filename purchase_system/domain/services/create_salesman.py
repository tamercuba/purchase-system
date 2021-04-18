from typing import TypedDict

from domain.entities import Salesman
from domain.ports.repositories import ISalesmanRepository
from shared.exceptions import EntityNotFound, RepeatedEntry
from shared.service import IService


class CreateSalesmanRequest(TypedDict):
    cpf: str
    name: str
    email: str
    password: str


class CreateSalesmanResponse(TypedDict):
    id: str
    cpf: str
    name: str
    email: str


class CreateSalesman(IService[CreateSalesmanRequest, CreateSalesmanResponse]):
    def __init__(self, salesman_repository: ISalesmanRepository):
        self._repo = salesman_repository

    def handle(self, request: CreateSalesmanRequest) -> CreateSalesmanResponse:
        self._check_cpf(request['cpf'])
        self._check_email(request['email'])

        new_salesman = Salesman(**request)
        self._repo.new(new_salesman)
        response: CreateSalesmanResponse = self.get_response(new_salesman)

        return response

    def _check_cpf(self, cpf: str) -> None:
        try:
            self._repo.get_by_cpf(cpf)
            raise RepeatedEntry('Repeated CPF', info={'cpf': cpf})
        except EntityNotFound:
            pass

    def _check_email(self, email: str) -> None:
        try:
            self._repo.get_by_email(email)
            raise RepeatedEntry('Repeated email', info={'email': email})
        except EntityNotFound:
            pass

    def get_response(self, salesman: Salesman) -> CreateSalesmanResponse:
        return {
            'id': salesman.id,
            'cpf': salesman.cpf,
            'name': salesman.name,
            'email': salesman.email,
        }
