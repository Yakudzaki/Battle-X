from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command, StateFilter
import random
from aiogram.dispatcher import FSMContext
from states import BombsState
from utils.test import generate
from utils.gen_field import generate_field

@dp.message_handler(Command('game'))
async def game(message: types.Message):
    await BombsState.count.set()
    await message.answer('Выберите кол-во бомб (Минимум 5, Максимум 24)')

@dp.message_handler(state=BombsState.count)
async def game(message: types.Message, state: FSMContext):
    await state.update_data(count=message.text)
    BombsState.next()
    field = generate(message.text)
    await message.answer('Минное поле', reply_markup=generate_field(field))
    await state.finish()

@dp.callback_query_handler(lambda call: call.data.startswith('Мины'), state=BombsState.field)
async def game(message: types.Message, state: FSMContext):
    await message.answer("Заглушка")

