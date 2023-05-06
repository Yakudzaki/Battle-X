import random
from utils.minefield import calculate_ratio, generate

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, StateFilter

from keyboards.inline.games_kb import games
from loader import dp
from states import BombsState
from utils.db.db_utils import get_user, withdraw_user_balance, deposite_user_balance
from utils.gen_field import generate_field


@dp.callback_query_handler(lambda m: m.data == 'Minefield' or m.data == 'Мины заново')
async def minefield(call: types.CallbackQuery):
    await call.message.answer('Введите вашу ставку (Минимальная: 10 ₽, Максимальная: 1000 ₽)')
    await BombsState.rate.set()

@dp.message_handler(state=BombsState.rate)
async def game(message: types.Message, state: FSMContext):
    rate = message.text
    if not rate.isdigit():
        await message.answer('<b>Введите число!<b>')
        return
    if get_user(message.from_user.id).balance < int(rate):
        await message.answer('<b>На вашем балансе не достаточно средств!<b>')
        return
    withdraw_user_balance(message.from_user.id, int(rate))
    await state.update_data(rate=int(message.text))
    await BombsState.next()

    await message.answer('Выберите кол-во бомб (Минимум: 3, Максимум: 24)')
    

@dp.message_handler(state=BombsState.count)
async def game(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('<b>Введите число!</b>')
        return
    if 3 > int(message.text) or int(message.text) > 24:
        await message.answer('<b>Введите количество бомб в соответствии с ограничениями!</b>\n\n'
                             '<b>Максимум</b> - <code>24</code>\n'
                             '<b>Минимум</b> - <code>3</code>')
        return
    await state.update_data(count=int(message.text))
    await BombsState.field.set()
    data = await state.get_data()
    rate = data.get('rate')
    count = data.get('count')

    field = generate(count=count)
    await state.update_data(field=field)

    await message.answer(
        '    <b>Минное поле 💣</b>\n\n'
        '➖➖➖➖➖➖➖\n'
        f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
        f'<b>❓ Кол-во бомб:</b> <code>{count} шт.</code>\n'
        '➖➖➖➖➖➖➖\n'
        f'<b>💰 Множитель:</b> <code>0x</code>\n'
        f'<b>💣 Отгадано бомб:</b> <code>0 шт.</code>\n\n'
        f'<b>💲 Сумма выигрыша:</b> <code>0 ₽</code>\n', reply_markup=generate_field(field))


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
            '    <b>Минное поле 💣</b>\n\n'
            '➖➖➖➖➖➖➖\n'
            f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
            f'<b>❓ Кол-во мин:</b> <code>{count} шт.</code>\n'
            '➖➖➖➖➖➖➖\n'
            f'<b>💰 Множитель:</b> <code>{calculate_ratio(count, field.count(2))}x</code>\n'
            f'<b>💣 Отгадано бомб:</b> <code>{field.count(2)} шт.</code>\n\n'
            f'<b>💲 Сумма выигрыша:</b> <code>{calculate_ratio(count, field.count(2)) * rate} ₽</code>\n', reply_markup=generate_field(field))
    if int(cell) == 1:
        await state.finish()
        field[int(index)] = 3
        await call.message.edit_text(
            '.   <b>Минное поле 💣</b>\n\n'
            '➖➖➖➖➖➖➖\n'
            f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
            f'<b>❓ Кол-во бомб:</b> <code>{count} шт.</code>\n'
            '➖➖➖➖➖➖➖\n'
            f'<b>💰 Множитель:</b> <code>{calculate_ratio(count, field.count(2))}x</code>\n'
            f'<b>💣 Отгадано бомб:</b> <code>{field.count(2)} шт.</code>\n'
            '➖➖➖➖➖➖➖\n\n'
            '<b>Проигрыш, попробуй снова!</b>', reply_markup=generate_field(field, finish=True))
        await call.message.answer('💣')


@dp.callback_query_handler(lambda m: m.data == 'Мины приз', state=BombsState.field)
async def game(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    field = data.get('field')
    count = data.get('count')
    rate = data.get('rate')
    ratio = calculate_ratio(count, field.count(2))
    if ratio <= 0.5:
        await call.answer('❌ Вы не можете забрать деньги пока множитель меньше 1x', show_alert=True)
        return
    prize = ratio * rate
    deposite_user_balance(call.from_user.id, prize)
    balance = get_user(call.from_user.id).balance
    await call.message.edit_text(f'Вы успешно забрали деньги, +{prize} ₽\n'
                                 f'Ваш баланс: {balance} ₽')
    await state.finish()
