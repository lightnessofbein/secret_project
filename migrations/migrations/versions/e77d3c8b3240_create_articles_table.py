"""Create articles table

Revision ID: e77d3c8b3240
Revises: 0950082f99e7
Create Date: 2023-04-16 22:18:44.805118

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Text


# revision identifiers, used by Alembic.
revision = 'e77d3c8b3240'
down_revision = '0950082f99e7'
branch_labels = None
depends_on = None



def upgrade():
    op.execute('CREATE SEQUENCE article_id_seq')
    op.create_table(
        'article',
        sa.Column('id', sa.Integer, sa.Sequence('article_id_seq'), primary_key=True, server_default=sa.text("nextval('article_id_seq'::regclass)")),
        sa.Column('topic_id', sa.Integer),
        sa.Column('author_id', sa.Integer),
        sa.Column('article_name', sa.String(255)),
        sa.Column('article_body', sa.Text)
    )

    article_table = table('article',
        column('id', Integer),
        column('topic_id', Integer),
        column('author_id', Integer),
        column('article_name', String),
        column('article_body', Text)
    )

    op.bulk_insert(article_table,
        [
            {'topic_id': 1, 'author_id': 1, 'article_name': 'Example Article 1', 'article_body': 'This is an example article body.'},
            {'topic_id': 2, 'author_id': 2, 'article_name': 'Example Article 2', 'article_body': 'This is another example article body.'}
        ]
    )

def downgrade():
    pass
