from domain.entities import Salesman
from domain.ports.repositories import ISalesmanRepository
from shared.exceptions import EntityNotFound
from sqlalchemy.orm import sessionmaker

from .generic import PostgresRepository
from .models import SalesmanMapper, SalesmanModel
from .password_manager_interface import IPasswordManager


class SalesmanRepository(PostgresRepository[Salesman], ISalesmanRepository):
    model = SalesmanModel
    mapper = SalesmanMapper

    def __init__(self, Session: sessionmaker, hash_manager: IPasswordManager):
        super().__init__(Session)
        self._hash_manager = hash_manager

    def get_by_id(self, _id: str) -> Salesman:
        query = self._select.where(self.model.id == _id)

        salesman = self._run_get(query)

        if not salesman:
            raise EntityNotFound(
                f'Cant found Sale with id: {_id}',
                info={'id': _id},
            )

        return salesman

    def get_by_cpf(self, cpf: str) -> Salesman:
        query = self._select.where(self.model.cpf == cpf)

        salesman: Salesman = self._run_get(query)

        if not salesman:
            raise EntityNotFound(
                f'Cant found Sale with id: {cpf}',
                info={'id': cpf},
            )

        return salesman

    def get_by_email(self, email: str) -> Salesman:
        query = self._select.where(self.model.email == email)

        salesman: Salesman = self._run_get(query)

        if not salesman:
            raise EntityNotFound(
                f'Cant found Sale with id: {email}',
                info={'id': email},
            )

        return salesman

    def new(self, salesman: Salesman) -> Salesman:
        return self._run_new(self._encrypt_salesman(salesman))

    def _encrypt_salesman(self, salesman: Salesman) -> Salesman:
        raw_pw = salesman.password.get_secret_value()
        encrypted_salesman = Salesman(
            **{
                **salesman.model_dump(),
                'password': self._hash_manager.hash_password(raw_pw),
            }
        )

        return encrypted_salesman
