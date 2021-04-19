"""fixing numeric field

Revision ID: 59dd3e454579
Revises: 642f3fd59a17
Create Date: 2021-04-19 15:04:28.633755

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '59dd3e454579'
down_revision = '642f3fd59a17'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('sales', 'value')
    op.add_column('sales', sa.Column('value', sa.Float))


def downgrade():
    op.drop_column('sales', 'value')
    op.add_column('sales', sa.Column('value', sa.Numeric(precision=2)))
