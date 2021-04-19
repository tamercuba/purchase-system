from adapters.api import settings
from domain.entities import Salesman
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
