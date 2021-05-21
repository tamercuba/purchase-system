from adapters.api.services import (
    validate_token_service,
    get_user_cashback_service,
)
from adapters.api.services.authentication import User
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from shared.exceptions import InvalidOperation

router = APIRouter()


class Response(BaseModel):
    total: float


@router.get(
    '/cashback/{user_cpf}',
    status_code=status.HTTP_200_OK,
    response_model=Response,
)
def get_cashback(
    user_cpf: str, user: User = Depends(validate_token_service)
) -> Response:
    try:
        result = get_user_cashback_service.handle(
            {'salesman_cpf': user_cpf, 'salesman': user}
        )

        return Response(total=result)
    except InvalidOperation:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
