from domain.entities import Sale, Salesman
from domain.ports.repositories import ISaleRepository
from domain.use_cases.exceptions import CantBeDeleted
from pydantic import BaseModel
from shared.use_case_interface import IUseCase


class DeleteSaleUseCaseRequest(BaseModel):
    sale_id: str
    salesman: Salesman


class DeleteSaleUseCase(IUseCase[DeleteSaleUseCaseRequest, None]):
    def __init__(
        self,
        sale_repository: ISaleRepository,
    ):
        self._sale_repo = sale_repository

    def handle(self, request: DeleteSaleUseCaseRequest) -> None:
        sale = self._sale_repo.get_by_id(request.sale_id)
        requisitor = request.salesman

        if sale.salesman_cpf != requisitor.cpf and not requisitor.is_staff:
            raise CantBeDeleted(entity=Sale, reason='Wrong permission')

        if not sale.can_be_deleted:
            raise CantBeDeleted(entity=Sale, reason='Wrong sale status')

        self._sale_repo.delete(request.sale_id)
