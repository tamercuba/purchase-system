from typing import Optional

from adapters.api.authentication import authenticate_service
from adapters.api.services import create_sale_service
from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

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
