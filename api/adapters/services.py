from api.adapters.authentication import authentication_handler
from api.adapters.repositories import sale_repository, salesman_repository
from purchase_system.domain.services import (
    Authenticate,
    AuthenticateResponse,
    AuthenticationRequest,
    CreateSaleRequest,
    CreateSaleService,
)

authentication_service = Authenticate(
    salesman_repository=salesman_repository,
    authentication_handler=authentication_handler
)
create_sale_service = CreateSaleService(sale_repository, salesman_repository)
