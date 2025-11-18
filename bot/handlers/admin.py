from aiogram import Router, F
from aiogram.types import Message
from bot.config import settings
import aiosqlite
from bot.database import DB_PATH
from aiogram import types

router = Router()

@router.message(F.text.startswith('/admin'))
async def admin_panel(message: Message):
    admin_ids = [int(x.strip()) for x in settings.ADMIN_IDS.split(',') if x.strip()]
    if message.from_user.id not in admin_ids:
        await message.answer('Нет доступа.')
        return
    # simple admin commands: /admin orders, /admin set <order_uid> <status> <tracking?>
    parts = message.text.split()
    if len(parts) >= 2 and parts[1] == 'orders':
        async with aiosqlite.connect(DB_PATH) as db:
            rows = await db.execute_fetchall('SELECT order_uid, total_rub, status, tracking FROM orders ORDER BY id DESC LIMIT 50')
        text = 'Последние заказы:\n'
        for r in rows:
            text += f"{r[0]} — {r[2]} — {r[1]:.0f} ₽ — {r[3] or '-'}\n"
        await message.answer(text)
        return
    if len(parts) >= 4 and parts[1] == 'set':
        order_uid = parts[2]
        new_status = parts[3]
        tracking = parts[4] if len(parts) >=5 else None
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute('UPDATE orders SET status=?, tracking=? WHERE order_uid=?', (new_status, tracking, order_uid))
            await db.commit()
            # notify user
            cur = await db.execute('SELECT user_id FROM orders WHERE order_uid=?', (order_uid,))
            row = await cur.fetchone()
            if row:
                user_id = row[0]
                await message.bot.send_message(user_id, f'Статус заказа #{order_uid} изменён: {new_status}. Трек: {tracking or "-"}')
        await message.answer('Готово.')
        return
    await message.answer('Admin: /admin orders | /admin set <order_uid> <status> [tracking]') 
