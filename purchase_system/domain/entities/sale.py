from datetime import date
from typing import Optional, TypedDict

from domain.entities.fields import SaleStatus
from domain.entities.value_objects import Cashback
from pydantic import Field
from shared.entities import Entity


class SaleDTO(TypedDict):
    code: str
    value: float
    date: str
    status: Optional[str]


class Sale(Entity):
    code: str
    value: float
    date: date
    status: SaleStatus = Field(default=SaleStatus.VALIDATING)
    salesman_cpf: str

    @property
    def cashback(self) -> Cashback:
        return Cashback(sale_value=self.value)

    def approve(self) -> None:
        self._update_status(SaleStatus.APPROVED)

    def repprove(self) -> None:
        self._update_status(SaleStatus.REPPROVED)

    def _update_status(self, value: str) -> None:
        self.status = value

    @property
    def can_be_updated(self) -> bool:
        return self.status == SaleStatus.VALIDATING

    @property
    def can_be_deleted(self) -> bool:
        return self.can_be_updated
