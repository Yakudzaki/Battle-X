from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import CommandHelp, Text
from loguru import logger
from utils.db.db_utils import create_user, user_exists

from keyboards.inline.help_kb import help_adm


@dp.message_handler(Text('📚 Помощь'))
async def help_handler(message: types.Message):
    await message.answer('<b> Связь с администрацией проекта. Только в данных случаях:</b> \n\n'
                         '<b>1️⃣ Найден баг бота</b> \n'
                         '<b>2️⃣ Есть какие то предложения</b> \n'
                         '<b>3️⃣ При обращении указывать свой ID</b> \n\n'
                         '<b>📛 Запрещено писать, о выплатах!</b>', reply_markup=help_adm)

@dp.message_handler(CommandHelp())
async def help_handler(message: types.Message):
    await message.answer('<b> Связь с администрацией проекта. Только в данных случаях:</b> \n\n'
                         '<b>1️⃣ Найден баг бота</b> \n'
                         '<b>2️⃣ Есть какие то предложения</b> \n'
                         '<b>3️⃣ При обращении указывать свой ID</b> \n\n'
                         '<b>📛 Запрещено писать, о выплатах!</b>', reply_markup=help_adm)