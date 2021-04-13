from uuid import UUID, uuid4


class EntityID(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: str):
        if not isinstance(v, str):
            raise TypeError('Invalid UUID4')

        try:
            _id = UUID(v)
        except Exception as e:
            raise TypeError(e.__str__())

        return v


def get_new_id():
    _id = uuid4()
    return _id.hex
