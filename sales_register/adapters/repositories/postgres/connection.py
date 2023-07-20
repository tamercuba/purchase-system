from .settings import postgres_settings
from sqlalchemy import create_engine, orm, pool

engine = create_engine(
    postgres_settings.DB_URI, poolclass=pool.NullPool, future=True
)

Session = orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)
