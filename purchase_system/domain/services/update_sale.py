from typing import TypedDict

from purchase_system.domain.entities import Sale, SaleDTO
from purchase_system.domain.ports.repositories import (
    ISaleRepository,
    ISalesmanRepository,
)
from purchase_system.domain.services.exceptions import CantBeUpdated
from purchase_system.shared.service import IService


class UpdateSaleRequest(TypedDict):
    sale_id: str
    salesman_id: str
    sale: SaleDTO


class UpdateSale(IService[UpdateSaleRequest, Sale]):
    def __init__(
        self,
        sale_repository: ISaleRepository,
        salesman_repository: ISalesmanRepository,
    ):
        self._sale_repo = sale_repository
        self._salesman_repo = salesman_repository

    def handle(self, request: UpdateSaleRequest) -> Sale:
        sale = self._sale_repo.get_by_id(request['sale_id'])
        salesman = self._salesman_repo.get_by_id(request['salesman_id'])

        if sale.salesman_cpf != salesman.cpf and not salesman.is_staff:
            raise CantBeUpdated(entity=Sale, reason='Wrong permission')

        if not sale.can_be_deleted:
            raise CantBeUpdated(entity=Sale, reason='Wrong sale status')

        updated_sale = Sale(id=request['sale_id'], **request['sale'])

        return self._sale_repo.update(updated_sale)
