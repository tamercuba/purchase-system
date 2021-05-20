from adapters.repositories.postgres.models.sale import SaleModel
from adapters.repositories.postgres.models.salesman import SalesmanModel
from domain.entities import Sale, Salesman
from shared.mapper import IEntityMapper


class SaleMapper(IEntityMapper):
    MODEL = SaleModel
    ENTITY = Sale


class SalesmanMapper(IEntityMapper):
    MODEL = SalesmanModel
    ENTITY = Salesman
