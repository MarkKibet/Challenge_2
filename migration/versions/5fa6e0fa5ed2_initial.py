"""Initial

Revision ID: 5fa6e0fa5ed2
Revises:
Create Date: 2025-03-09 14:37:39.654044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision: str = '5fa6e0fa5ed2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('character_name', sa.String, nullable=False)
    )

    
    op.create_table(
        'auditions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('actor', sa.String, nullable=False),
        sa.Column('location', sa.String, nullable=False),
        sa.Column('phone', sa.Integer, nullable=False),
        sa.Column('hired', sa.Boolean, default=False),
        sa.Column('role_id', sa.Integer, sa.ForeignKey('roles.id'))
    )

def downgrade() -> None:
    """Downgrade schema."""
    # Drop the auditions table
    op.drop_table('auditions')

    # Drop the roles table
    op.drop_table('roles')
