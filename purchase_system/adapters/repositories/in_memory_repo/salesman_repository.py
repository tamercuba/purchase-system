from typing import Optional

from adapters.repositories.in_memory_repo import GenericInMemoryRepository
from domain.entities import Salesman
from domain.ports.repositories import ISalesmanRepository


class SalesmanRepository(
    GenericInMemoryRepository[Salesman], ISalesmanRepository
):
    def get_by_cpf(self, cpf: str) -> Optional[Salesman]:
        result = None
        for entity in self._storage.values():
            if entity.cpf == cpf:
                result = entity
                break

        return result
