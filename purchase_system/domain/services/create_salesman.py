from typing import Callable, TypedDict, Optional, Any, Dict
from domain.entities import Salesman
from domain.ports.repositories import ISalesmanRepository
from shared.exceptions import EntityNotFound, RepeatedEntry
from shared.service import IService


class CreateSalesmanRequest(TypedDict):
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


class CreateSalesman(IService[CreateSalesmanRequest, CreateSalesmanResponse]):
    def __init__(
        self,
        salesman_repository: ISalesmanRepository,
        hash_algo: Callable = None,
    ):
        self._repo = salesman_repository
        self._hash_algo = hash_algo

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

    def _hash_password(self, password: str) -> str:
        if self._hash_algo:
            return self._hash_algo(password)

        return password

    def get_input_parsed(self, request: CreateSalesmanRequest) -> Dict[str, Any]:
        result = {
            **request,
            'password': self._hash_password(request['password'])
        }

        if result.get('is_staff') is None:
            del result['is_staff']

        return result
