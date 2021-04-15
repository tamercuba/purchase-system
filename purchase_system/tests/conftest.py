import pytest
from adapters.repositories.in_memory_repo import GenericInMemoryRepository
from core.entities import Sale, Salesman
from shared.entity import Entity

# pylint: disable=redefined-outer-name


@pytest.fixture
def mocked_in_memory_repo(mocked_entity_class):
    class MockedRepo(GenericInMemoryRepository[mocked_entity_class]):
        pass

    initial_values = [
        mocked_entity_class(**{'name': 'Oi'}),
        mocked_entity_class(**{'name': 'Tchau'}),
    ]

    return MockedRepo(initial_values=initial_values)


@pytest.fixture
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


@pytest.fixture
def sale_data():
    return {
        'code': 'a',
        'value': 10,
        'date': '1997-09-01',
        'salesman_cpf': '123',
    }


@pytest.fixture
def sale(sale_data):
    return Sale(**sale_data)
