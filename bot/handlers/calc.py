from aiogram import Router, F
from aiogram.types import Message
from bot.calculations import calculate_item_price

router = Router()

@router.message(F.text == '💱 Расчёт')
async def calc_start(message: Message):
    await message.answer('Отправьте цену в юанях и категорию через пробел: например "120 shoes"')

@router.message()
async def calc_process(message: Message):
    parts = message.text.split()
    if len(parts) >= 2:
        try:
            price = float(parts[0])
            cat = parts[1]
            rub = calculate_item_price(cat, price)
            await message.answer(f'Примерная цена: {rub:.0f} ₽ (включая доставку/комиссию)')
        except:
            pass
