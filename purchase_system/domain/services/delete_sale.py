from typing import TypedDict

from domain.entities import Sale
from domain.ports.repositories import ISaleRepository, ISalesmanRepository
from domain.services.exceptions import CantBeDeleted
from shared.service import IService


class DeleteSaleRequest(TypedDict):
    sale_id: str
    salesman_id: str


class DeleteSaleService(IService[DeleteSaleRequest, None]):
    def __init__(
        self,
        sale_repository: ISaleRepository,
        salesman_repository: ISalesmanRepository,
    ):
        self._sale_repo = sale_repository
        self._salesman_repo = salesman_repository

    async def handle(self, request: DeleteSaleRequest, **kwargs) -> None:
        sale = await self._sale_repo.get_by_id(request['sale_id'])
        salesman = await self._salesman_repo.get_by_id(request['salesman_id'])

        if sale.salesman_cpf != salesman.cpf and not salesman.is_stuff:
            raise CantBeDeleted(entity=Sale, reason='Wrong permission')

        if not sale.can_be_deleted:
            raise CantBeDeleted(entity=Sale, reason='Wrong sale status')

        await self._sale_repo.delete(request['sale_id'])
