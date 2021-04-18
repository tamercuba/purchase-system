from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from api.adapters.services import create_salesman_service
from api.authentication.login_service import login_service
from purchase_system.shared.exceptions import RepeatedEntry

router = APIRouter()

class Request(BaseModel):
    cpf: str
    name: str
    email: str
    password: str

class Response(BaseModel):
    access_token: str


@router.post(
    '/register', status_code=status.HTTP_201_CREATED, response_model=Response
)
def register(request: Request, auth: AuthJWT = Depends()):
    try:
        user = create_salesman_service.handle(request.dict())
        token = login_service.create_access_token(user['id'], auth)
        return Response(access_token=token)

    except RepeatedEntry as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=e.info
        )
