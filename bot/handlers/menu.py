from aiogram import Router, F
from aiogram.types import Message
from bot.handlers.order import start_order_flow
from bot.handlers.cart import show_cart
from bot.handlers.calc import calc_start
from bot.handlers.my_orders import my_orders
from bot.handlers.help import help_cmd

router = Router()

@router.message(F.text == '🛒 Заказать')
async def on_order_button(message: Message):
    await start_order_flow(message)

@router.message(F.text == '🧾 Корзина')
async def on_cart_button(message: Message):
    await show_cart(message)

@router.message(F.text == '💱 Расчёт')
async def on_calc_button(message: Message):
    await calc_start(message)

@router.message(F.text == '📦 Мои заказы')
async def on_my_orders(message: Message):
    await my_orders(message)

@router.message(F.text == '❓ Помощь')
async def on_help(message: Message):
    await help_cmd(message)
