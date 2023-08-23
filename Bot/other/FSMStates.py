from aiogram.fsm.state import StatesGroup, State

class SetParams(StatesGroup):
    flat_type = State()
    price_from = State()
    price_to = State()
    commission = State()