from typing import List


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
