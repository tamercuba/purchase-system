from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from api.adapters.services import list_sales_service
from api.authentication import authenticate_service

router = APIRouter()


@router.get('/sale')
def list_sales(auth: AuthJWT = Depends()) -> None:
    user = authenticate_service(auth)
    return list_sales_service.handle({'salesman_id': user.id})
