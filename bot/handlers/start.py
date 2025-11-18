from aiogram import Router
from aiogram.types import Message
from bot.keyboards import main_menu
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer('Привет! Я Poizon-бот. Выберите действие:', reply_markup=main_menu())
