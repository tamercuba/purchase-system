import pytest
from shared.entity import Entity
from shared.exceptions import InvalidEntityType


@pytest.mark.asyncio
class TestInMemoryRepo:
    async def test_count(self, mocked_in_memory_repo):
        total = await mocked_in_memory_repo.count()
        assert total == 2

    async def test_new(self, mocked_in_memory_repo, mocked_entity_class):
        new_entity = mocked_entity_class(**{'name': 'new'})

        old_total = await mocked_in_memory_repo.count()

        await mocked_in_memory_repo.new(new_entity)

        new_total = await mocked_in_memory_repo.count()

        assert old_total == new_total - 1

    async def test_new_wrong_entity_type(self, mocked_in_memory_repo):
        class WrongEntity(Entity):
            name: str

        wrong_entity = WrongEntity(name='a')

        with pytest.raises(InvalidEntityType) as e:
            await mocked_in_memory_repo.new(wrong_entity)
            assert 'WrongEntity must be A type' in e

    async def test_get_by_id(self, mocked_in_memory_repo, mocked_entity_class):
        new_entity = mocked_entity_class(**{'name': 'new'})

        await mocked_in_memory_repo.new(new_entity)

        new_searched_entity = await mocked_in_memory_repo.get_by_id(
            _id=new_entity.id
        )

        assert new_entity == new_searched_entity
