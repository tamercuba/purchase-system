from adapters.repositories.postgres.models.base import Base
from sqlalchemy import Column, Date, Float, String


class SaleModel(Base):
    __tablename__ = 'sales'

    id = Column(String(length=32), primary_key=True)
    code = Column(String(length=32))
    value = Column(Float)
    status = Column(String(length=32))
    date = Column(Date)
    salesman_cpf = Column(String(length=11))
