import pytest
from core.entities import Salesman
from shared.entity import Entity

# pylint: disable=redefined-outer-name


@pytest.fixture(scope='session')
def mocked_entity_class():
    class A(Entity):
        name: str

    return A


@pytest.fixture
def salesman_data():
    return {
        'cpf': '123',
        'name': 'Adriano Imperador',
        'email': 'didico@flamengo.com',
        'password': 'a',
    }


@pytest.fixture
def salesman(salesman_data):
    return Salesman(**salesman_data)
