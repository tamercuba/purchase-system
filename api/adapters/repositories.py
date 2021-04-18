from purchase_system.adapters.repositories.in_memory_repo import (
    SaleRepository,
    SalesmanRepository,
)
from purchase_system.domain.entities import Salesman

initial = Salesman(**{
    'email': 'tamercuba@gmail.com',
    'password': '$2b$12$OKFQ1uVGPOAOc2mYn/SoSO87PHA2qVYEjUGrwC5KYK9rOoHrHeKge',
    'cpf': '123',
    'name': 'tamer'
})

sale_repository = SaleRepository()
salesman_repository = SalesmanRepository(initial_values=[initial])
