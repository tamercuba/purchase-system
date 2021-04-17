from typing import TypedDict

from domain.entities import Sale, SaleDTO
from domain.ports.repositories import ISaleRepository, ISalesmanRepository
from shared.service import IService


class CreateSaleRequest(TypedDict):
    salesman_id: str
    sale: SaleDTO


class CreateSaleService(IService[CreateSaleRequest, Sale]):
    def __init__(
        self,
        sale_repository: ISaleRepository,
        salesman_repository: ISalesmanRepository,
    ):
        self._sale_repo = sale_repository
        self._salesman_repo = salesman_repository

    def handle(self, request: CreateSaleRequest) -> Sale:
        salesman = self._salesman_repo.get_by_id(request['salesman_id'])
        new_sale = salesman.new_sale(**request['sale'])

        return self._sale_repo.new(new_sale)
