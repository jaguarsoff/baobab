from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    bot_token: str = Field(..., env="BOT_TOKEN")
    admin_ids: str = Field('', env="ADMINS")

    YUAN_RATE: float = 12.3
    DELIVERY_PRICE_PER_KG: int = 600
    SHOES_FEE: int = 800
    CLOTHES_FEE: int = 500
    BULK_DISCOUNT_COUNT: int = 3
    BULK_PRICE: int = 350
    SMALL_ITEM_PERCENT: float = 1.0

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
