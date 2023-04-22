from loader import dp, bot
from aiogram import types
from filters.admin_only import IsAdmin
from loguru import logger
from keyboards.inline.admin_kb import ikb_adm
from aiogram.dispatcher.filters import Command
from states import test
from aiogram.dispatcher import FSMContext


@dp.message_handler(IsAdmin(), Command('admin'))
async def admin(message: types.Message):
    await test.name.set()
    await message.reply('Администратор, приветсвую в админ панели', reply_markup=ikb_adm)

@dp.message_handler(state=test.name)
async def no_text(message: types.Message, state: FSMContext):
    await message.answer('Все работает')