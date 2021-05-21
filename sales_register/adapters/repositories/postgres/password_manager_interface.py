from abc import ABC, abstractmethod


class IPasswordManager(ABC):
    @abstractmethod
    def validate_password(self, plain_pw: str, hashed_pw: str) -> bool:
        ...

    @abstractmethod
    def hash_password(self, pw: str) -> str:
        ...
