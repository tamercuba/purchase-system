from adapters.repositories.postgres.db import engine
from sqlalchemy import Table


class PostgresRepository:
    def __init__(self, table: Table):
        self._table = table

    def _run_query(self, query):
        with engine.connect() as conn:
            cursor = conn.execute(query)
            print(dir(cursor))

        return cursor

    def _get_dict(self, result, keys):
        return dict(zip(keys, result))
