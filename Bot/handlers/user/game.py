from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default.games_kb import games

from utils.db.db_utils import get_user



@dp.message_handler(Command('game'))
async def game(message: types.Message):
    nickname = get_user(message.from_user.id).nickname
    await message.answer(f'{nickname}, выберите одну из игр', reply_markup=games)

@dp.message_handler(text='🎮 Игры')
async def game(message: types.Message):
    nickname = get_user(message.from_user.id).nickname
    await message.answer(f'{nickname}, выберите одну из игр', reply_markup=games)
