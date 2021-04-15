import pytest
from pydantic import ValidationError
from shared.entities import Entity, get_new_id


def test_create_entity_id_auto_assign(mocked_entity_class):
    name = 'Michael Jackson'
    entity = mocked_entity_class(name=name)

    assert entity.name == name
    assert entity.id


def test_create_entity_valid_id(mocked_entity_class):
    _id = get_new_id()
    name = 'Raul Seixas'
    entity = mocked_entity_class(name=name, id=_id)

    assert entity.name == name
    assert entity.id == _id


def test_create_entity_invalid_id(mocked_entity_class):
    _id = '1234'
    name = 'Tamer'

    with pytest.raises(ValidationError):
        mocked_entity_class(name=name, id=_id)


def test_create_entity_wrong_type_id(mocked_entity_class):
    _id = 1234
    name = 'Tamer'

    with pytest.raises(ValidationError):
        mocked_entity_class(name=name, id=_id)


def test_compare_entities(mocked_entity_class):
    entity1 = mocked_entity_class(name='Um')
    entity2 = entity1.copy()
    entity2.name = 'Dois'

    assert entity1.name != entity2.name
    assert entity1 == entity2


def test_compare_different_entities_with_same_id(mocked_entity_class):
    """
    According to wikipedia the probability of colisions using uui4 algorithm
    is:
        Only after generating 1 billion UUIDs every second for the next
        100 years, the probability of creating just one duplicate would be
        about 50%. Or, to put it another way, the probability of one
        duplicate would be about 50% if every person on earth owned 600
        million UUIDs.
    So this test only exists to get 100% on coverage
    """

    class Entity2(Entity):
        name: str

    _id = get_new_id()

    entity1 = mocked_entity_class(name='um', id=_id)
    entity2 = Entity2(name='dois', id=_id)

    assert entity1 != entity2
    assert entity1.id == entity2.id
