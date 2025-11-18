from aiogram import Router
from aiogram.types import Message
from bot.calculations import calculate_item_price

router = Router()

@router.message()
async def calc_start(message: Message):
    # if user clicked calc button, they may send like "120 shoes"
    parts = message.text.split()
    if len(parts) >= 2:
        try:
            price = float(parts[0])
            cat = parts[1]
            rub = calculate_item_price(cat, price)
            await message.answer(f'Примерная цена: {rub:.0f} ₽ (включая доставку/комиссию)')
        except:
            pass
