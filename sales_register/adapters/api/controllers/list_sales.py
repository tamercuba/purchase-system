from adapters.api.services import list_sales_use_case, validate_token_service
from adapters.api.services.authentication import User
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get('/sale')
def list_sales(user: User = Depends(validate_token_service)):
    return list_sales_use_case.handle(user)
