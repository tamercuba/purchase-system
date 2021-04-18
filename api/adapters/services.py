from api.adapters.repositories import sale_repository, salesman_repository
from purchase_system.domain.services import (
    CreateSaleService,
    CreateSalesman,
    DeleteSaleService,
    ListSales,
)

create_sale_service = CreateSaleService(sale_repository, salesman_repository)
create_salesman_service = CreateSalesman(salesman_repository)
delete_sale_service = DeleteSaleService(sale_repository, salesman_repository)
list_sales_service = ListSales(sale_repository, salesman_repository)
