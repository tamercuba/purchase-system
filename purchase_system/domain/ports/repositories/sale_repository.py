from abc import abstractmethod

from domain.entities import Sale


class ISaleRepository:
    @abstractmethod
    async def get_by_id(self, _id: str) -> Sale:
        pass

    @abstractmethod
    async def delete(self, _id: str) -> None:
        pass
