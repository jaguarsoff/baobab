
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from bot.handlers.start import router as start_router
from bot.handlers.menu import router as menu_router

async def main():
    bot = Bot(token="TEST", parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(menu_router)
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())
