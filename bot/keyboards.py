from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🛒 Заказать")],
            [KeyboardButton(text="🧺 Корзина"), KeyboardButton(text="📦 Мои заказы")],
            [KeyboardButton(text="📘 Помощь"), KeyboardButton(text="📏 Расчёт")]
        ],
        resize_keyboard=True
    )
