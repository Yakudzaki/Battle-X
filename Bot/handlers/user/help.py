from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from loguru import logger
from utils.db.db_utils import create_user, user_exists


# Сработает если юзера нет в бд
@dp.message_handler(lambda m: user_exists(m.from_user.id) is False)
async def start(message: types.Message):
    user_id = message.from_user.id
    create_user(user_id)
    await message.answer('⚙️ Вот список команд, которые вы можете использовать:'
    
    '/start - Запустить бота.'
    
    '/help - Вызвать это сообщение.'
    
    '/menu - Показать главное меню со всеми играми и прочим.'

    '/games - Показать список доступных игр.'

    '/donate - Пополнить баланс.'

    '/profile - Показать информацию об аккаунте.'

    '❓ Если у вас возникли вопросы, воспользуйтесь командой /report (Сообщение), чтобы связаться с администраторами бота.')


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer('⚙️ Вот список команд, которые вы можете использовать:'
    
    '/start - Запустить бота.'
    
    '/help - Вызвать это сообщение.'
    
    '/menu - Показать главное меню со всеми играми и прочим.'

    '/games - Показать список доступных игр.'

    '/donate - Пополнить баланс.'

    '/profile - Показать информацию об аккаунте.'

    '❓ Если у вас возникли вопросы, воспользуйтесь командой /report (Сообщение), чтобы связаться с администраторами бота.')
