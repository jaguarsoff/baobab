from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from bot.states import OrderStates
import aiosqlite
from bot.db import DB_PATH

router = Router()

async def start_order(message: Message, state: FSMContext):
    await state.set_state(OrderStates.waiting_link)
    await message.answer("Введите ссылку на товар:")

@router.message(OrderStates.waiting_link)
async def process_link(message: Message, state: FSMContext):
    await state.update_data(link=message.text)
    await state.set_state(OrderStates.waiting_category)
    await message.answer("Укажите категорию (shoes/clothes/small):")

@router.message(OrderStates.waiting_category)
async def process_category(message: Message, state: FSMContext):
    await state.update_data(category=message.text)
    await state.set_state(OrderStates.waiting_size)
    await message.answer("Введите размер (или '-' если нет):")

@router.message(OrderStates.waiting_size)
async def process_size(message: Message, state: FSMContext):
    await state.update_data(size=message.text)
    await state.set_state(OrderStates.waiting_price)
    await message.answer("Введите цену в юанях:")

@router.message(OrderStates.waiting_price)
async def process_price(message: Message, state: FSMContext):
    data = await state.get_data()
    uid = message.from_user.id

    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO cart(user_id, link, size, category, price) VALUES (?, ?, ?, ?, ?)",
            (uid, data['link'], data['size'], data['category'], float(message.text))
        )
        await db.commit()

    await message.answer("Товар добавлен в корзину!")
    await state.clear()
