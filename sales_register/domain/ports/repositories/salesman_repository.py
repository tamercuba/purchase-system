from abc import abstractmethod

from domain.entities import Salesman


class ISalesmanRepository:
    @abstractmethod
    def new(self, salesman: Salesman) -> Salesman:
        pass

    @abstractmethod
    def get_by_cpf(self, cpf: str) -> Salesman:
        pass

    @abstractmethod
    def get_by_id(self, _id: str) -> Salesman:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Salesman:
        pass
