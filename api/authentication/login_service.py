from typing import Union

from fastapi_jwt_auth import AuthJWT

from api.adapters.repositories import salesman_repository
from api.authentication.config import User, pwd_context
from purchase_system.domain.ports.repositories import ISalesmanRepository
from purchase_system.shared.exceptions import EntityNotFound


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

    def create_access_token(self, user_id: str, auth: AuthJWT) -> str:
        return  f'Bearer {auth.create_access_token(subject=user_id)}'

login_service = LoginService(salesman_repository)
