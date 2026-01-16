"""add_foreign_key

Revision ID: e802c6d3c153
Revises: cc51cd1991e5
Create Date: 2026-01-10 21:52:23.829023

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e802c6d3c153'
down_revision: Union[str, Sequence[str], None] = 'cc51cd1991e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


"""add_foreign_key_to_posts_table.py"""



def upgrade() -> None:
    """Add foreign key constraint from posts.owner_id to users.id"""
    
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    
    
    op.create_foreign_key(
        'post_users_fk',  # constraint name
        source_table='posts',  # table with the foreign key
        referent_table='USERS',  # table being referenced
        local_cols=['owner_id'],  # column in posts table
        remote_cols=['id'],  # column in users table
        ondelete='CASCADE'  # delete posts when user is deleted
    )


def downgrade() -> None:
    """Remove foreign key constraint and column"""
    # Drop the foreign key constraint first
    op.drop_constraint('post_users_fk', 'posts', type_='foreignkey')
    
    # Then drop the owner_id column
    op.drop_column('posts', 'owner_id')