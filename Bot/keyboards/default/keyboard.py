from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


markup = ReplyKeyboardMarkup(resize_keyboard=True)
games_btn = KeyboardButton('👾 Игры')
profile_btn = KeyboardButton('🔐 Профиль')
recharge_btn = KeyboardButton('🛒 Пополнить')
referrals_btn = KeyboardButton('👥 Рефералы')

markup.add(games_btn, profile_btn, recharge_btn, referrals_btn)
