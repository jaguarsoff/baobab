from aiogram import Router
from aiogram.types import Message
from bot.keyboards import main_menu

router = Router()

@router.message(commands=['start'])
async def cmd_start(message: Message):
    await message.answer('Привет! Я Poizon-бот. Выберите действие:', reply_markup=main_menu())
