
from aiogram import Router, F
from aiogram.types import Message
from bot.db import new_order

router=Router()

async def start_order(message: Message):
    await message.answer("Отправьте ссылку товара:")

@router.message(F.text.startswith("http"))
async def receive_link(message: Message):
    new_order(message.from_user.id, message.text, "-", "-", 1, 0, 1)
    await message.answer("Заказ создан!")
