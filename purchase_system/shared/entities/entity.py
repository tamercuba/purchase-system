from typing import Any, List

from pydantic import BaseModel, Field

from purchase_system.shared.entities.id import EntityID, get_new_id


class Entity(BaseModel):
    id: EntityID = Field(default_factory=get_new_id)

    def __eq__(self, other: Any):
        if not isinstance(other, self.__class__):
            return False

        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    @classmethod
    def attributes(cls) -> List[str]:
        return [*cls.schema()['properties'].keys()]

    @classmethod
    def hasattr(cls, attr: str) -> bool:
        return attr in cls.attributes()
