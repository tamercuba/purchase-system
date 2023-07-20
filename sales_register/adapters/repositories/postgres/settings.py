from pydantic_settings import BaseSettings
from sqlalchemy.engine import URL


class PostgresSettings(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    DB_USER: str = 'postgres'
    DB_PW: str = 'postgres'
    DB_NAME: str = 'sales_register'

    DB_URI: URL = URL(
        drivername='postgresql',
        username=DB_USER,
        password=DB_PW,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
    )  # type: ignore


postgres_settings = PostgresSettings()
