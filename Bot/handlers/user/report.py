from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Command
from loguru import logger
from utils.db.db_utils import get_user
from data.config import ADMINS


@dp.message_handler(Command('report'))
async def report_handler(message: types.Message):
    if len(message.text.split()) > 1:
        cause = message.text.split()[1:]
        tg_user = message.from_user
        db_user = get_user(tg_user.id)
        
        for admin in ADMINS:
            await bot.send_message(admin, f"Пришел репорт от <a href='tg://user?id={tg_user.id}'>{tg_user.first_name}</a>!\n"
                             f'<b>BU ID</b> - <code>{db_user.bu_id}</code>\n'
                             f'<b>TG ID</b> - <code>{tg_user.id}</code>\n'
                             f'<b>MESSAGE</b> - {"".join(x + " " for x in cause)}\n')
        await message.answer('Ваше сообщение было отправлено администраторам!')
    else:
        await message.answer('<b>Введите сообщение репорта!</b>')

