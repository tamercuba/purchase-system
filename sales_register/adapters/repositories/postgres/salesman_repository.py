from typing import Optional

from adapters.repositories.postgres.db import engine
from adapters.repositories.postgres.generic import PostgresRepository
from domain.entities import Salesman
from domain.ports.repositories import ISalesmanRepository
from shared.exceptions import EntityNotFound


class SalesmanRepository(PostgresRepository, ISalesmanRepository):
    def get_by_id(self, _id: str) -> Salesman:
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

        return Salesman(**self._get_dict(result, keys))

    def get_by_cpf(self, cpf: str) -> Optional[Salesman]:
        query = self._table.select().where(self._table.c.cpf == cpf)
        with engine.connect() as conn:
            cursor = conn.execute(query)
            result = cursor.first()
            keys = list(cursor.keys())

        if not result:
            raise EntityNotFound(
                f'Cant found Sale with id: {cpf}',
                info={'id': cpf},
            )

        return Salesman(**self._get_dict(result, keys))

    def get_by_email(self, email: str) -> Optional[Salesman]:
        query = self._table.select().where(self._table.c.email == email)
        with engine.connect() as conn:
            cursor = conn.execute(query)
            result = cursor.first()
            keys = list(cursor.keys())

        if not result:
            raise EntityNotFound(
                f'Cant found Sale with id: {email}',
                info={'id': email},
            )

        return Salesman(**self._get_dict(result, keys))

    def new(self, salesman: Salesman) -> Salesman:
        query = self._table.insert().values(
            id=salesman.id,
            cpf=salesman.cpf,
            name=salesman.name,
            email=salesman.email,
            password=salesman.password.get_secret_value(),
            is_staff=salesman.is_staff,
        )
        with engine.connect() as conn:
            conn.execute(query)
        return salesman
