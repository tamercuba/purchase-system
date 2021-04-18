from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from api.authentication import authenticate_service, login_service

router = APIRouter()


class Request(BaseModel):
    email: str
    password: str


@router.post('/token')
def get_token(request: Request, Auth: AuthJWT = Depends()):
    user = login_service(request.email, request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = login_service.create_access_token(user.id, Auth)

    return {"token": token}


@router.get('/teste2')
def teste2(Authorize: AuthJWT = Depends()):
    user = authenticate_service(Authorize)
    return {'a': str(user)}
