import os
import handlers
from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import config
from loader import dp, bot
import filters
import logging


user_message = 'Пользователь'
admin_message = 'Админ'


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row(user_message, admin_message)

    await message.answer('''Привет! 👋

🤖 Я бот-магазин для заработка! Заработай деньги играя в игры.
    
📌 Что бы попасть в главное меню со всеми играми и т.д возпользуйтесь командой /menu.

💰 Пополнить счет можно через Яндекс.кассу, Сбербанк или Qiwi.

❓ Возникли вопросы? Не проблема! Команда /sos поможет связаться с админами, которые постараются как можно быстрее откликнуться.

🤝 Заказать похожего бота? Свяжитесь с разработчиком <a href="https://t.me/Yakudza_Drill">Four</a>''', reply_markup=markup)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
