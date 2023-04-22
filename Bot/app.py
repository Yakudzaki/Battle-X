import os
import handlers
from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import config
from loader import dp, bot
import filters
from loguru import logger
from utils.db.db_utils import *

if __name__ == '__main__':
    print(get_user(1644643904).balance)
    deposite_user_balance(1644643904, 10000)
    print(get_user(1644643904).balance)
    logger.info('Bot is started!')
    executor.start_polling(dp, skip_updates=True)
    logger.info('Bot shuts dowm!')
