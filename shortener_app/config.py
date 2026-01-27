from pydantic_settings import BaseSettings, SettingsConfigDict

from functools import lru_cache

class Settings (BaseSettings):
    env_name: str ="Local"
    base_url : str= "http://localhost:8000"
    db_url : str = "sqlite:///./shortener.db"
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",          # 🔥 THIS LINE FIXES IT
    )


@lru_cache()
def get_settings()->Settings:
    settings =Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings

