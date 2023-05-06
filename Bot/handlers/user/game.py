from loader import dp
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command, StateFilter
import random
from aiogram.dispatcher import FSMContext
from states import BombsState
from utils.test import generate
from utils.gen_field import generate_field
from test import calculate
from keyboards.inline.games_kb import games

from utils.db.db_utils import get_user

@dp.message_handler(Command('game'))
async def game(message: types.Message):
    nickname = get_user(message.from_user.id).nickname
    await message.answer(f'{nickname}, выберите одну из игр', reply_markup=games)

@dp.callback_query_handler(lambda m: m.data == 'Minefield')
async def minefield(call: types.CallbackQuery):
    await call.message.answer()


@dp.message_handler(state=BombsState.rate)
async def game(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Пожалуйста введите число')
        return
    await state.update_data(rate=int(message.text))
    await BombsState.count.set()
    
    data = await state.get_data()
    rate = data.get('rate')
    await message.answer('<b>Выберите кол-во бомб</b>')
    

@dp.message_handler(state=BombsState.count)
async def game(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Пожалуйста введите число')
        return
    if 5 > int(message.text) or int(message.text) > 24:
        await message.answer('вы забанены за абьюз системы')
        return
    await state.update_data(count=int(message.text))
    await BombsState.field.set()
    data = await state.get_data()
    rate = data.get('rate')
    count = data.get('count')

    field = generate(count=count)
    await state.update_data(field=field)

    await message.answer(
        '⠀<b>Минное поле 💣</b>\n\n'
        '➖➖➖➖➖➖➖\n'
        f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
        f'<b>❓ Кол-во мин:</b> <code>{count} шт.</code>\n'
        '➖➖➖➖➖➖➖\n'
        f'<b>💰 Множитель:</b> <code>0x</code>\n'
        f'<b>💣 Отгадано бомб:</b> <code>0 шт.</code>\n\n'
        f'<b>Сумма выигрыша:</b> <code>0 ₽</code>\n', reply_markup=generate_field(field))


@dp.callback_query_handler(lambda m: len(m.data.split()) == 3, state=BombsState.field)
async def game(call: types.CallbackQuery, state: FSMContext):
    _, cell, index = call.data.split()
    data = await state.get_data()
    field = data.get('field')
    rate = data.get('rate')
    count = data.get('count')

    if int(cell) == 0:
        field[int(index)] = 2
        await state.update_data(field=field)
        await call.message.edit_text(
            '⠀<b>Минное поле 💣</b>\n\n'
            '➖➖➖➖➖➖➖\n'
            f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
            f'<b>❓ Кол-во мин:</b> <code>{count} шт.</code>\n'
            '➖➖➖➖➖➖➖\n'
            f'<b>💰 Множитель:</b> <code>{calculate(25 - count, field.count(2))}x</code>\n'
            f'<b>💣 Отгадано бомб:</b> <code>{field.count(2)} шт.</code>\n\n'
            f'<b>Сумма выигрыша:</b> <code>{calculate(25 - count, field.count(2)) * rate} ₽</code>\n', reply_markup=generate_field(field))
    if int(cell) == 1:
        await state.finish()
        field[int(index)] = 3
        await call.message.edit_text(
            '⠀<b>Минное поле 💣</b>\n\n'
            '➖➖➖➖➖➖➖\n'
            f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
            f'<b>❓ Кол-во мин:</b> <code>{count} шт.</code>\n'
            '➖➖➖➖➖➖➖\n'
            f'<b>💰 Множитель:</b> <code>{calculate(25 - count, field.count(2))}x</code>\n'
            f'<b>💣 Отгадано бомб:</b> <code>{field.count(2)} шт.</code>\n'
            '➖➖➖➖➖➖➖\n\n'
            '<b>Проигрыш, попробуй снова!</b>', reply_markup=generate_field(field, finish=True))
        await call.message.answer('💣')


