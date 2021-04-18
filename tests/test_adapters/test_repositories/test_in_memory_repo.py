import pytest

from purchase_system.shared.entities import Entity
from purchase_system.shared.exceptions import (
    EntityAttributeDoesntExist,
    InvalidEntityType,
)


class TestInMemoryRepo:
    def test_count(self, mocked_in_memory_repo):
        total = mocked_in_memory_repo.count()
        assert total == 2

    def test_new(self, mocked_in_memory_repo, mocked_entity_class):
        new_entity = mocked_entity_class(**{'name': 'new'})

        old_total = mocked_in_memory_repo.count()

        mocked_in_memory_repo.new(new_entity)

        new_total = mocked_in_memory_repo.count()

        assert old_total == new_total - 1

    def test_new_wrong_entity_type(self, mocked_in_memory_repo):
        class WrongEntity(Entity):
            name: str

        wrong_entity = WrongEntity(name='a')

        with pytest.raises(InvalidEntityType) as e:
            mocked_in_memory_repo.new(wrong_entity)
            assert 'WrongEntity must be A type' in e

    def test_get_by_id(self, mocked_in_memory_repo, mocked_entity_class):
        new_entity = mocked_entity_class(**{'name': 'new'})

        mocked_in_memory_repo.new(new_entity)

        new_searched_entity = mocked_in_memory_repo.get_by_id(
            _id=new_entity.id
        )

        assert new_entity == new_searched_entity

    def test_get_attr_wrong_implementation(self, mocked_in_memory_repo):
        with pytest.raises(EntityAttributeDoesntExist):
            mocked_in_memory_repo.get_nonexistent_attribute()
