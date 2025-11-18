from bot.config import settings

def calculate_item_price(category: str, price_yuan: float, weight_kg: float = 1.0):
    base = price_yuan * settings.YUAN_RATE

    if category == 'shoes':
        fee = settings.SHOES_FEE
    elif category == 'clothes':
        fee = settings.CLOTHES_FEE
    elif category == 'small':
        fee = base * settings.SMALL_ITEM_PERCENT
    else:
        fee = 0

    delivery = settings.DELIVERY_PRICE_PER_KG * weight_kg
    return base + fee + delivery

def calculate_cart_total(items):
    # items: list of dicts with keys category, price_yuan, qty (optional), weight (optional)
    total = 0.0
    counts = {'shoes':0, 'clothes':0}
    for it in items:
        cat = it.get('category')
        qty = int(it.get('qty',1))
        if cat in counts:
            counts[cat] += qty

    for it in items:
        cat = it.get('category')
        price = float(it.get('price_yuan',0))
        qty = int(it.get('qty',1))
        weight = float(it.get('weight',1.0))
        per = calculate_item_price(cat, price, weight)
        # Apply bulk discount: if total count of this category >= BULK_DISCOUNT_COUNT, price replaced by BULK_PRICE per item
        if cat in ('shoes','clothes') and counts.get(cat,0) >= settings.BULK_DISCOUNT_COUNT:
            per = settings.BULK_PRICE + settings.DELIVERY_PRICE_PER_KG * weight
        total += per * qty
    return total
