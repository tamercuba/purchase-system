from typing import Union

from adapters.api.services.authentication.context import pwd_context
from adapters.api.services.authentication.user import User
from domain.ports.repositories import ISalesmanRepository
from fastapi_jwt_auth import AuthJWT
from shared.exceptions import EntityNotFound


class LoginService:
    def __init__(self, user_repo: ISalesmanRepository):
        self._repo = user_repo

    def __call__(self, email: str, password: str) -> Union[User, bool]:
        try:
            user: User = self._repo.get_by_email(email)
            if self.verify_password(
                password, user.password.get_secret_value()
            ):
                return user

        except EntityNotFound:
            return False

        return False

    @staticmethod
    def verify_password(plain_password, hashed_password) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    def create_access_token(self, user_id: str, auth: AuthJWT) -> str:
        return f'Bearer {auth.create_access_token(subject=user_id)}'
