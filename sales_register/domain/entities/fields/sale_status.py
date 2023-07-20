from enum import Enum


class SaleStatus(str, Enum):
    APPROVED = 'Aprovado'
    VALIDATING = 'Em validação'
    REPPROVED = 'Reprovado'

    @property
    def can_be_updated(self) -> bool:
        return self == self.__class__.VALIDATING
