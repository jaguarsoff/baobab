from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from bot.handlers.order import start_order

router = Router()

@router.message(Text("🛒 Заказать"))
async def order_btn(message: Message, state):
    await start_order(message, state)
