from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_PROJECT_PATH = Path(__file__).resolve().parent.parent.parent.parent


class Settings(BaseSettings):
    DB_URL: str
    model_config = SettingsConfigDict(
        env_file=BASE_PROJECT_PATH / ".env", env_file_encoding="utf-8"
    )


settings = Settings()  # ty:ignore[missing-argument]
