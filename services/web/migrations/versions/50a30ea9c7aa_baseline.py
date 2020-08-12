"""baseline

Revision ID: 50a30ea9c7aa
Revises: 
Create Date: 2020-07-29 13:44:37.793393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50a30ea9c7aa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "grocery_lists",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String)
    )
    op.create_table(
        "grocery_items",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('list_id', sa.Integer, sa.ForeignKey('grocery_lists.id'), nullable=False),
        sa.Column('name', sa.String),
        sa.Column('quantity', sa.Integer)
    )


def downgrade():
    op.drop_table('grocery_items')
    op.drop_table('grocery_lists')
