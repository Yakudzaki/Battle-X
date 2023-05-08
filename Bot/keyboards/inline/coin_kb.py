from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


coin_kb = InlineKeyboardMarkup(row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Орел', callback_data='Монетка 0'),
        ],
        [
            InlineKeyboardButton(text='Решка', callback_data='Монетка 1')
        ],
        [
            InlineKeyboardButton(text='Забрать деньги', callback_data='Монетка приз')
        ]
    ]
)
