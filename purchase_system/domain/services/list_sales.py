from typing import List, NewType, TypedDict

from purchase_system.domain.entities import Sale
from purchase_system.domain.ports.repositories import (
    ISaleRepository,
    ISalesmanRepository,
)
from purchase_system.shared.service import IService


class ListSalesRequest(TypedDict):
    salesman_id: str


class SaleResponse(TypedDict):
    id: str
    code: str
    value: float
    data: str
    cashback_value: float
    cashback_total: float
    status: str


ListSalesResponse = NewType('ListSalesReponse', List[SaleResponse])


class ListSales(IService[ListSalesRequest, ListSalesResponse]):
    def __init__(
        self,
        sale_repository: ISaleRepository,
        salesman_repository: ISalesmanRepository,
    ):
        self._sale_repo = sale_repository
        self._salesman_repo = salesman_repository

    def handle(self, request: ListSalesRequest) -> ListSalesResponse:
        salesman = self._salesman_repo.get_by_id(request['salesman_id'])
        result = self._sale_repo.list_by_cpf(salesman.cpf)
        return self.get_response(result)

    def get_response(self, sales: List[Sale]) -> ListSalesResponse:
        return list(
            map(
                lambda sale: {
                    'id': sale.id,
                    'code': sale.code,
                    'value': sale.value,
                    'data': str(sale.date),
                    'cashback_value': sale.cashback.value,
                    'cashback_total': sale.cashback.total,
                    'status': sale.status,
                },
                sales,
            )
        )
