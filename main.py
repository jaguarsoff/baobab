import asyncio
from aiogram import Bot, Dispatcher
from bot.config import settings
from bot.db import init_db

from bot.handlers.start import router as start_router
from bot.handlers.menu import router as menu_router
from bot.handlers.order import router as order_router
from bot.handlers.cart import router as cart_router
from bot.handlers.calc import router as calc_router
from bot.handlers.checkout import router as checkout_router
from bot.handlers.my_orders import router as my_orders_router
from bot.handlers.admin_panel import router as admin_router

async def main():
    await init_db()
    bot = Bot(token=settings.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(order_router)
    dp.include_router(cart_router)
    dp.include_router(calc_router)
    dp.include_router(checkout_router)
    dp.include_router(my_orders_router)
    dp.include_router(admin_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
