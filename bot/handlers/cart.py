from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
import aiosqlite
from bot.db import DB_PATH

router = Router()

@router.message(Text("🧺 Корзина"))
async def show_cart(message: Message):
    uid = message.from_user.id
    async with aiosqlite.connect(DB_PATH) as db:
        rows = await db.execute_fetchall("SELECT id, link, size, category, price FROM cart WHERE user_id=?", (uid,))

    if not rows:
        return await message.answer("Корзина пуста.")

    text = "🧺 *Корзина:*\n\n"
    for r in rows:
        text += f"#{r[0]} — {r[1]} | {r[3]} | {r[2]} | {r[4]}¥\n"

    await message.answer(text, parse_mode="Markdown")
