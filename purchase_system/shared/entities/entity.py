from typing import Any

from pydantic import BaseModel, Field
from shared.entities.id import EntityID, get_new_id


class Entity(BaseModel):
    id: EntityID = Field(default_factory=get_new_id)

    def __eq__(self, other: Any):
        if not isinstance(other, self.__class__):
            return False

        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)
