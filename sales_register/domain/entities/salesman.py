from domain.entities.fields import SaleStatus
from domain.entities.sale import Sale
from pydantic import EmailStr, SecretStr, validator
from shared.entities import Entity


# pylint: disable=no-self-argument
class Salesman(Entity):
    cpf: str
    name: str
    email: EmailStr
    password: SecretStr
    is_staff: bool = False

    def new_sale(self, **kwargs) -> Sale:
        data = {**kwargs, 'status': SaleStatus.APPROVED}

        if not self.is_staff:
            del data['status']

        result = Sale(**{**data, 'salesman_cpf': self.cpf})

        return result

    @validator('is_staff')
    def set_is_staff(cls, value) -> bool:
        return bool(value)

    @validator('cpf')
    def remove_special_chars(cls, value: str) -> str:
        return value.replace('.', '').replace('-', '').replace('/', '')
