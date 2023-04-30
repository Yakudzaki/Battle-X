from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from loader import dp
from utils.db.db_utils import get_user



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
