from adapters.api.authentication.config import User
from adapters.api.services import authenticate_service, list_sales_service
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get('/sale')
def list_sales(user: User = Depends(authenticate_service)):
    return list_sales_service.handle(user)
