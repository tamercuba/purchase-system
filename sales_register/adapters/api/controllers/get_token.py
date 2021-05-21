from adapters.api.services import login_service
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

router = APIRouter()


class Request(BaseModel):
    email: str
    password: str


@router.post('/token')
def get_token(request: Request, Auth: AuthJWT = Depends()):
    user = login_service(request)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = login_service.create_access_token(user.id, Auth)

    return {"token": token}
