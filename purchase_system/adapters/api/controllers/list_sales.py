from adapters.api.authentication import authenticate_service
from adapters.api.services import list_sales_service
from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

router = APIRouter()


@router.get('/sale')
def list_sales(auth: AuthJWT = Depends()) -> None:
    user = authenticate_service(auth)
    return list_sales_service.handle(user)
