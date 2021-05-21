from adapters.repositories.postgres import SaleRepository, SalesmanRepository
from adapters.repositories.postgres.db.connection import Session

sale_repository = SaleRepository(Session)
salesman_repository = SalesmanRepository(Session)
