from typing import List, TypedDict

from domain.entities import Salesman
from domain.ports.repositories import ISaleRepository
from shared.use_case_interface import IUseCase


class SaleResponse(TypedDict):
    id: str
    code: str
    value: float
    date: str
    cashback_value: float
    cashback_total: float
    status: str


class ListSalesUseCase(IUseCase[Salesman, List[Salesman]]):
    def __init__(
        self,
        sale_repository: ISaleRepository,
    ):
        self._sale_repo = sale_repository

    def handle(self, request: Salesman) -> List[Salesman]:
        requisitor = request
        return self._sale_repo.list_by_cpf(requisitor.cpf)
