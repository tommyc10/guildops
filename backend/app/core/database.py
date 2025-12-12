# backend/app/core/database.py

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from app.core.config import settings

# 1. DATABASE URL
# We need to make sure the URL string starts with "sqlite+aiosqlite"
# If your settings.DATABASE_URL is just "sqlite:///...", we force the async driver here.
# ideally, update your .env to be: DATABASE_URL=sqlite+aiosqlite:///./guildops.db
db_url = settings.DATABASE_URL
if not db_url.startswith("sqlite+aiosqlite"):
    db_url = "sqlite+aiosqlite:///./guildops.db"

# 2. ASYNC ENGINE
engine = create_async_engine(
    db_url,
    echo=settings.DEBUG,
    connect_args={"check_same_thread": False} # Needed for SQLite
)

# 3. ASYNC SESSION FACTORY
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 4. BASE MODEL
Base = declarative_base()

# 5. DEPENDENCY
# This is what we will use in our API routes to get a DB connection
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()