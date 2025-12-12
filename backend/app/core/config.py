from pydantic_settings import BaseSettings
from pydantic import Field, ConfigDict


class Settings(BaseSettings):
    """
    Application Settings

    This class loads environment variables from the .env file
    Pydantic will automatically convert types and validate them
    """


    # Project Info
    PROJECT_NAME: str = "GuildOps"
    PROJECT_VERSION: str = "0.1.0"
    DEBUG: bool = True


    # Database Settings
    DATABASE_URL: str = "sqlite+aiosqlite:///./guildops.db"

    # AI Config
    OPENAI_API_KEY: str 


    # This config tells Pydantic to read from a .env file
    model_config = ConfigDict(env_file=".env", extra="ignore")


settings = Settings()