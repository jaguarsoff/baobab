
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🛒 Заказать"), KeyboardButton(text="📦 Мои заказы")],
            [KeyboardButton(text="🧮 Расчёт"), KeyboardButton(text="ℹ️ Помощь")]
        ],
        resize_keyboard=True
    )
