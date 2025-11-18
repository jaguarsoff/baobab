
from aiogram.types import Message

async def start_order_flow(message: Message):
    await message.answer("Отправьте ссылку на товар:")
