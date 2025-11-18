
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.config import settings

router=Router()

@router.message(Command("admin"))
async def admin_panel(message: Message):
    if message.from_user.id != settings.ADMIN_ID:
        return await message.answer("Нет доступа.")
    await message.answer("Админ панель готова.")
