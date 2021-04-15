from abc import abstractmethod

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
