"""populate

Revision ID: aa93d5e15a1b
Revises: 59dd3e454579
Create Date: 2021-04-19 19:47:15.035862

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'aa93d5e15a1b'
down_revision = '59dd3e454579'
branch_labels = None
depends_on = None

_id = 'e73faa1a056b4b72b1b434e30cd4e2cc'


def upgrade():
    meta = sa.MetaData(bind=op.get_bind())
    meta.reflect(only=('users',))
    salesman_table = sa.Table('users', meta)
    op.bulk_insert(
        salesman_table,
        [
            {
                'id': _id,
                'cpf': '15350946056',
                'name': 'admin',
                'email': 'admin@admin.com',
                'password': (
                    '$2b$12$z9bysHuwfVqaXeMoxvIbW.'
                    'N1fLHzeMu36J.our7mqXHueyBEDv8Za'
                ),
                'is_staff': True,
            }
        ],
    )


def downgrade():
    meta = sa.MetaData(bind=op.get_bind())
    meta.reflect(only=('users',))
    salesman_table = sa.Table('users', meta)
    op.execute(
        sa.sql.expression.delete(salesman_table).where(
            salesman_table.c.id == _id
        )
    )
