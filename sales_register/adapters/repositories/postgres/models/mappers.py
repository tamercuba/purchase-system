from adapters.repositories.postgres.models.sale import SaleModel
from adapters.repositories.postgres.models.salesman import SalesmanModel
from domain.entities import Sale, Salesman
from shared.mapper import GenericEntityMapper


class SaleMapper(GenericEntityMapper[SaleModel, Sale]):
    MODEL = SaleModel
    ENTITY = Sale


class SalesmanMapper(GenericEntityMapper[SalesmanModel, Salesman]):
    MODEL = SalesmanModel
    ENTITY = Salesman
