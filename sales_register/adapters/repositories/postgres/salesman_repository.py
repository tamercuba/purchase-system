from typing import Optional

from adapters.repositories.postgres.generic import PostgresRepository
from adapters.repositories.postgres.models import SalesmanMapper, SalesmanModel
from domain.entities import Salesman
from domain.ports.repositories import ISalesmanRepository
from shared.exceptions import EntityNotFound


class SalesmanRepository(PostgresRepository, ISalesmanRepository):
    model = SalesmanModel
    mapper = SalesmanMapper

    def get_by_id(self, _id: str) -> Salesman:
        query = self._select.where(self.model.id == _id)

        salesman: Salesman = self._run_get(query)

        if not salesman:
            raise EntityNotFound(
                f'Cant found Sale with id: {_id}',
                info={'id': _id},
            )

        return salesman

    def get_by_cpf(self, cpf: str) -> Optional[Salesman]:
        query = self._select.where(self.model.cpf == cpf)

        salesman: Salesman = self._run_get(query)

        if not salesman:
            raise EntityNotFound(
                f'Cant found Sale with id: {cpf}',
                info={'id': cpf},
            )

        return salesman

    def get_by_email(self, email: str) -> Optional[Salesman]:
        query = self._select.where(self.model.email == email)

        salesman: Salesman = self._run_get(query)

        if not salesman:
            raise EntityNotFound(
                f'Cant found Sale with id: {email}',
                info={'id': email},
            )

        return salesman

    def new(self, salesman: Salesman) -> Salesman:
        return self._run_new(salesman)
