from typing import List

from adapters.repositories.postgres.db import engine
from adapters.repositories.postgres.generic import PostgresRepository
from adapters.repositories.web import GetTotalCashback
from domain.entities import Sale
from domain.ports.repositories import ISaleRepository
from shared.exceptions import EntityNotFound
from sqlalchemy import Table
from sqlalchemy.engine import Connection


class SaleRepository(PostgresRepository, GetTotalCashback, ISaleRepository):
    def get_by_id(self, _id: str) -> Sale:
        query = self._table.select().where(self._table.c.id == _id)
        with engine.connect() as conn:
            cursor = conn.execute(query)
            result = cursor.first()
            keys = list(cursor.keys())

        if not result:
            raise EntityNotFound(
                f'Cant found Sale with id: {_id}',
                info={'id': _id},
            )

        return Sale(**self._get_dict(result, keys))

    def delete(self, _id: str) -> None:
        with engine.connect() as conn:
            query = self._table.delete().where(self._table.c.id == _id)
            conn.execute(query)

    def update(self, entity: Sale) -> Sale:
        query = (
            self._table.update()
            .where(self._table.c.id == entity.id)
            .values(
                code=entity.code,
                value=entity.value,
                date=entity.date,
                status=entity.status,
                salesman_cpf=entity.salesman_cpf,
            )
        )
        with engine.connect() as conn:
            conn.execute(query)

        return entity

    def new(self, entity: Sale) -> Sale:
        query = self._table.insert().values(
            id=entity.id,
            code=entity.code,
            value=entity.value,
            date=entity.date,
            status=entity.status,
            salesman_cpf=entity.salesman_cpf,
        )
        with engine.connect() as conn:
            conn.execute(query)
        return entity

    def list_by_cpf(self, cpf: str) -> List[Sale]:
        query = self._table.select().where(self._table.c.salesman_cpf == cpf)
        with engine.connect() as conn:
            cursor = conn.execute(query)
            results = cursor.fetchall()
        return [Sale(**result) for result in results]
