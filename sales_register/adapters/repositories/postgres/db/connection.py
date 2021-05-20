from adapters.repositories.postgres.config import DB_URI
from sqlalchemy import create_engine, orm, pool

engine = create_engine(DB_URI, poolclass=pool.NullPool, future=True)

Session = orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)
