from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from api.adapters.services import delete_sale_service
from api.authentication import authenticate_service

router = APIRouter(prefix='/sale')


class Request(BaseModel):
    sale_id: str


@router.post('/delete', status_code=status.HTTP_204_NO_CONTENT)
def delete_sale(request: Request, auth: AuthJWT = Depends()) -> None:
    user = authenticate_service(auth)
    delete_sale_service.handle(
        {'sale_id': request.sale_id, 'salesman_id': user.id}
    )
