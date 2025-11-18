from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import aiosqlite
from bot.database import DB_PATH
from bot.calculations import calculate_cart_total
from bot.utils import gen_order_uid, now
from bot.keyboards import cart_item_kb

router = Router()

async def show_cart(message: Message):
    user_id = message.from_user.id
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute('SELECT id, link, size, category, price_yuan FROM cart WHERE user_id=?', (user_id,))
        rows = await cur.fetchall()
    if not rows:
        await message.answer('Ваша корзина пуста.')
        return
    text = 'Корзина:\n'
    items = []
    for r in rows:
        text += f"#{r[0]} — {r[1]} | {r[3]} | {r[2]} | {r[4]}¥\n"
        items.append({'category': r[3], 'price_yuan': r[4], 'qty':1})
    total = calculate_cart_total(items)
    text += f"\nИтог: {total:.0f} ₽\n\nОтправьте /checkout чтобы оформить заказ."
    await message.answer(text)
