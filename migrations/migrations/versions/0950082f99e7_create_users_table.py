"""Create users table

Revision ID: 0950082f99e7
Revises: 
Create Date: 2023-04-16 22:13:57.887670

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer


# revision identifiers, used by Alembic.
revision = '0950082f99e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE SEQUENCE users_id_seq')
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, sa.Sequence('users_id_seq'), primary_key=True, server_default=sa.text("nextval('users_id_seq'::regclass)")),
        sa.Column('name', sa.String(255)),
        sa.Column('email', sa.String(255))
    )

    users_table = table('users',
        column('id', Integer),
        column('name', String),
        column('email', String)
    )

    op.bulk_insert(users_table,
        [
            {'name': 'Alice', 'email': 'alice@example.com'},
            {'name': 'Bob', 'email': 'bob@example.com'}
        ]
    )


def downgrade():
    pass
