import random
from time import sleep
from utils.db.db_utils import get_user
from loader import dp
from aiogram import types

from utils.generate_rate import play_rate
from states.states import FootBallState
from aiogram.dispatcher.filters import Command, Text, StateFilter
from aiogram.dispatcher import FSMContext
from data.config import football_rate, sad_smails, right_smails


@dp.message_handler(text='Футбол ⚽')
async def football(message: types.Message):
    await message.answer('💰 Введите сумму ставки\n (От 10 до 1000 ₽)', reply_markup=play_rate('⚽️'))
    await FootBallState.rate.set()

@dp.message_handler(state=FootBallState.rate)
async def football(message: types.Message, state: FSMContext):
    rate = message.text

    if (not rate.isnumeric()) or (not rate.isascii()):
        await message.answer('<b>⚠️ Введите число!</b>')
        return
    
    if get_user(message.from_user.id).balance < int(rate):
        await message.answer(f'<b>{random.choice(sad_smails)} На вашем балансе не достаточно средств!</b>')
        return
    
    await state.finish()
    
    rate = int(rate)


    msg = await message.answer_dice('⚽️')
    dice_value: int = msg.dice.value

    mult: int = football_rate.get(dice_value)

    print(mult)
    sleep(3.5)
    if mult > 1:
        await message.answer(
            'Вы выиграли\n'
            f'Ставка - {rate}\n'
            f'Множитель - {mult}')
    elif mult < 1:
        await message.answer(
            'Вы проиграли\n'
            f'Ставка - {rate}\n'
            f'Множитель - {mult}')

    

