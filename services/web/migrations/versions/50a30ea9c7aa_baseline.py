"""baseline

Revision ID: 50a30ea9c7aa
Revises: 
Create Date: 2020-07-29 13:44:37.793393

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '50a30ea9c7aa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        "CREATE TABLE IF NOT EXISTS grocery_lists ("
            "id serial NOT NULL PRIMARY KEY,"
            "name varchar"
        ");"
    )
    op.execute(
        "CREATE TABLE IF NOT EXISTS grocery_items ("
            "id serial NOT NULL PRIMARY KEY,"
            "list_id integer NOT NULL,"
            "name varchar,"
            "quantity integer,"
            "FOREIGN KEY(list_id) REFERENCES grocery_lists(id)"
        ");"
    )


def downgrade():
    op.execute("DROP TABLE IF EXISTS grocery_items;")
    op.execute("DROP TABLE IF EXISTS grocery_lists;")



