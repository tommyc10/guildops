from fastapi import FastAPI
from app.core.config import settings


# Create FastAPI app instance

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)


@app.get("/health")
async def health_check():
    return {
        "status": "active",
        "system": "GuildOps Mission Control",
        "version": settings.PROJECT_VERSION,
        "database": "connected"
    }


@app.get("/")
async def root():
    return {"message": "Welcome to GuildOps Mission Control!"}