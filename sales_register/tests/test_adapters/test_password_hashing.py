from base64 import b64decode, b64encode

import pytest
from adapters.password_hashing.implementation import PasswordHashManager


class B64MockedCryptContext:
    def verify(self, plain_pw: str, hashed_pw: str) -> bool:
        decoded = b64decode(hashed_pw).decode()
        return plain_pw == decoded

    def hash(self, pw: str) -> str:
        return b64encode(str.encode(pw)).decode()


class TestPwHashing:
    @pytest.fixture(autouse=True)
    def injector(self):
        new_context = B64MockedCryptContext()
        self.manager = PasswordHashManager(context=new_context)

    def test_validate_successfully(self):
        raw_pw = 'oi'
        result = 'b2k='

        assert self.manager.validate_password(raw_pw, result)
        assert self.manager.hash_password(raw_pw) == result

    def test_fail_to_validate(self):
        raw_pw = 'oi'
        result = 'aW8K'

        assert not self.manager.validate_password(raw_pw, result)
        assert self.manager.hash_password(raw_pw) != result
