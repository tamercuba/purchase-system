from typing import List


class SaleStatus(str):
    APPROVED = 'Aprovado'
    VALIDATING = 'Em validação'
    REPPROVED = 'Reprovado'

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: str) -> str:
        if not isinstance(v, str):
            raise TypeError('SaleStatus needs to be a string')

        valid_statuses = [cls.APPROVED, cls.VALIDATING, cls.REPPROVED]
        if v not in valid_statuses:
            raise TypeError(f'Invalid SaleStatus, valids: {valid_statuses}')

        return v
