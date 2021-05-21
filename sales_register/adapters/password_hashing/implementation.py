from typing import Optional

from adapters.password_hashing.context import CryptContext, pwd_context
from adapters.repositories.postgres.password_manager_interface import (
    IPasswordManager,
)


class PasswordHashManager(IPasswordManager):
    def __init__(self, context: Optional[CryptContext] = None):
        self.context = context if context else pwd_context

    def validate_password(self, plain_pw: str, hashed_pw: str) -> bool:
        return self.context.verify(plain_pw, hashed_pw)

    def hash_password(self, pw: str) -> str:
        return self.context.hash(pw)
