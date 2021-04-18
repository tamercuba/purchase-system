from api.adapters.repositories import sale_repository, salesman_repository
from purchase_system.domain.services import (
    CreateSaleService,
    CreateSalesman,
    DeleteSaleService,
    GetSalesmanCashback,
    ListSales,
    UpdateSale,
)

create_sale_service = CreateSaleService(sale_repository, salesman_repository)
create_salesman_service = CreateSalesman(salesman_repository)
delete_sale_service = DeleteSaleService(sale_repository)
list_sales_service = ListSales(sale_repository, salesman_repository)
update_sale_service = UpdateSale(sale_repository, salesman_repository)
get_user_cashback_service = GetSalesmanCashback(sale_repository)
