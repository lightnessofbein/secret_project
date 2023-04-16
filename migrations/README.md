# Database Migrations

This repository contains the code and configuration for managing database migrations using Alembic and Python.

## Prerequisites

Before running the migrations, you'll need to install the required dependencies by running the following command:

```pip install -r requirements.txt```


You'll also need to update the `alembic.ini` file with the appropriate connection string for your PostgreSQL database.

## Running Migrations

To run the migrations and update your database schema to the latest version, you can use the `run_migrations.py` script. Here's an example of how you might do this:

```python run_migrations.py```


This script will run all pending migrations and update your database schema to the latest version.

## Creating New Migrations

To create a new migration script that defines changes to the database schema, you can use the `alembic revision` command with the `--autogenerate` option. Here's an example of how you might do this:

```alembic revision --autogenerate -m “Description of changes”```


This command will generate a new migration script in the `migrations/versions` directory. You can open this file and update the `upgrade` and `downgrade` functions to define the changes to the database schema.

Once you've updated the migration script, you can run it using the `alembic upgrade` command to apply the changes to your database.

## Rolling Back Migrations

If you need to roll back a migration and undo changes to the database schema, you can use the `alembic downgrade` command. Here's an example of how you might do this:

 ```alembic downgrade -1```


This command will roll back the most recent migration and undo its changes to the database schema.