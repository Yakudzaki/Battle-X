from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


stavka_kb = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='💸 5 ₽', callback_data='Rate 10'),
            InlineKeyboardButton(text='💸 50 ₽', callback_data='Rate 50')
        ],
        [
            InlineKeyboardButton(text='💸 100 ₽', callback_data='Rate 100')
        ],
    ]
)

coin_kb = InlineKeyboardMarkup(row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Орел', callback_data='Монетка 0'),
        ],
        [
            InlineKeyboardButton(text='Решка', callback_data='Монетка 1')
        ],
        [
            InlineKeyboardButton(text='💸 Забрать деньги', callback_data='Монетка приз')
        ]
    ]
)
