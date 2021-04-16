from adapters.repositories.in_memory_repo import GenericInMemoryRepository
from domain.entities import Salesman
from domain.ports.repositories import ISalesmanRepository


class SalesmanRepository(
    GenericInMemoryRepository[Salesman], ISalesmanRepository
):
    def get_by_cpf(self, cpf: str) -> Salesman:
        return self._get_by_attribute(attr_name='cpf', attr_value=cpf)

    def get_by_email(self, email: str) -> Salesman:
        return self._get_by_attribute(attr_name='email', attr_value=email)
