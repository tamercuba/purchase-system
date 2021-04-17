from typing import List

from purchase_system.adapters.repositories.in_memory_repo import (
    GenericInMemoryRepository,
)
from purchase_system.domain.entities import Sale
from purchase_system.domain.ports.repositories import ISaleRepository


class SaleRepository(GenericInMemoryRepository[Sale], ISaleRepository):
    def list_by_cpf(self, cpf: str) -> List[Sale]:
        return list(
            filter(
                lambda sale: sale.salesman_cpf == cpf, self._storage.values()
            )
        )

    def total_salesman_cashback(self, cpf: str) -> float:
        salesman_sales = filter(
            lambda sale: sale.salesman_cpf == cpf, self._storage.values()
        )

        total = 0

        for sale in salesman_sales:
            total += sale.cashback.total

        return total
