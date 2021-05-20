from typing import Dict

from sqlalchemy.orm import declarative_base

_Base = declarative_base()


class Base(_Base):
    __abstract__ = True

    def dict(self) -> Dict:
        return {
            c.name: str(getattr(self, c.name)) for c in self.__table__.columns
        }
