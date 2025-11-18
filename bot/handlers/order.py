from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
import aiosqlite
from bot.database import DB_PATH
from bot.utils import now

router = Router()

class OrderStates(StatesGroup):
    waiting_link = State()
    waiting_category = State()
    waiting_size = State()
    waiting_price = State()
    confirm = State()

async def start_order_flow(message: Message):
    await message.answer('Отправьте ссылку на товар:')
    await OrderStates.waiting_link.set()

@router.message(OrderStates.waiting_link)
async def process_link(message: Message, state: FSMContext):
    await state.update_data(link=message.text)
    await message.answer('Укажите категорию (shoes/clothes/small):')
    await OrderStates.waiting_category.set()

@router.message(OrderStates.waiting_category)
async def process_category(message: Message, state: FSMContext):
    await state.update_data(category=message.text.lower())
    await message.answer('Введите размер (или -):')
    await OrderStates.waiting_size.set()

@router.message(OrderStates.waiting_size)
async def process_size(message: Message, state: FSMContext):
    await state.update_data(size=message.text)
    await message.answer('Введите цену в юанях (число):')
    await OrderStates.waiting_price.set()

@router.message(OrderStates.waiting_price)
async def process_price(message: Message, state: FSMContext):
    try:
        price = float(message.text)
    except:
        await message.answer('Пожалуйста, введите число (например 120.5)')
        return
    data = await state.get_data()
    link = data.get('link')
    cat = data.get('category')
    size = data.get('size')
    # save to cart
    user_id = message.from_user.id
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('INSERT INTO cart(user_id, link, size, category, price_yuan) VALUES (?,?,?,?,?)',
                         (user_id, link, size, cat, price))
        await db.commit()
    await message.answer('Товар добавлен в корзину ✅')
    await state.clear()
