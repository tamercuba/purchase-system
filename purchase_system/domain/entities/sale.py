from datetime import date
from typing import List, Optional, TypedDict

from domain.entities.value_objects import Cashback
from pydantic import Field
from shared.entities import Entity


class SaleDTO(TypedDict):
    code: str
    value: float
    date: str
    status: Optional[str]


class SaleStatus(str):
    APPROVED = 'Aprovado'
    VALIDATING = 'Em validação'
    REPPROVED = 'Reprovado'

    @classmethod
    @property
    def valid_statuses(cls) -> List[str]:
        return [cls.APPROVED, cls.VALIDATING, cls.REPPROVED]

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: str) -> str:
        if not isinstance(v, str):
            raise TypeError('SaleStatus needs to be a string')

        # pylint: disable=unsupported-membership-test
        if v not in cls.valid_statuses:
            raise TypeError(
                f'Invalid SaleStatus, valids: {cls.valid_statuses}'
            )

        return v


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
