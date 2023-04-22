import os
import handlers
from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import config
from loader import dp, bot
import filters
from loguru import logger

if __name__ == '__main__':
    logger.info('Bot is started!')
    executor.start_polling(dp, skip_updates=True)
    logger.info('Bot shuts dowm!')
