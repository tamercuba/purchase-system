from decouple import config
from sqlalchemy.engine import URL

# _DB_HOST = config('DB_HOST')
_DB_HOST = config('POSTGRES_PORT_5432_TCP_ADDR', None) or config('DB_HOST')
_DB_PORT = config('DB_PORT')
_DB_USER = config('DB_USER')
_DB_PW = config('DB_PW')
_DB_NAME = config('DB_NAME')

# DB_URI = f'postgresql://{_DB_USER}:{_DB_PW}@{_DB_HOST}:{_DB_PORT}/{_DB_NAME}'
DB_URI = URL(
    drivername='postgresql',
    username=_DB_USER,
    password=_DB_PW,
    host=_DB_HOST,
    port=_DB_PORT,
    database=_DB_NAME,
)
