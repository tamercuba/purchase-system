from domain.entities import Sale, SaleDTO, Salesman
from domain.ports.repositories import ISaleRepository
from pydantic import BaseModel
from shared.use_case_interface import IUseCase


class CreateSaleUseCaseRequest(BaseModel):
    salesman: Salesman
    sale: SaleDTO


class CreateSaleUseCase(IUseCase[CreateSaleUseCaseRequest, Sale]):
    def __init__(
        self,
        sale_repository: ISaleRepository,
    ):
        self._sale_repo = sale_repository

    def handle(self, request: CreateSaleUseCaseRequest) -> Sale:
        requisitor = request.salesman
        new_sale = requisitor.new_sale(request.sale)

        return self._sale_repo.new(new_sale)
