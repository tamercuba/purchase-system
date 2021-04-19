from adapters.api.authentication import AuthenticateService, LoginService
from adapters.api.authentication.config import pwd_context
from adapters.repositories.postgres import SaleRepository, SalesmanRepository
from adapters.repositories.postgres.db import sales_table, salesman_table
from domain.services import (
    CreateSaleService,
    CreateSalesman,
    DeleteSaleService,
    GetSalesmanCashback,
    ListSales,
    UpdateSale,
)

sale_repository = SaleRepository(sales_table)
salesman_repository = SalesmanRepository(salesman_table)

login_service = LoginService(salesman_repository)
authenticate_service = AuthenticateService(salesman_repository)

create_sale_service = CreateSaleService(sale_repository)
create_salesman_service = CreateSalesman(
    salesman_repository, hash_algo=pwd_context.hash
)
delete_sale_service = DeleteSaleService(sale_repository)
list_sales_service = ListSales(sale_repository)
update_sale_service = UpdateSale(sale_repository)
get_user_cashback_service = GetSalesmanCashback(sale_repository)
