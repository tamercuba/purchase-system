from adapters.repositories.in_memory_repo import GenericInMemoryRepository
from domain.entities import Sale
from domain.ports.repositories import ISaleRepository


class SaleRepository(GenericInMemoryRepository[Sale], ISaleRepository):
    pass
