from aiogram.fsm.state import StatesGroup, State

class OrderStates(StatesGroup):
    waiting_link = State()
    waiting_category = State()
    waiting_size = State()
    waiting_price = State()

class ContactStates(StatesGroup):
    waiting_name = State()
    waiting_phone = State()
