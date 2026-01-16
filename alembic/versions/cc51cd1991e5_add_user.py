"""add_user

Revision ID: cc51cd1991e5
Revises: 4221be930416
Create Date: 2026-01-10 21:33:21.300770

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc51cd1991e5'
down_revision: Union[str, Sequence[str], None] = '4221be930416'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "USERS",
    
        sa.Column("id",sa.Integer(),nullable=False,primary_key=True),
        sa.Column("email",sa.String(),nullable=False,unique=True),
        sa.Column("passW",sa.String(),nullable=False),
        sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False)
    )
def downgrade() -> None:
    
    op.drop_table('users')
