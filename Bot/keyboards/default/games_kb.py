from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

games = ReplyKeyboardMarkup(row_width=2,
    keyboard=[
        [
            KeyboardButton(text='Button Blast 💣'),
            KeyboardButton(text='Трейд 📊')
        ],
    ], input_field_placeholder='Выберите игру', resize_keyboard=True, one_time_keyboard=True
)