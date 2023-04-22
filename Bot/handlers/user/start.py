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
    await message.answer('Привет! 👋\n'
        '🤖 Я бот-магазин для заработка! Заработай деньги играя в игры.\n'
        '📌 Что бы попасть в главное меню со всеми играми и т.д возпользуйтесь командой /menu.\n'
        '💰 Пополнить счет можно через Яндекс.кассу, Сбербанк или Qiwi.\n'
        '❓ Возникли вопросы? Не проблема! Команда /report(Сообщение) поможет связаться с админами, которые постараются как можно быстрее откликнуться.\n\n\n'
        '🤝 Заказать похожего бота? Свяжитесь с одним из разработчиков <a href="https://t.me/Yakudza_Drill">Yakudza</a> или <a href="">x-FouR-x</a>')


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет! 👋\n'
        '🤖 Я бот-магазин для заработка! Заработай деньги играя в игры.\n'
        '📌 Что бы попасть в главное меню со всеми играми и т.д возпользуйтесь командой /menu.\n'
        '💰 Пополнить счет можно через Яндекс.кассу, Сбербанк или Qiwi.\n'
        '❓ Возникли вопросы? Не проблема! Команда /report(Сообщение) поможет связаться с админами, которые постараются как можно быстрее откликнуться.\n\n\n'
        '🤝 Заказать похожего бота? Свяжитесь с разработчиком <a href="https://t.me/Yakudza_Drill">Yakudza</a>')