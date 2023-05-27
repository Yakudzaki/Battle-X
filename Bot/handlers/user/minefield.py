import random

from utils.minefield import calculate_ratio, generate

from utils.format_int import format_int

from aiogram import Dispatcher, types

from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import Command, Text

from keyboards.default.games_kb import games

from keyboards.inline.mines_buttons import stavka_kb, bombs_kb

from loader import dp

from states import BombsState

from utils.db.db_utils import get_user, withdraw_user_balance, deposite_user_balance
from utils.gen_field import generate_field
from decimal import Decimal
from time import sleep


from data.config import sad_smails, right_smails


@dp.message_handler(Text('Минёр 💣'))
async def minefield(message: types.Message):
    await message.answer('💰 Введите сумму ставки\n (От 10 до 1000 ₽)', reply_markup=stavka_kb)
    await BombsState.rate.set()

@dp.callback_query_handler(lambda m: m.data == 'Мины заново')
async def minefield(call: types.CallbackQuery):

    await call.message.answer('💰 Введите вашу ставку', reply_markup=stavka_kb)

    await BombsState.rate.set()


@dp.callback_query_handler(
    lambda m: m.data.startswith('Rate'),
    state=BombsState.rate)
async def game(call: types.CallbackQuery, state: FSMContext):
    rate = call.data.split()[1]

    if (not rate.isnumeric()) or (not rate.isascii()):
        await call.message.answer('<b>⚠️ Введите число!</b>')
        return

    if 10 > int(rate) or int(rate) > 1000:
        await call.message.answer(
            '⚠️ Выберите ставку соблюдая ограничения\n'
            '(От 10 до 1000 ₽)', reply_markup=stavka_kb)
        return

    if get_user(call.from_user.id).balance < int(rate):
        await call.message.answer(f'<b>{random.choice(sad_smails)} На вашем балансе не достаточно средств!</b>')
        return

    withdraw_user_balance(int(call.from_user.id), int(rate))

    await call.message.delete()

    await state.update_data(rate=int(rate))
    await BombsState.next()
    await call.message.answer('💣 Выберите кол-во бомб\n (От 3 до 24)', reply_markup=bombs_kb)

@dp.message_handler(state=BombsState.rate)
async def game(message: types.Message, state: FSMContext):
    rate = message.text

    if (not rate.isnumeric()) or (not rate.isascii()):
        await message.answer('<b>⚠️ Введите число!</b>')
        return
    
    if 10 > int(rate) or int(rate) > 1000:
        await message.answer(
            '⚠️ Выберите ставку соблюдая ограничения\n'
            '(От 10 до 1000 ₽)', reply_markup=stavka_kb)
        return

    if get_user(message.from_user.id).balance < int(rate):
        await message.answer(f'<b>{random.choice(sad_smails)} На вашем балансе не достаточно средств!</b>')
        return

    withdraw_user_balance(int(message.from_user.id), int(rate))

    await state.update_data(rate=int(message.text))
    await BombsState.next()
    await message.answer('💣 Выберите кол-во бомб\n (От 3 до 24)', reply_markup=bombs_kb)


@dp.callback_query_handler(lambda m: m.data.startswith('Bombs'), state=BombsState.count)
async def game(call: types.CallbackQuery, state: FSMContext):
    count = int(call.data.split()[1])

    await call.message.delete()

    await state.update_data(count=count)
    await BombsState.next()
    
    data = await state.get_data()
    rate = data.get('rate')
    count = data.get('count')
    field = generate(count=count)

    await state.update_data(field=field)
    await call.message.answer(
        '<b>👾 Игра - Минёр</b>\n\n'
        '➖➖➖➖➖➖➖\n'
        f'<b>💸 Ставка:</b> <code>{format_int(rate)} ₽</code>\n'
        f'<b>💣 Кол-во бомб:</b> <code>{count} шт.</code>\n'
        '➖➖➖➖➖➖➖\n'
        f'<b>💰 Множитель:</b> <code>0x</code>\n'
        f'<b>💎 Отгадано кристалов:</b> <code>0 шт.</code>\n\n'
        f'<b>🔥 Сумма выигрыша:</b> <code>0 ₽</code>\n', reply_markup=generate_field(field))


