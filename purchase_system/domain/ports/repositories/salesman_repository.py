from abc import abstractmethod
from typing import Optional

from domain.entities import Salesman


class ISalesmanRepository:
    @abstractmethod
    def new(self, salesman: Salesman) -> None:
        pass

    @abstractmethod
    def get_by_cpf(self, cpf: str) -> Optional[Salesman]:
        pass

    @abstractmethod
    def get_by_id(self, _id: str) -> Optional[Salesman]:
        pass
