"""addcolumn

Revision ID: 4221be930416
Revises: 70e299f270bc
Create Date: 2026-01-10 21:24:12.461891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4221be930416'
down_revision: Union[str, Sequence[str], None] = '70e299f270bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
