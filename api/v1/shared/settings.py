from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_URL: str = "mysql+mysqlconnector://root:1234@localhost:3306/sergiobot"
    
settings = Settings()