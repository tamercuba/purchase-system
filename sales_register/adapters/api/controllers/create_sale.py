from typing import Optional

from adapters.api.services import create_sale_use_case, validate_token_service
from adapters.api.services.authentication import User
from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter()


class Request(BaseModel):
    code: str
    value: float
    date: str
    status: Optional[str] = None


@router.post('/sale')
def create_sale(
    request: Request, user: User = Depends(validate_token_service)
):
    result = create_sale_use_case.handle(
        {"salesman": user, "sale": request.dict()}
    )
    return result.dict()
