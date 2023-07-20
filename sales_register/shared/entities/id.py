from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import CoreSchema, core_schema


class EntityID(str):
    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: core_schema.JsonSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        json_schema: dict[str, Any] = {}
        json_schema.update(type='string')
        return json_schema

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.general_plain_validator_function(cls.validate)

    @classmethod
    def validate(cls, v: str, _: core_schema.ValidationInfo):
        if not isinstance(v, str):
            raise TypeError('Invalid UUID4')

        try:
            UUID(v)
        except Exception as e:
            raise TypeError(e.__str__())

        return v

    @classmethod
    def new(cls) -> EntityID:
        return cls(uuid4().hex)
