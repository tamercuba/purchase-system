from domain.entities.sale import Sale, SaleStatus
from pydantic import EmailStr, SecretStr, validator
from shared.entities import Entity


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
    # pylint: disable=no-self-argument
    def set_is_staff(cls, value) -> bool:
        return bool(value)
