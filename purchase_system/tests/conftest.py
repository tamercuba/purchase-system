import pytest
from adapters.repositories.in_memory_repo import GenericInMemoryRepository
from domain.entities import Sale, Salesman
from shared.entities import Entity, ValueObject

# pylint: disable=redefined-outer-name


@pytest.fixture
def mocked_in_memory_repo(mocked_entity_class):
    class MockedRepo(GenericInMemoryRepository[mocked_entity_class]):
        def get_nonexistent_attribute(self):
            return self._get_by_attribute('bla', 1)

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


@pytest.fixture
def mocked_value_object_class():
    class A(ValueObject):
        name: str

    return A


@pytest.fixture
def multiple_sales_data():
    return [
        {
            'code': 'a',
            'value': 1000,
            'date': '1997-09-01',
            'salesman_cpf': '456',
        },
        {
            'code': 'b',
            'value': 2000,
            'date': '1995-09-01',
            'salesman_cpf': '456',
        },
        {
            'code': 'c',
            'value': 3000,
            'date': '1295-09-01',
            'salesman_cpf': '789',
        },
    ]


@pytest.fixture
def multiple_salesmans_data():
    return [
        {
            'cpf': '123',
            'name': 'Adriano Imperador',
            'email': 'didico@flamengo.com',
            'password': 'a',
            'is_staff': True,
        },
        {
            'cpf': '456',
            'name': 'Tamer',
            'email': 'bbb@aa.com',
            'password': 'ac',
        },
    ]
