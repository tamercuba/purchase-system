from typing import TypedDict

from purchase_system.domain.entities import Salesman
from purchase_system.domain.ports.repositories import ISaleRepository
from purchase_system.shared.exceptions import InvalidOperation
from purchase_system.shared.service import IService


class GetSalesmanCashbackRequest(TypedDict):
    salesman: Salesman
    salesman_cpf: str


class GetSalesmanCashbackResponse(TypedDict):
    cashback_total: float


class GetSalesmanCashback(
    IService[GetSalesmanCashbackRequest, GetSalesmanCashbackResponse]
):
    def __init__(
        self,
        sale_repository: ISaleRepository,
    ):
        self._sale_repo = sale_repository

    def handle(
        self, request: GetSalesmanCashbackRequest
    ) -> GetSalesmanCashbackResponse:
        requisitor = request['salesman']
        requisited_cpf = request['salesman_cpf']

        if requisitor.is_staff or requisited_cpf == requisitor.cpf:
            return self._sale_repo.total_salesman_cashback(requisited_cpf)

        raise InvalidOperation()
