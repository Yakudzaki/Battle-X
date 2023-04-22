from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from loguru import logger

@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет! 👋\n'
        '🤖 Я бот-магазин для заработка! Заработай деньги играя в игры.\n'
        '📌 Что бы попасть в главное меню со всеми играми и т.д возпользуйтесь командой /menu.\n'
        '💰 Пополнить счет можно через Яндекс.кассу, Сбербанк или Qiwi.\n'
        '❓ Возникли вопросы? Не проблема! Команда /sos поможет связаться с админами, которые постараются как можно быстрее откликнуться.\n\n\n'
        '🤝 Заказать похожего бота? Свяжитесь с разработчиком <a href="https://t.me/Yakudza_Drill">Four</a>')