from aiogram import Router
from aiogram.types import Message
import aiosqlite
from bot.database import DB_PATH
from bot.utils import gen_order_uid, now
from bot.calculations import calculate_cart_total
from aiogram.filters import Command

router = Router()

@router.message(Command("checkout"))
async def checkout(message: Message):
    user_id = message.from_user.id
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute('SELECT id, link, size, category, price_yuan FROM cart WHERE user_id=?', (user_id,))
        cart = await cur.fetchall()
        if not cart:
            await message.answer('Корзина пуста.')
            return
        items = []
        for r in cart:
            items.append({'category': r[3], 'price_yuan': r[4], 'qty':1})
        total = calculate_cart_total(items)
        order_uid = gen_order_uid()
        await db.execute('INSERT INTO orders(order_uid, user_id, total_rub, status, created_at) VALUES (?,?,?,?,?)',
                         (order_uid, user_id, total, 'created', now()))
        # get inserted order id
        cur2 = await db.execute('SELECT id FROM orders WHERE order_uid=?', (order_uid,))
        row = await cur2.fetchone()
        order_id = row[0]
        for r in cart:
            await db.execute('INSERT INTO order_items(order_id, link, size, category, price_yuan) VALUES (?,?,?,?,?)',
                             (order_id, r[1], r[2], r[3], r[4]))
        await db.execute('DELETE FROM cart WHERE user_id=?', (user_id,))
        await db.commit()
    await message.answer(f'Заказ #{order_uid} создан. Итог: {total:.0f} ₽\nПосле изменения статуса Вы получите уведомление.')
