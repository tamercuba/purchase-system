from adapters.api import settings
from adapters.api.services.authentication.context import pwd_context
from adapters.api.services.authentication.login_service import LoginService
from adapters.api.services.authentication.user import User
from adapters.api.services.authentication.validate_token import (
    ValidateTokenService,
)
from adapters.api.services.pw_hash_manager import pw_hash_manager
from adapters.api.services.repositories import salesman_repository
from domain.entities import Salesman
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel, Field


class Settings(BaseModel):
    authjwt_secret_key: str = Field(default=settings.SECRET_KEY)


@AuthJWT.load_config
def get_config():
    return Settings()


validate_token_service = ValidateTokenService(salesman_repository)
login_service = LoginService(salesman_repository, pw_hash_manager)
