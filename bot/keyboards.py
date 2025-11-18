from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🛒 Заказать"),
                KeyboardButton(text="📦 Мои заказы"),
            ],
            [
                KeyboardButton(text="🧮 Расчёт"),
                KeyboardButton(text="🛠 Помощь"),
            ]
        ],
        resize_keyboard=True
    )


def cart_item_kb(item_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Удалить', callback_data=f'del:{item_id}'),
         InlineKeyboardButton('Оформить', callback_data=f'checkout:{item_id}')]
    ])
