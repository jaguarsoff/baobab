
from aiogram import Router, F
from aiogram.types import Message
from bot.handlers.order import start_order_flow

router = Router()

@router.message(F.text == "🛒 Заказать")
async def on_order(message: Message):
    await start_order_flow(message)
