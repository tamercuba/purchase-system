from typing import List

from adapters.api.services import list_sales_use_case, validate_token_service
from adapters.api.services.authentication import User
from fastapi import APIRouter, Depends, status

router = APIRouter()

Response = List[User]


@router.get('/sale', status_code=status.HTTP_200_OK)
def list_sales(user: User = Depends(validate_token_service)) -> Response:
    return list_sales_use_case.handle(user)
