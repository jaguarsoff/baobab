from aiogram import Router
from aiogram.types import Message
import aiosqlite
from bot.database import DB_PATH

router = Router()

async def my_orders(message: Message):
    user_id = message.from_user.id
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute('SELECT order_uid, total_rub, status, tracking FROM orders WHERE user_id=?', (user_id,))
        rows = await cur.fetchall()
    if not rows:
        await message.answer('У вас нет заказов.')
        return
    text = 'Мои заказы:\n'
    for r in rows:
        text += f"Заказ #{r[0]} — {r[2]} — {r[3] or '-'} — {r[1]:.0f} ₽\n"
    await message.answer(text)
