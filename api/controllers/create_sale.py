from typing import Optional

from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from api.adapters.services import create_sale_service
from api.authentication import authenticate_service

router = APIRouter()


class Request(BaseModel):
    code: str
    value: float
    date: str
    status: Optional[str] = None


@router.post('/sale')
def create_sale(request: Request, auth: AuthJWT = Depends()):
    user = authenticate_service(auth)
    result = create_sale_service.handle(
        {"salesman": user, "sale": request.dict()}
    )
    return result.dict()
