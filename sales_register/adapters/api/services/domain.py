from adapters.api.services.repositories import (
    sale_repository,
    salesman_repository,
)
from domain.services import (
    CreateSaleService,
    CreateSalesmanService,
    DeleteSaleService,
    GetSalesmanCashbackService,
    ListSalesService,
    UpdateSaleService,
)

create_sale_service = CreateSaleService(sale_repository)
create_salesman_service = CreateSalesmanService(salesman_repository)
delete_sale_service = DeleteSaleService(sale_repository)
list_sales_service = ListSalesService(sale_repository)
update_sale_service = UpdateSaleService(sale_repository)
get_user_cashback_service = GetSalesmanCashbackService(sale_repository)
