from typing import List, NewType, TypedDict

from domain.entities import Sale, Salesman
from domain.ports.repositories import ISaleRepository
from shared.service import IService


class SaleResponse(TypedDict):
    id: str
    code: str
    value: float
    data: str
    cashback_value: float
    cashback_total: float
    status: str


ListSalesResponse = NewType('ListSalesReponse', List[SaleResponse])


class ListSales(IService[Salesman, ListSalesResponse]):
    def __init__(
        self,
        sale_repository: ISaleRepository,
    ):
        self._sale_repo = sale_repository

    def handle(self, request: Salesman) -> ListSalesResponse:
        requisitor = request
        result = self._sale_repo.list_by_cpf(requisitor.cpf)
        return self.get_response(result)

    def get_response(self, sales: List[Sale]) -> ListSalesResponse:
        return list(
            map(
                lambda sale: {
                    'id': sale.id,
                    'code': sale.code,
                    'value': sale.value,
                    'date': str(sale.date),
                    'cashback_value': sale.cashback.value,
                    'cashback_total': sale.cashback.total,
                    'status': sale.status,
                },
                sales,
            )
        )
