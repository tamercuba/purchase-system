from typing import Optional

from domain.entities import Salesman
from domain.ports.repositories import ISalesmanRepository
from pydantic import BaseModel
from shared.exceptions import EntityNotFound, RepeatedEntry
from shared.use_case_interface import IUseCase


class CreateSalesmanUseCaseRequest(BaseModel):
    cpf: str
    name: str
    email: str
    password: str
    is_staff: Optional[bool]


class CreateSalesmanUseCaseResponse(BaseModel):
    id: str
    cpf: str
    name: str
    email: str


class CreateSalesmanUseCase(
    IUseCase[CreateSalesmanUseCaseRequest, CreateSalesmanUseCaseResponse]
):
    def __init__(
        self,
        salesman_repository: ISalesmanRepository,
    ):
        self._repo = salesman_repository

    def handle(
        self, request: CreateSalesmanUseCaseRequest
    ) -> CreateSalesmanUseCaseResponse:
        self._check_cpf(request.cpf)
        self._check_email(request.email)

        new_salesman = Salesman(
            **{
                **request.dict(exclude_none=True),
                'is_staff': bool(request.is_staff),
            }
        )
        self._repo.new(new_salesman)

        return CreateSalesmanUseCaseResponse(
            **{
                'id': new_salesman.id,
                'cpf': new_salesman.cpf,
                'name': new_salesman.name,
                'email': new_salesman.email,
            }
        )

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
