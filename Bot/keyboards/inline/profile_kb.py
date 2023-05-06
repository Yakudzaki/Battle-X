from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

games = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='📤 Вывод', callback_data='withdraw'),
            InlineKeyboardButton(text='💳 Пополнить', callback_data='topup')
        ],
    ]
)
