from typing import List

from domain.entities import Salesman
from domain.ports.repositories import ISaleRepository
from shared.use_case_interface import IUseCase


class ListSalesUseCase(IUseCase[Salesman, List[Salesman]]):
    def __init__(
        self,
        sale_repository: ISaleRepository,
    ):
        self._sale_repo = sale_repository

    def handle(self, request: Salesman) -> List[Salesman]:
        return self._sale_repo.list_by_cpf(request.cpf)
