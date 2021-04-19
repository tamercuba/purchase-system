from functools import wraps
from typing import Dict, Optional

from adapters.api import settings

# from adapters.api.authentication.authentication_service import (
#     authenticate_service,
# )
from domain.entities import Salesman
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT
from passlib.context import CryptContext
from pydantic import BaseModel, Field

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

User = Salesman


class Settings(BaseModel):
    authjwt_secret_key: str = Field(default=settings.SECRET_KEY)


@AuthJWT.load_config
def get_config():
    return Settings()


# def requires_authorization(route):
#     @wraps(route)
#     def wrapper(Authorize: AuthJWT = Depends()):
#         return route(authenticate_service(Authorize))

#     return wrapper


# def requires_authorization_2(params: Optional[Dict[str, BaseModel]]):
#     def decorate(route):
#         @wraps(route)
#         def wrapper(auth: AuthJWT):
#             user = authenticate_service(auth)
#             return route(user=user, **params)

#         return wrapper

#     return decorate
