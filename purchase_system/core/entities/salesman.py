from core.entities.sale import Sale, SaleDTO
from shared.entity import Entity


class Salesman(Entity):
    cpf: str
    name: str
    email: str
    password: str

    def new_sale(self, **kwargs) -> Sale:
        saleDto: SaleDTO = {**kwargs, 'salesman_cpf': self.cpf}
        return Sale(**saleDto)
