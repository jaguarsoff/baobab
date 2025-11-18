
import asyncio
from aiogram import Bot, Dispatcher
from bot.config import settings
from bot.db import init_db
from bot.handlers.start import router as start_router
from bot.handlers.menu import router as menu_router
from bot.handlers.order import router as order_router
from bot.handlers.admin import router as admin_router

async def main():
    bot = Bot(settings.BOT_TOKEN)
    dp = Dispatcher()
    await init_db()
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(order_router)
    dp.include_router(admin_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
