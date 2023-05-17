import shedulers, handlers

from aiogram import executor
from loader import dp, bot
from loguru import logger
from utils.db.db_utils import *
from utils.notify_admins import on_startup


if __name__ == '__main__':
    logger.info('Bot is started!')
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    logger.info('Bot shuts dowm!')
