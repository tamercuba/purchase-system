from typing import Any, Dict, Optional, TypedDict

from domain.entities import Salesman
from domain.ports.repositories import ISalesmanRepository
from shared.exceptions import EntityNotFound, RepeatedEntry
from shared.use_case_interface import IUseCase


class CreateSalesmanRequest(TypedDict, total=False):
    cpf: str
    name: str
    email: str
    password: str
    is_staff: Optional[bool]


class CreateSalesmanResponse(TypedDict):
    id: str
    cpf: str
    name: str
    email: str


class CreateSalesmanUseCase(
    IUseCase[CreateSalesmanRequest, CreateSalesmanResponse]
):
    def __init__(
        self,
        salesman_repository: ISalesmanRepository,
    ):
        self._repo = salesman_repository

    def handle(self, request: CreateSalesmanRequest) -> CreateSalesmanResponse:
        self._check_cpf(request['cpf'])
        self._check_email(request['email'])

        new_salesman = Salesman(**self.get_input_parsed(request))
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

    def get_input_parsed(
        self, request: CreateSalesmanRequest
    ) -> Dict[str, Any]:
        return {**request, 'is_staff': bool(request.get('is_staff'))}
