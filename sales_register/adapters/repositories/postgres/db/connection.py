from adapters.repositories.postgres.config import DB_URI
from sqlalchemy import create_engine, pool

# class PostgresConnector:
#     def __init__(self):
#         self.engine = create_engine(DB_URI, poolclass=pool.NullPool)

#     def create_connection(self):
#         return self.engine.connect()


engine = create_engine(DB_URI, poolclass=pool.NullPool)

# class PostgresConnection:
#     connection = None

#     @classmethod
#     def create_connection(cls):
#         if not cls.connection:
#             cls.connection = PostgresConnector().create_connection()

#         return cls.connection


# conn = PostgresConnection().create_connection()
