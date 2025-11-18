
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str = "YOUR_TOKEN"
    ADMIN_ID: int = 123

settings = Settings()
