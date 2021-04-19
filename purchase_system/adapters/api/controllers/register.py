from adapters.api.services import create_salesman_service, login_service
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from shared.exceptions import RepeatedEntry
from typing import Optional

router = APIRouter()


class Request(BaseModel):
    cpf: str
    name: str
    email: str
    password: str
    is_staff: Optional[bool]


class Response(BaseModel):
    access_token: str


@router.post('/register', response_model=Response)
def register(request: Request, auth: AuthJWT = Depends()):
    try:
        user = create_salesman_service.handle(request.dict())
        token = login_service.create_access_token(user['id'], auth)
        return Response(
            access_token=token, status_code=status.HTTP_201_CREATED
        )

    except RepeatedEntry as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=e.info
        )
