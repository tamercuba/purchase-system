from adapters.api.services import login_service
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

router = APIRouter()


class Request(BaseModel):
    email: str
    password: str


class Response(BaseModel):
    token: str


@router.post('/token', status_code=status.HTTP_200_OK, response_model=Response)
def get_token(request: Request, Auth: AuthJWT = Depends()) -> Response:
    user = login_service(request)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = login_service.create_access_token(user.id, Auth)

    return Response(token=token)
