from adapters.repositories.in_memory_repo.db import (
    sale_repository,
    salesman_repository,
)
from domain.services import (
    CreateSaleService,
    CreateSalesman,
    DeleteSaleService,
    GetSalesmanCashback,
    ListSales,
    UpdateSale,
)

create_sale_service = CreateSaleService(sale_repository)
create_salesman_service = CreateSalesman(salesman_repository)
delete_sale_service = DeleteSaleService(sale_repository)
list_sales_service = ListSales(sale_repository)
update_sale_service = UpdateSale(sale_repository)
get_user_cashback_service = GetSalesmanCashback(sale_repository)
