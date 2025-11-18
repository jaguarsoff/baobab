from bot.config import settings

def calculate_price(category, price, weight=1):
    base = price * settings.YUAN_RATE

    if category == "shoes":
        fee = settings.SHOES_FEE
    elif category == "clothes":
        fee = settings.CLOTHES_FEE
    elif category == "small":
        fee = price * settings.YUAN_RATE * settings.SMALL_ITEM_PERCENT
    else:
        fee = 0

    delivery = settings.DELIVERY_PRICE_PER_KG * weight
    return base + fee + delivery
