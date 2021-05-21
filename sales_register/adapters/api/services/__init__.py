from adapters.api.services.authentication import (
    login_service,
    pwd_context,
    validate_token_service,
)
from adapters.api.services.domain import (
    create_sale_service,
    create_salesman_service,
    delete_sale_service,
    get_user_cashback_service,
    list_sales_service,
    update_sale_service,
)
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
