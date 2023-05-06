from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import CommandHelp
from loguru import logger
from utils.db.db_utils import create_user, user_exists


@dp.message_handler(CommandHelp())
async def help(message: types.Message):
    user_id = message.from_user.id
    await message.answer('⚙️ Вот список команд, которые вы можете использовать:'
    
                         '/start - Запустить бота.'
    
                         '/help - Вызвать это сообщение.'
    
                         '/menu - Показать главное меню со всеми играми и прочим.'

                         '/games - Показать список доступных игр.'

                         '/donate - Пополнить баланс.'

                         '/profile - Показать информацию об аккаунте.'

                         '❓ Если у вас возникли вопросы, воспользуйтесь командой /report (Сообщение), чтобы связаться с администраторами бота.')

