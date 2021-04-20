import pytest
from pydantic import ValidationError
from shared.entities import ValueObject


class TestValueObject:
    def test_compare_same_value_objects(self, mocked_value_object_class):
        vo1 = mocked_value_object_class(name='a')
        vo2 = mocked_value_object_class(name='a')

        assert vo1 == vo2

    def test_compare_different_value_objects_implementation(
        self, mocked_value_object_class
    ):
        class WrongValueObject(ValueObject):
            name: str

        vo1 = mocked_value_object_class(name='a')
        vo2 = WrongValueObject(name='a')

        assert vo1 != vo2

    def test_different_value_object_props(self, mocked_value_object_class):
        vo1 = mocked_value_object_class(name='a')
        vo2 = mocked_value_object_class(name='b')

        assert vo1 != vo2

    @pytest.mark.parametrize('data', [({'car': 'a'}), ({})])
    def test_wrongly_initialized_value_object(
        self, data, mocked_value_object_class
    ):
        with pytest.raises(ValidationError):
            mocked_value_object_class(**data)
