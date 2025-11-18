
from aiogram import Router, F
from aiogram.types import Message
from bot.handlers.order import start_order

router=Router()

@router.message(F.text=="🛒 Заказать")
async def go_order(message: Message):
    await start_order(message)
