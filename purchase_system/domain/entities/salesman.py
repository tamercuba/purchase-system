from pydantic import EmailStr, Field, SecretStr

from purchase_system.domain.entities.sale import Sale, SaleStatus
from purchase_system.shared.entities import Entity


class Salesman(Entity):
    cpf: str
    name: str
    email: EmailStr
    password: SecretStr
    is_staff: bool = Field(default=False)

    def new_sale(self, **kwargs) -> Sale:
        data = {**kwargs}

        if self.is_staff and 'status' not in data:
            data['status'] = SaleStatus.APPROVED

        result = Sale(**{**data, 'salesman_cpf': self.cpf})

        return result
