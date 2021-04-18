from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from api.adapters.services import get_user_cashback_service
from api.authentication import authenticate_service
from purchase_system.shared.exceptions import InvalidOperation

router = APIRouter()


class Response(BaseModel):
    total: float


@router.get(
    '/cashback/<user_cpf:str>',
    status_code=status.HTTP_200_OK,
    response_model=Response,
)
def get_cashback(user_cpf: str, auth: AuthJWT = Depends()) -> Response:
    user = authenticate_service(auth)
    try:
        result = get_user_cashback_service.handle(
            {'salesman_cpf': user_cpf, 'salesman': user}
        )

        return Response(total=result.cashback_total)
    except InvalidOperation:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
