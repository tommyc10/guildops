# backend/alembic/env.py

import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

# ----------------- 1. IMPORTS ADDED -----------------
import sys
import os

# Add the parent directory to path so we can import 'app'
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.config import settings       # To get DATABASE_URL
from app.models.models import Base         # To get Table Definitions
# ----------------------------------------------------

# this is the Alembic Config object
config = context.config

# ----------------- 2. OVERRIDE URL -----------------
# Force Alembic to use the URL from our Pydantic settings
# This ensures .env and Alembic always agree
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
# ---------------------------------------------------

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ----------------- 3. SET METADATA -----------------
# This tells Alembic: "Look at these classes to see what tables should exist"
target_metadata = Base.metadata
# ---------------------------------------------------

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode (no DB connection needed)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode (connects to DB)."""
    
    # Create an Async Engine
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())