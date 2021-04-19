from sqlalchemy import (
    Boolean,
    Column,
    Date,
    Float,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
)

metadata = MetaData()

sales_table = Table(
    'sales',
    metadata,
    Column('id', String(length=32), primary_key=True),
    Column('code', String(length=32)),
    Column('value', Float),
    Column('status', String(length=32)),
    Column('date', Date),
    Column('salesman_cpf', String(length=11)),
)

salesman_table = Table(
    'users',
    metadata,
    Column('id', String(length=32), primary_key=True),
    Column('cpf', String(length=11)),
    Column('name', String(length=32)),
    Column('email', String(length=32)),
    Column('password', String(length=64)),
    Column('is_staff', Boolean),
)
