from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from bot.config import settings

router = Router()

@router.message(Text("📏 Расчёт"))
async def start_calc(message: Message):
    await message.answer("Введите цену в юанях:")

@router.message()
async def calc_result(message: Message):
    try:
        price = float(message.text)
        rub = price * settings.YUAN_RATE
        await message.answer(f"По курсу: {rub} ₽")
    except:
        pass
