from abc import abstractmethod
from typing import List

from domain.entities import Sale


class ISaleRepository:
    @abstractmethod
    def get_by_id(self, _id: str) -> Sale:
        pass

    @abstractmethod
    def delete(self, _id: str) -> None:
        pass

    @abstractmethod
    def update(self, entity: Sale) -> Sale:
        pass

    @abstractmethod
    def new(self, entity: Sale) -> Sale:
        pass

    @abstractmethod
    def list_by_cpf(self, cpf: str) -> List[Sale]:
        pass
