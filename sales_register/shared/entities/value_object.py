from typing import Any

from pydantic import BaseModel


class ValueObject(BaseModel):
    def __eq__(self, other: Any):
        if not isinstance(other, self.__class__):
            return False

        return self.model_dump() == other.model_dump()
