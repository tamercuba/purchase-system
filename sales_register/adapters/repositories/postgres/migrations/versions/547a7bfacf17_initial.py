"""user initial table

Revision ID: 547a7bfacf17
Revises: 
Create Date: 2021-04-18 16:52:48.024705

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '547a7bfacf17'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.String(length=32), primary_key=True),
        sa.Column('cpf', sa.String(length=11)),
        sa.Column('name', sa.String(length=32)),
        sa.Column('email', sa.String(length=32)),
        sa.Column('password', sa.String(length=64)),
        sa.Column('is_staff', sa.Boolean),
    )


def downgrade():
    op.drop_table('users')
