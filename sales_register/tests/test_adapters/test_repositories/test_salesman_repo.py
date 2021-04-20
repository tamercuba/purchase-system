import pytest
from adapters.repositories.in_memory_repo import SalesmanRepository
from shared.exceptions import EntityNotFound


class TestSalesmanRepo:
    @pytest.fixture(autouse=True)
    def injector(self, salesman):
        self.new_salesman = salesman
        self.repo = SalesmanRepository(initial_values=[salesman])

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
