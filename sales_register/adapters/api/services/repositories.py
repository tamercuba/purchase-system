from adapters.api.services.pw_hash_manager import pw_hash_manager
from adapters.repositories.postgres import SaleRepository, SalesmanRepository
from adapters.repositories.postgres.connection import Session

sale_repository = SaleRepository(Session)
salesman_repository = SalesmanRepository(Session, pw_hash_manager)
