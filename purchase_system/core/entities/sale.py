from datetime import date
from typing import Optional, TypedDict

from pydantic import Field
from shared.entity import Entity


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

    def approve(self):
        self._update_status('approved')

    def repprove(self):
        self._update_status('repproved')

    def _update_status(self, value: str):
        self.status = value
