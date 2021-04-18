from purchase_system.adapters.repositories.in_memory_repo import (
    SaleRepository,
    SalesmanRepository,
)
from purchase_system.domain.entities import Sale, Salesman

salesmans = [
    Salesman(
        **{
            'email': 'tamercuba@gmail.com',
            'password': '$2b$12$OKFQ1uVGPOAOc2mYn/SoSO87PHA2qVYEjUGrwC5KYK9rOoHrHeKge',
            'cpf': '123',
            'name': 'tamer',
        }
    )
]
sales = [
    Sale(
        **{
            'code': 'a',
            'value': 1000,
            'date': '2020-01-01',
            'salesman_cpf': '123',
        }
    ),
    Sale(
        **{
            'code': 'b',
            'value': 2000,
            'date': '2020-01-02',
            'salesman_cpf': '123',
        }
    ),
    Sale(
        **{
            'code': 'b',
            'value': 2000,
            'date': '2020-01-02',
            'salesman_cpf': '456',
        }
    ),
]

sale_repository = SaleRepository(initial_values=sales)
salesman_repository = SalesmanRepository(initial_values=salesmans)
