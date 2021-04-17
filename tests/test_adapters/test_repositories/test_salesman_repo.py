import pytest

from purchase_system.adapters.repositories.in_memory_repo import (
    SalesmanRepository,
)
from purchase_system.domain.entities import Salesman
from purchase_system.shared.exceptions import EntityNotFound


class TestSalesmanRepo:
    def setup(self):
        self.repo = SalesmanRepository()
        self.new_salesman = Salesman(
            **{
                'cpf': '123',
                'name': 'Adriano Imperador',
                'email': 'didico@flamengo.com',
                'password': 'a',
            }
        )

        self.repo.new(self.new_salesman)

    def test_get_by_cpf(self):
        result = self.repo.get_by_cpf(self.new_salesman.cpf)

        assert result
        assert result == self.new_salesman

    @pytest.mark.parametrize('cpf', [('111'), (1), (False)])
    def test_get_by_wrong_cpf(self, cpf):
        with pytest.raises(EntityNotFound):
            self.repo.get_by_cpf(cpf)

    def test_get_by_email(self):
        result = self.repo.get_by_email(self.new_salesman.email)

        assert result
        assert result == self.new_salesman

    @pytest.mark.parametrize('email', [('111'), (1), (False)])
    def test_get_by_wrong_email(self, email):
        with pytest.raises(EntityNotFound):
            self.repo.get_by_email(email)
