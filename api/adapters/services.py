from api.adapters.repositories import sale_repository, salesman_repository
from purchase_system.domain.services import (
    CreateSaleRequest,
    CreateSaleService,
    CreateSalesman,
    CreateSalesmanRequest,
    CreateSalesmanResponse,
)

create_sale_service = CreateSaleService(sale_repository, salesman_repository)
create_salesman_service = CreateSalesman(salesman_repository)
