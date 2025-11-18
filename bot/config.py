from pydantic import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_IDS: str

    YUAN_RATE: float = 12.3
    DELIVERY_PRICE_PER_KG: int = 600
    SHOES_FEE: int = 800
    CLOTHES_FEE: int = 500
    BULK_DISCOUNT_COUNT: int = 3
    BULK_PRICE: int = 350
    SMALL_ITEM_PERCENT: float = 1.0

    class Config:
        env_file = '../.env'  # when running from project root

settings = Settings()
