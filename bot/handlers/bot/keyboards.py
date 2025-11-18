
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🛒 Заказать")],
            [KeyboardButton(text="📦 Мои заказы")]
        ],
        resize_keyboard=True
    )
