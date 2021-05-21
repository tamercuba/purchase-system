from datetime import date
from typing import Optional

from adapters.api.services import create_sale_use_case, validate_token_service
from adapters.api.services.authentication import User
from fastapi import APIRouter, Depends, status
from pydantic import BaseModel

router = APIRouter()


class Request(BaseModel):
    code: str
    value: float
    date: str
    status: Optional[str] = None


class Response(BaseModel):
    id: str
    code: str
    value: float
    date: date
    status: Optional[str] = None
    salesman_cpf: str


@router.post(
    '/sale', status_code=status.HTTP_201_CREATED, response_model=Response
)
def create_sale(
    request: Request, user: User = Depends(validate_token_service)
) -> Response:
    result = create_sale_use_case.handle(
        {"salesman": user, "sale": request.dict()}
    )

    return Response(**result.dict())
