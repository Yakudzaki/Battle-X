from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

games = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Минное поле 💣', callback_data='Minefield'),
            InlineKeyboardButton(text='Трейд 📊', callback_data='Trade')
        ],
    ]
)