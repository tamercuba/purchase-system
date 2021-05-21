from typing import TypedDict

from domain.entities import Sale, SaleDTO, Salesman
from domain.ports.repositories import ISaleRepository
from domain.use_cases.exceptions import CantBeUpdated
from pydantic import ValidationError
from shared.use_case_interface import IUseCase


class UpdateSaleRequest(TypedDict):
    sale_id: str
    salesman: Salesman
    sale: SaleDTO


class UpdateSaleUseCase(IUseCase[UpdateSaleRequest, Sale]):
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

        try:
            updated_sale = Sale(
                id=request['sale_id'],
                salesman_cpf=requisitor.cpf,
                **request['sale'],
            )

            return self._sale_repo.update(updated_sale)
        except ValidationError as e:
            raise CantBeUpdated(entity=Sale, reason=str(e))
