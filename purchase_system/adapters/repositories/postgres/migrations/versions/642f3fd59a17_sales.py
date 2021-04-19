"""sales

Revision ID: 642f3fd59a17
Revises: 547a7bfacf17
Create Date: 2021-04-18 16:54:47.129554

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '642f3fd59a17'
down_revision = '547a7bfacf17'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'sales',
        sa.Column('id', sa.String(length=32), primary_key=True),
        sa.Column('code', sa.String(length=32)),
        sa.Column('value', sa.Numeric(precision=2)),
        sa.Column('status', sa.String(length=32)),
        sa.Column('date', sa.Date),
        sa.Column('salesman_cpf', sa.String(length=11)),
    )


def downgrade():
    op.drop_table('sales')
