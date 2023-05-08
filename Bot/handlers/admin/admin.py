from loader import dp, bot
from aiogram import types
from filters.admin_only import IsAdmin
from loguru import logger
from keyboards.inline.admin_kb import ikb_adm
from aiogram.dispatcher.filters import Command
from states import BombsState
from aiogram.dispatcher import FSMContext


@dp.message_handler(IsAdmin(), Command('admin'))
async def admin(message: types.Message):
    await message.reply(f'{message.from_user.first_name}, добро пожаловать в админ панель!', reply_markup=ikb_adm)
