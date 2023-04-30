from aiogram.dispatcher.filters.state import StatesGroup, State


class BombsState(StatesGroup):
    count = State()
    field = State()