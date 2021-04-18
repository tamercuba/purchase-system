from typing import TypedDict

from domain.entities import Sale, SaleDTO, Salesman
from domain.ports.repositories import ISaleRepository
from domain.services.exceptions import CantBeUpdated
from shared.service import IService


class UpdateSaleRequest(TypedDict):
    sale_id: str
    salesman: Salesman
    sale: SaleDTO


class UpdateSale(IService[UpdateSaleRequest, Sale]):
    def __init__(
        self,
        sale_repository: ISaleRepository,
    ):
        self._sale_repo = sale_repository

    def handle(self, request: UpdateSaleRequest) -> Sale:
        sale = self._sale_repo.get_by_id(request['sale_id'])
        requisitor = request['salesman']

        if sale.salesman_cpf != requisitor.cpf and not requisitor.is_staff:
            raise CantBeUpdated(entity=Sale, reason='Wrong permission')

        if not sale.can_be_deleted:
            raise CantBeUpdated(entity=Sale, reason='Wrong sale status')

        updated_sale = Sale(id=request['sale_id'], **request['sale'])

        return self._sale_repo.update(updated_sale)
