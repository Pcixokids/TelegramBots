from aiogram.dispatcher.filters.state import State, StatesGroup

class registration_state(StatesGroup):
    sex = State()
    target = State()
    name = State()
    age = State()
    city = State()
    description = State()
    foto = State()