from shedulers import scheduler

from loader import dp, bot
from aiogram import types
from loguru import logger
from utils.db.db_utils import get_user

@dp.message_handler(text='📒 Профиль')
async def profile_handler(message: types.Message):
    user = get_user(message.from_user.id)
    await message.answer()