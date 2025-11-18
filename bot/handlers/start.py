from aiogram import Router, F
from aiogram.types import Message
from bot.keyboards import main_menu

router = Router()

@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Привет! Я Poizon-бот. Выберите действие:', reply_markup=main_menu())
