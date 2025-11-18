from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str = "TOKEN"
    ADMIN_ID: int = 123456
    YUAN_RATE: float = 12.3
    DELIVERY_PRICE_PER_KG: int = 600
    SHOES_FEE: int = 800
    CLOTHES_FEE: int = 500
    BULK_DISCOUNT_COUNT: int = 3
    BULK_PRICE: int = 350
    SMALL_ITEM_PERCENT: float = 1.0

    class Config:
        env_file = ".env"

settings = Settings()
