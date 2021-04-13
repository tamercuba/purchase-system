import pytest
from shared.entity import Entity


@pytest.fixture(scope='session')
def mocked_entity_class():
    class A(Entity):
        name: str

    return A
