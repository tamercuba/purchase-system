from typing import List

from adapters.repositories.postgres.generic import PostgresRepository
from adapters.repositories.postgres.models import SaleModel
from adapters.repositories.postgres.models.mappers import SaleMapper
from adapters.repositories.web import GetTotalCashback
from domain.entities import Sale
from domain.ports.repositories import ISaleRepository
from shared.exceptions import EntityNotFound


class SaleRepository(PostgresRepository, GetTotalCashback, ISaleRepository):
    model = SaleModel
    mapper = SaleMapper

    def get_by_id(self, _id: str) -> Sale:
        query = self._select.where(self.model.id == _id)

        sale: Sale = self._run_get(query)

        if not sale:
            raise EntityNotFound(
                f'Cant found Sale with id: {_id}',
                info={'id': _id},
            )

        return sale

    def delete(self, _id: str) -> None:
        query = self._delete.where(self.model.id == _id).execution_options(
            synchronize_session=False
        )
        self._run_delete(query)

    def update(self, entity: Sale) -> Sale:
        query = self._update.where(self.model.id == entity.id).values(
            code=entity.code,
            value=entity.value,
            date=entity.date,
            status=entity.status,
            salesman_cpf=entity.salesman_cpf,
        )
        self._run_update(query)

        return entity

    def new(self, entity: Sale) -> Sale:
        return self._run_new(entity)

    def list_by_cpf(self, cpf: str) -> List[Sale]:
        query = self._select.where(self.model.salesman_cpf == cpf)
        return self._run_list(query)
