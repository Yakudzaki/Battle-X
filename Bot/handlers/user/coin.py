import random

from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from loguru import logger
from utils.db.db_utils import get_user, withdraw_user_balance, deposite_user_balance
from states import CoinState
from keyboards.inline.coin_kb import coin_kb
from aiogram.dispatcher import FSMContext
import random


sad_smails = ['😟', '😢', '😥', '😕', '😪', '😿', '🙁', '☹️', '😓']
right_smails = ['🎉', '✅', '🥇', '👏', '👍', '🎊', '🥳', '🍾', '👑', '👌']

@dp.message_handler(Command('coin'))
async def coin(message: types.Message):
    await CoinState.rate.set()
    
    await message.answer('<b>💰 Введите сумму ставки</b>')
    
@dp.message_handler(Text('Монетка 🪙'))
async def coin(message: types.Message):
    await CoinState.rate.set()
    
    await message.answer('<b>💰 Введите сумму ставки</b>')

    
@dp.message_handler(state=CoinState.rate)
async def coin(message: types.Message, state: FSMContext):
    rate = message.text
    user_id = message.from_user.id

    if not rate.isdigit():
        await message.answer('<b>⚠️ Введите число!</b>')
        return
    elif 5 < int(rate) > 1000:
        await message.answer('Введите сумму соблюдая ограничения\n'
                             '(От 5 до 1000 ₽)')
        return
    elif get_user(message.from_user.id).balance < int(rate):

        await message.answer(f'{random.choice(sad_smails)} <b>У вас недостаточно средств</b>!')
        return
    withdraw_user_balance(int(user_id), int(rate))
    await state.update_data(rate=int(rate), count=0)

    await CoinState.next()

    await message.answer(
        '<i>👾 Игра - Монетка</i>\n\n'
        '➖➖➖➖➖➖➖\n'
        f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
        '<b>👀 Угаданно:</b> <code>0 раз</code>\n'
        '➖➖➖➖➖➖➖\n'
        '<b>📈 Множитель:</b> <code>0x</code>\n'
        '<b>🔥 Выйгрыш:</b> <code>0 ₽</code>', reply_markup=coin_kb)

@dp.callback_query_handler(
    lambda m: m.data.startswith('Монетка') and not m.data.endswith('приз'), 
    state=CoinState.count_guess)
async def coin(call: types.CallbackQuery, state: FSMContext):
    sign = int(call.data.split()[1])
    random_sign = random.randint(0, 1)
    
    data = await state.get_data()
    rate = data.get('rate')
    count = data.get('count')
    if sign == 0:
        if sign == random_sign:
            count += 1
            await state.update_data(count=count)
            await call.message.edit_text(
                '<i>👾 Игра - Монетка</i>\n\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
                f'<b>👀 Угаданно:</b> <code>{count} раз</code>\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>📈 Множитель:</b> <code>{count * 0.5}x</code>\n'
                f'<b>🔥 Выйгрыш:</b> <code>{rate * (count * 0.5)} ₽</code>\n\n'
                f'<b>{random.choice(right_smails)} Правильно! Это был орел!</b>', reply_markup=coin_kb)
        else:
            await state.finish()
            await call.message.edit_text(
                '<i>👾 Игра - Монетка</i>\n\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
                f'<b>👀 Угаданно:</b> <code>{count} раз</code>\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>📉 Множитель:</b> <code>{count * 0.5}x</code>\n\n'
                f'<b>{random.choice(sad_smails)} Не угадал! Это была решка</b>', reply_markup=coin_kb
            )
    else:
        if sign == random_sign:
            count += 1
            await state.update_data(count=count)
            await call.message.edit_text(
                '<i>👾 Игра - Монетка</i>\n\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
                f'<b>👀 Угаданно:</b> <code>{count} раз</code>\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>📈 Множитель:</b> <code>{count * 0.5}x </code>\n'
                f'<b>🔥 Выйгрыш:</b> <code>{rate * (count * 0.5)} ₽</code>\n\n'
                f'<b>{random.choice(right_smails)} Правильно! Это была решка</b>', reply_markup=coin_kb)
            await state.update_data(count=count)
        else:
            await state.finish()
            await call.message.edit_text(
                '<i>👾 Игра - Монетка</i>\n\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
                f'<b>👀 Угаданно:</b> <code>{count} раз</code>\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>📉 Множитель:</b> <code>{count * 0.5}x</code>\n\n'

                f'<b>{random.choice(sad_smails)} Не угадал! Это был орел</b>', reply_markup=coin_kb)

@dp.callback_query_handler(
    lambda m: m.data == 'Монетка приз', 
    state=CoinState.count_guess)
async def coin(call: types.CallbackQuery, state=FSMContext):
    data = await state.get_data()
    rate = data.get('rate')
    count = data.get('count')
    await state.finish()
    deposite_user_balance(call.from_user.id, rate * (count * 0.5))
    await call.message.answer(f'{random.choice(right_smails)} Вы успешно забрали выйгрыш, +{rate * (count * 0.5)} ₽')
