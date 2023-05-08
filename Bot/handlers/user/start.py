from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from loguru import logger
from utils.db.db_utils import create_user, user_exists
from utils.generate_bu_id import generate_id
from keyboards.default.keyboard import markup


# Сработает если юзера нет в бд
@dp.message_handler(lambda m: user_exists(m.from_user.id) is False)
async def start(message: types.Message):
    user_id = message.from_user.id
    bu_id = generate_id()
    create_user(user_id, bu_id)
    await message.answer(
        'Приветик! 👋\n\n'
        '🤖 Я - бот для заработка! Играя в игры, ты можешь заработать деньги.\n\n'

        '💰 Чтобы пополнить свой счет, можешь воспользоваться Яндекс.кассой, Сбербанком или Qiwi.\n\n'
        '❓ Есть вопросы? Не беда! Задавай их командой /report (текст сообщения) и администраторы обязательно ответят тебе как можно быстрее.\n\n'
        '🤔 Не знаешь, как пользоваться ботом? Напиши /help и я подскажу тебе, как начать!\n\n'
        '🤝 А еще, если хочешь заказать похожего бота, свяжись с <a href="https://t.me/Yakudza_Drill">Yakudza</a> или <a href="https://t.me/x_FouR_x">Four</a>', disable_web_page_preview=True, reply_markup=markup)


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer(
        f'Приветик! {message.from_user.first_name} 👋\n\n'
        '🤖 Я - бот для заработка! Играя в игры, ты можешь заработать деньги.\n\n'
        '💰 Чтобы пополнить свой счет, можешь воспользоваться Яндекс.кассой, Сбербанком или Qiwi.\n\n'
        '❓ Есть вопросы? Не беда! Задавай их командой /report (текст сообщения) и администраторы обязательно ответят тебе как можно быстрее.\n\n'
        '🤔 Не знаешь, как пользоваться ботом? Напиши /help и я подскажу тебе, как начать!'
        '🤝 А еще, если хочешь заказать похожего бота, свяжись с <a href="https://t.me/Yakudza_Drill">Yakudza</a> или <a href="https://t.me/x_FouR_x">Four</a>', disable_web_page_preview=True, reply_markup=markup)
