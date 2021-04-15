from datetime import date
from typing import Optional, TypedDict

from domain.entities.value_objects import Cashback
from pydantic import Field
from shared.entities import Entity


class SaleDTO(TypedDict):
    code: str
    value: float
    date: str
    status: Optional[str]


class SaleStatus(str):
    valid_statuses = ['validating', 'approved', 'repproved']

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: str) -> str:
        if not isinstance(v, str):
            raise TypeError('SaleStatus needs to be a string')

        if v not in cls.valid_statuses:
            raise TypeError(
                f'Invalid SaleStatus, valids: {cls.valid_statuses}'
            )

        return v


class Sale(Entity):
    code: str
    value: float
    date: date
    status: SaleStatus = Field(default='validating')
    salesman_cpf: str

    @property
    def cashback(self) -> Cashback:
        return Cashback(sale_value=self.value)

    def approve(self) -> None:
        self._update_status('approved')

    def repprove(self) -> None:
        self._update_status('repproved')

    def _update_status(self, value: str) -> None:
        self.status = value

    @property
    def can_be_updated(self) -> bool:
        return self.status == 'validating'

    @property
    def can_be_deleted(self) -> bool:
        return self.can_be_updated
