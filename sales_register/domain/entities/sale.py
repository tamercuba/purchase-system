from datetime import date
from typing import Optional

from domain.entities.fields import SaleStatus
from domain.entities.value_objects import Cashback
from pydantic import BaseModel
from shared.entities import Entity


class SaleDTO(BaseModel):
    code: str
    value: float
    date: str
    status: Optional[str] = None


class Sale(Entity):
    code: str
    value: float
    date: date
    salesman_cpf: str
    status: SaleStatus = SaleStatus.VALIDATING

    @property
    def cashback(self) -> Cashback:
        return Cashback(sale_value=self.value)

    def approve(self) -> None:
        self._update_status(SaleStatus.APPROVED)

    def repprove(self) -> None:
        self._update_status(SaleStatus.REPPROVED)

    def _update_status(self, value: SaleStatus) -> None:
        self.status = value

    @property
    def can_be_updated(self) -> bool:
        return self.status.can_be_updated

    @property
    def can_be_deleted(self) -> bool:
        return self.can_be_updated
