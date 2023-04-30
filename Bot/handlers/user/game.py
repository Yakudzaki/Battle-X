from loader import dp
from aiogram import Dispatcher, types
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
    await BombsState.field.set()
    field = generate(message.text)
    await state.update_data(field=field)
    await message.answer('Минное поле', reply_markup=generate_field(field))

@dp.callback_query_handler(state=BombsState.field)
async def game(call: types.CallbackQuery, state: FSMContext):
    _, cell, index = call.data.split()
    data = await state.get_data()
    field = data.get('field')
    print(await state.get_data())
    if int(cell) == 0:
        field[int(index)] = 2
        await state.update_data(field=field)
        await call.message.edit_text('Поле:', reply_markup=generate_field(field))
    if int(cell) == 1:
        await state.finish()
        await call.message.edit_text("Вы проиграли")
        await call.message.answer('💣')
