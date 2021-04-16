from typing import List

from adapters.repositories.in_memory_repo import GenericInMemoryRepository
from domain.entities import Sale
from domain.ports.repositories import ISaleRepository


class SaleRepository(GenericInMemoryRepository[Sale], ISaleRepository):
    def list_by_cpf(self, cpf: str) -> List[Sale]:
        return list(
            filter(
                lambda sale: sale.salesman_cpf == cpf, self._storage.values()
            )
        )
