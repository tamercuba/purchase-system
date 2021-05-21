from adapters.api.services.repositories import (
    sale_repository,
    salesman_repository,
)
from domain.use_cases import (
CreateSaleUseCase,
CreateSalesmanUseCase,
DeleteSaleUseCase,
ListSalesUseCase,
UpdateSaleUseCase,
GetSalesmanCashbackUseCase,
)

create_sale_use_case = CreateSaleUseCase(sale_repository)
create_salesman_use_case = CreateSalesmanUseCase(salesman_repository)
delete_sale_use_case = DeleteSaleUseCase(sale_repository)
list_sales_use_case = ListSalesUseCase(sale_repository)
update_sale_use_case = UpdateSaleUseCase(sale_repository)
get_user_cashback_use_case = GetSalesmanCashbackUseCase(sale_repository)
