import random

from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from loguru import logger
from utils.db.db_utils import get_user, withdraw_user_balance, deposite_user_balance
from states import CoinState
from keyboards.inline.coin_kb import coin_kb
from aiogram.dispatcher import FSMContext

@dp.message_handler(Command('coin'))
async def coin(message: types.Message):
    await CoinState.rate.set()
    
    await message.answer('<b>Введите ставку</b>')
    
@dp.message_handler(Text('Монетка 💱'))
async def coin(message: types.Message):
    await CoinState.rate.set()
    
    await message.answer('<b>Введите ставку</b>')

    
@dp.message_handler(state=CoinState.rate)
async def coin(message: types.Message, state: FSMContext):
    rate = message.text
    user_id = message.from_user.id

    if not rate.isdigit():
        await message.answer('<b>Введите число</b>')
        return
    elif 5 < int(rate) > 1000:
        await message.answer(
            'Ой! Выберите ставку в соответствии с ограничениями\n'
            '(Минимальная сумма - 5 ₽, максимальная - 1000 ₽)')
        return
    elif get_user(message.from_user.id).balance < int(rate):
        await message.answer('У вас недостаточно средств')
        return
    withdraw_user_balance(int(user_id), int(rate))
    await state.update_data(rate=int(rate), count=0)

    await CoinState.next()

    await message.answer(
        '🪙 Монетка\n\n'
        '➖➖➖➖➖➖➖\n'
        f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
        '<b>Кол-во угаданно:</b> <code>0 раз</code>\n'
        '➖➖➖➖➖➖➖\n'
        '<b>Множитель:</b> <code>0x</code>\n'
        '<b>Итоговый приз:</b> <code>0 ₽</code>', reply_markup=coin_kb)

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
                '🪙 Монетка\n\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
                f'<b>Кол-во угаданно:</b> <code>{count} раз</code>\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>Множитель:</b> <code>{count * 0.5}x</code>\n'
                f'<b>Итоговый приз:</b> <code>{rate * (count * 0.5)} ₽</code>\n\n'
                '<b>Правильно! Это был орел</b>', reply_markup=coin_kb)
        else:
            await state.finish()
            await call.message.edit_text(
                '🪙 Монетка\n\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
                f'<b>Кол-во угаданно:</b> <code>{count} раз</code>\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>Множитель:</b> <code>{count * 0.5}x</code>\n\n'
                '<b>Не удача! Это была решка</b>', reply_markup=coin_kb
            )
    else:
        if sign == random_sign:
            count += 1
            await state.update_data(count=count)
            await call.message.edit_text(
                '🪙 Монетка\n\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
                f'<b>Кол-во угаданно:</b> <code>{count} раз</code>\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>Множитель:</b> <code>{count * 0.5}</code>\n'
                f'<b>Итоговый приз:</b> <code>{rate * (count * 0.5)}x ₽</code>\n\n'
                '<b>Правильно! Это была решка</b>', reply_markup=coin_kb)
            await state.update_data(count=count)
        else:
            await state.finish()
            await call.message.edit_text(
                '🪙 Монетка\n\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>💸 Ставка:</b> <code>{rate} ₽</code>\n'
                f'<b>Кол-во угаданно:</b> <code>{count} раз</code>\n'
                '➖➖➖➖➖➖➖\n'
                f'<b>Множитель:</b> <code>{count * 0.5}x</code>\n\n'

                '<b>Не удача! Это был орел</b>', reply_markup=coin_kb)

@dp.callback_query_handler(
    lambda m: m.data == 'Монетка приз', 
    state=CoinState.count_guess)
async def coin(call: types.CallbackQuery, state=FSMContext):
    data = await state.get_data()
    rate = data.get('rate')
    count = data.get('count')
    deposite_user_balance(call.from_user.id, rate * (count * 0.5))
    await call.message.answer(f'Вы успешно забрали приз, +{rate * (count * 0.5)} ₽')
