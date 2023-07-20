from domain.entities.fields import SaleStatus
from domain.entities.sale import Sale, SaleDTO
from pydantic import EmailStr, SecretStr, field_validator
from shared.entities import Entity


# pylint: disable=no-self-argument
class Salesman(Entity):
    cpf: str
    name: str
    email: EmailStr
    password: SecretStr
    is_staff: bool = False

    def new_sale(self, sale: SaleDTO) -> Sale:
        if self.is_staff:
            sale.status = SaleStatus.APPROVED

        result = Sale(
            **{**sale.dict(exclude_none=True), 'salesman_cpf': self.cpf}
        )

        return result

    @field_validator('is_staff')
    def set_is_staff(cls, value) -> bool:
        return bool(value)

    @field_validator('cpf')
    def remove_special_chars(cls, value: str) -> str:
        return value.replace('.', '').replace('-', '').replace('/', '')
