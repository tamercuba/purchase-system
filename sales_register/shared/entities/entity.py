from typing import Any, Dict, List

from pydantic import BaseModel, Field
from shared.entities.id import EntityID


class Entity(BaseModel):
    id: EntityID = Field(default_factory=EntityID.new)

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

    def dict_with_secrets(self) -> Dict:
        def get_value(value):
            if hasattr(value, 'get_secret_value'):
                return value.get_secret_value()

            return value

        return {key: get_value(value) for key, value in self.dict().items()}
