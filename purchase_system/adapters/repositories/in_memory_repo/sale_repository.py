from adapters.repositories.in_memory_repo import GenericInMemoryRepository
from core.entities import Sale
from core.ports.repositories import ISaleRepository


class SaleRepository(GenericInMemoryRepository[Sale], ISaleRepository):
    pass
