from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



markup = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton('👾 Игры'),
        KeyboardButton('🔐 Профиль')
    ],
    [
        KeyboardButton('🛒 Пополнить'),
        KeyboardButton('👥 Рефералы')
    ]
])