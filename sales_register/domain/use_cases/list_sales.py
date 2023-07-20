from typing import List

from domain.entities import Sale, Salesman
from domain.ports.repositories import ISaleRepository
from shared.use_case_interface import IUseCase


class ListSalesUseCase(IUseCase[Salesman, List[Sale]]):
    def __init__(
        self,
        sale_repository: ISaleRepository,
    ):
        self._sale_repo = sale_repository

    def handle(self, request: Salesman) -> List[Sale]:
        return self._sale_repo.list_by_cpf(request.cpf)
