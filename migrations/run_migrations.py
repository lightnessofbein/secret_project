from alembic.config import Config
from alembic import command

import os

#TODO: add secrets for host, password, port and db also.
db_host = os.environ.get('DB_HOST', 'localhost')
db_url = f'postgresql://postgres:postgres@{db_host}:5432/mydatabase'

alembic_cfg = Config("alembic.ini")
alembic_cfg.set_main_option('sqlalchemy.url', db_url)
command.upgrade(alembic_cfg, "head")
