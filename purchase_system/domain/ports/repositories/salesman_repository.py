from abc import abstractmethod
from typing import Optional

from purchase_system.domain.entities import Salesman


class ISalesmanRepository:
    @abstractmethod
    def new(self, salesman: Salesman) -> Salesman:
        pass

    @abstractmethod
    def get_by_cpf(self, cpf: str) -> Optional[Salesman]:
        pass

    @abstractmethod
    def get_by_id(self, _id: str) -> Optional[Salesman]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[Salesman]:
        pass
