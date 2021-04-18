from fastapi import Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import JWTDecodeError

from api.adapters.repositories import salesman_repository
from purchase_system.domain.ports.repositories import ISalesmanRepository
from purchase_system.shared.exceptions import EntityNotFound


class AuthenticateService:
    def __init__(self, user_repo: ISalesmanRepository):
        self._repo = user_repo

    def __call__(self, auth: AuthJWT):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            auth.jwt_required()
            user_id = auth.get_jwt_subject()
        except JWTDecodeError:
            raise credentials_exception

        try:
            user = self._repo.get_by_id(user_id)
            return user
        except EntityNotFound:
            raise credentials_exception


authenticate_service = AuthenticateService(salesman_repository)
