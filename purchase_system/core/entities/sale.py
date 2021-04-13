from datetime import date
from typing import Any, List, Optional, TypedDict

from pydantic import Field, root_validator
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

    @classmethod
    def get_status(cls, cpf: str) -> str:
        if cpf in ['15350946056']:
            return 'approved'

        return 'validating'


class Sale(Entity):
    code: str
    value: float
    date: date
    status: SaleStatus = Field(default='validating')
    salesman_cpf: str

    # pylint: disable=no-self-argument
    @root_validator
    def check_status(cls, values: List[Any]) -> List[Any]:
        cpf = values.get('salesman_cpf')
        values['status'] = SaleStatus.get_status(cpf)
        return values

    def approve(self):
        self._update_status('approved')

    def repprove(self):
        self._update_status('repproved')

    @property
    def cashback(self) -> float:
        if self.value <= 1000:
            return 0.1

        if self.value <= 1500:
            return 0.15

        return 0.2

    @property
    def cashback_result(self) -> float:
        return self.cashback * self.value

    def _update_status(self, value: str):
        self.status = value
