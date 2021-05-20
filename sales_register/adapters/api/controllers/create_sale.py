from typing import Optional

from adapters.api.authentication import User
from adapters.api.services import authenticate_service, create_sale_service
from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter()


class Request(BaseModel):
    code: str
    value: float
    date: str
    status: Optional[str] = None


@router.post('/sale')
def create_sale(request: Request, user: User = Depends(authenticate_service)):
    result = create_sale_service.handle(
        {"salesman": user, "sale": request.dict()}
    )
    return result.dict()
