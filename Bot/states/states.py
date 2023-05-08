from aiogram.dispatcher.filters.state import StatesGroup, State


class BombsState(StatesGroup):
    rate = State()
    count = State()
    field = State()

class CoinState(StatesGroup):
    rate = State()
    count_guess = State()
