from domain.entities import Salesman
from domain.ports.repositories import ISaleRepository
from pydantic import BaseModel
from shared.exceptions import InvalidOperation
from shared.use_case_interface import IUseCase


class GetSalesmanCashbackUseCaseRequest(BaseModel):
    salesman: Salesman
    salesman_cpf: str


class GetSalesmanCashbackUseCase(
    IUseCase[GetSalesmanCashbackUseCaseRequest, float]
):
    def __init__(
        self,
        sale_repository: ISaleRepository,
    ):
        self._sale_repo = sale_repository

    def handle(self, request: GetSalesmanCashbackUseCaseRequest) -> float:
        requisitor = request.salesman
        requisited_cpf = request.salesman_cpf

        if requisitor.is_staff or requisited_cpf == requisitor.cpf:
            return self._sale_repo.total_salesman_cashback(requisited_cpf)

        raise InvalidOperation()
