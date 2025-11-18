
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str = "8288012104:AAEy_eFaSjwG8DGBQaRPQGy2cG3pFpCzTqE"
    ADMIN_ID: int = 8254985499

settings = Settings()
