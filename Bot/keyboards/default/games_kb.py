from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

games = ReplyKeyboardMarkup(row_width=2,
    keyboard=[
        [
            KeyboardButton(text='Минёр 💣'),
            KeyboardButton(text='Трейд 📊'),
            KeyboardButton(text='Монетка 💱'),
            KeyboardButton(text='Классик 🎫'),
            KeyboardButton(text='Dice ↕️'),
            KeyboardButton(text='Кости 🎲')
            KeyboardButton(text='Дэуль 🔫')
        ],
    ], input_field_placeholder='Выберите игру', resize_keyboard=True, one_time_keyboard=True
)
