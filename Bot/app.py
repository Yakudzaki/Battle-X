from aiogram import executor, types
from data import config
from loader import dp, bot
from loguru import logger
from utils.db.db_utils import *



if __name__ == '__main__':
    logger.info('Bot is started!')
    executor.start_polling(dp, skip_updates=True)
    logger.info('Bot shuts dowm!')
