from adapters.repositories.postgres.models.base import Base
from sqlalchemy import Boolean, Column, String


class SalesmanModel(Base):
    __tablename__ = 'users'

    id = Column(String(length=32), primary_key=True)
    cpf = Column(String(length=11))
    name = Column(String(length=32))
    email = Column(String(length=32))
    password = Column(String(length=64))
    is_staff = Column(Boolean)