@dp.message_handler(state=BombsState.count)
async def game(message: types.Message, state: FSMContext):
    if not message.text.isnumeric():
        await message.answer('<b>⚠️ Введите число!</b>')
        return

    if 3 > int(message.text) or int(message.text) > 24:
        await message.answer('<b>⚠️ Введите количество бомб в соответствии с ограничениями!</b>\n\n'
                             '<b>🔺 Максимум</b> - <code>24</code>\n'
                             '<b>🔻 Минимум</b> - <code>3</code>', reply_markup=bombs_kb)
        return

    await state.update_data(count=int(message.text))
    await BombsState.field.set()
    data = await state.get_data()
    rate = data.get('rate')
    count = data.get('count')
    field = generate(count=count)

    await state.update_data(field=field)
    await message.answer(
        '<b>👾 Игра - Минёр</b>\n\n'
        '➖➖➖➖➖➖➖\n'
        f'<b>💸 Ставка:</b> <code>{format_int(rate)} ₽</code>\n'
        f'<b>💣 Кол-во бомб:</b> <code>{count} шт.</code>\n'
        '➖➖➖➖➖➖➖\n'
        f'<b>💰 Множитель:</b> <code>0x</code>\n'
        f'<b>💎 Отгадано кристалов:</b> <code>0 шт.</code>\n\n'
        f'<b>🔥 Сумма выигрыша:</b> <code>0 ₽</code>\n', reply_markup=generate_field(field))


@dp.callback_query_handler(lambda m: len(m.data.split()) == 3, state=BombsState.field)
async def game(call: types.CallbackQuery, state: FSMContext):
    index = call.data.split()[1]

    if (not index.isnumeric()) or (not index.isascii()) or (not (0 < int(index) < 26)):
        return

    data = await state.get_data()

    field = data.get('field')
    rate = data.get('rate')
    count = data.get('count')

    cell = field[int(index)]

    if int(cell) == 0:
        field[int(index)] = 2
        await state.update_data(field=field)
        prize = calculate_ratio(count, field.count(2)) * Decimal(str(rate))

        await call.message.edit_text(
            '<b>👾 Игра - Минёр</b>\n\n'
            '➖➖➖➖➖➖➖\n'
            f'<b>💸 Ставка:</b> <code>{format_int(rate)} ₽</code>\n'
            f'<b>💣 Кол-во мин:</b> <code>{count} шт.</code>\n'
            '➖➖➖➖➖➖➖\n'
            f'<b>💰 Множитель:</b> <code>{calculate_ratio(count, field.count(2))}x</code>\n'
            f'<b>💎 Отгадано кристалов:</b> <code>{field.count(2)} шт.</code>\n\n'
            f'<b>🔥 Сумма выигрыша:</b> <code>{format_int(prize)} ₽</code>\n', reply_markup=generate_field(field))

    if int(cell) == 1:
        await state.finish()

        field[int(index)] = 3

        balance = get_user(call.from_user.id).balance

        await call.message.edit_text(
            '<b>👾 Игра - Минёр</b>\n\n'
            '➖➖➖➖➖➖➖\n'
            f'<b>💸 Ставка:</b> <code>{format_int(rate)} ₽</code>\n'
            f'<b>💣 Кол-во бомб:</b> <code>{count} шт.</code>\n'
            '➖➖➖➖➖➖➖\n'
            f'<b>💰 Множитель:</b> <code>{calculate_ratio(count, field.count(2))}x</code>\n'
            f'<b>💎 Отгадано кристалов:</b> <code>{field.count(2)} шт.</code>\n'
            '➖➖➖➖➖➖➖\n\n'
            f'<b>{random.choice(sad_smails)} Проигрыш, попробуй снова!</b>\n'
            f'<b>📉 Ваш баланс: <code>{format_int(balance)} ₽</code></b>', reply_markup=generate_field(field, finish=True))

        await call.message.answer('💣')

@dp.callback_query_handler(lambda m: m.data == 'Мины приз', state=BombsState.field)
async def game(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()

    field = data.get('field')
    count = data.get('count')
    rate = data.get('rate')

    ratio = calculate_ratio(count, field.count(2))

    if ratio == 0:
        await call.answer('❌ Нельзя забрать деньги когда множитель равен нулю (0x)', show_alert=True)
        return

    await state.finish()

    prize = ratio * Decimal(str(rate))

    deposite_user_balance(call.from_user.id, prize)

    balance = get_user(call.from_user.id).balance

    await call.message.edit_text(
            '<b>👾 Игра - Минёр</b>\n\n'
            '➖➖➖➖➖➖➖\n'
            f'<b>💸 Ставка:</b> <code>{format_int(rate)} ₽</code>\n'
            f'<b>💣 Кол-во бомб:</b> <code>{count} шт.</code>\n'
            '➖➖➖➖➖➖➖\n'
            f'<b>💰 Множитель:</b> <code>{calculate_ratio(count, field.count(2))}x</code>\n'
            f'<b>💎 Отгадано кристалов:</b> <code>{field.count(2)} шт.</code>\n'
            '➖➖➖➖➖➖➖\n\n'
            f'<b>{random.choice(right_smails)} Вы успешно забрали деньги, <code>+{format_int(prize)} ₽ ({ratio}x)</code></b>\n'
            f'📈 <b>Ваш обновленный баланс: <code>{format_int(balance)} ₽</code></b>', reply_markup=generate_field(field, finish=True)
    )

    await call.message.answer('💎')

    
    
