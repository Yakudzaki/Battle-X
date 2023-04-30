from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from loader import dp



markup = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('👾 Игры'),
        KeyboardButton('🔐 Профиль')
    ],
    [
        KeyboardButton('🛒 Пополнить'),
        KeyboardButton('👥 Рефералы')
    ]
], resize_keyboard=True)



@dp.message_handler(text='👾 Игры')
async def games_handler(message: Message):
    await message.answer('Вы нажали на кнопку "👾 Игры"')



@dp.message_handler(text='🔐 Профиль')
async def profile_handler(message: Message):
    await message.answer('Вы нажали на кнопку "🔐 Профиль"')



@dp.message_handler(text='🛒 Пополнить')
async def recharge_handler(message: Message):
    await message.answer('Вы нажали на кнопку "🛒 Пополнить"')



@dp.message_handler(text='👥 Рефералы')
async def referrals_handler(message: Message):
    await message.answer('Вы нажали на кнопку "👥 Рефералы"')


