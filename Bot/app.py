import os
import handlers
from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import config
from loader import dp, bot
import filters
from loguru import logger
from utils.db.db_utils import *
import aioredis
from aiogram.dispatcher.storage import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2



async def main():
    # Создаем подключение к Redis
    redis = await aioredis.create_redis_pool('redis://localhost')

    # Создаем объект RedisStorage2
    storage = RedisStorage2(redis)

    # Создаем объект Dispatcher с использованием MemoryStorage и RedisStorage2
    dp = Dispatcher(bot, storage=storage)

    # Запускаем бота
    await executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    print(get_user(1644643904).balance)
    deposite_user_balance(1644643904, 10000)
    print(get_user(1644643904).balance)
    logger.info('Bot is started!')
    main()
    logger.info('Bot shuts dowm!')
