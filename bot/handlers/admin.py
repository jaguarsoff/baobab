from aiogram import Router, F
from aiogram.types import Message
from bot.config import settings
import aiosqlite
from bot.database import DB_PATH

router = Router()

@router.message()
async def admin_panel(message: Message):
    text = message.text.strip()
    if not text.startswith('/admin'):
        return
    admin_ids = [int(x.strip()) for x in settings.admin_ids.split(',') if x.strip()]
    if message.from_user.id not in admin_ids:
        await message.answer('Нет доступа.')
        return
    parts = text.split()
    if len(parts) >= 2 and parts[1] == 'orders':
        async with aiosqlite.connect(DB_PATH) as db:
            cur = await db.execute('SELECT order_uid, total_rub, status, tracking FROM orders ORDER BY id DESC LIMIT 50')
            rows = await cur.fetchall()
        rtext = 'Последние заказы:\n'
        for r in rows:
            rtext += f"{r[0]} — {r[2]} — {r[1]:.0f} ₽ — {r[3] or '-'}\n"
        await message.answer(rtext)
        return
    if len(parts) >= 4 and parts[1] == 'set':
        order_uid = parts[2]
        new_status = parts[3]
        tracking = parts[4] if len(parts) >=5 else None
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute('UPDATE orders SET status=?, tracking=? WHERE order_uid=?', (new_status, tracking, order_uid))
            await db.commit()
            cur = await db.execute('SELECT user_id FROM orders WHERE order_uid=?', (order_uid,))
            row = await cur.fetchone()
            if row:
                user_id = row[0]
                await message.bot.send_message(user_id, f'Статус заказа #{order_uid} изменён: {new_status}. Трек: {tracking or "-"}')
        await message.answer('Готово.')
        return
    await message.answer('Admin: /admin orders | /admin set <order_uid> <status> [tracking]')
