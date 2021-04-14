from typing import TypedDict

from core.entities import Salesman
from core.ports.repositories import ISalesmanRepository
from shared.service import IService


class NewSalesmanRequest(TypedDict):
    cpf: str
    name: str
    email: str
    password: str


class NewSalesmanResponse(NewSalesmanRequest):
    id: str


class CreateNewSalesman(IService[NewSalesmanRequest, NewSalesmanResponse]):
    def __init__(self, salesmanRepository: ISalesmanRepository):
        self._repo = salesmanRepository

    async def handle(
        self, request: NewSalesmanRequest, **kwargs
    ) -> NewSalesmanResponse:
        existing_salesman = await self._repo.get_by_cpf(request['cpf'])
        if existing_salesman:
            response: NewSalesmanResponse = self.get_response(
                existing_salesman
            )
        else:
            new_salesman = Salesman(**{request})
            await self._repo.new(new_salesman)
            response: NewSalesmanResponse = self.get_response(new_salesman)

        return response

    def get_response(self, salesman: Salesman) -> NewSalesmanResponse:
        return {
            'id': salesman.id,
            'cpf': salesman.cpf,
            'name': salesman.name,
            'email': salesman.email,
            'password': salesman.password,
        }
