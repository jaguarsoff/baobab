from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    buttons = [
        [KeyboardButton('🛒 Заказать'), KeyboardButton('📦 Мои заказы')],
        [KeyboardButton('🧾 Корзина'), KeyboardButton('💱 Расчёт')],
        [KeyboardButton('❓ Помощь')]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def cart_item_kb(item_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Удалить', callback_data=f'del:{item_id}'),
         InlineKeyboardButton('Оформить', callback_data=f'checkout:{item_id}')]
    ])
