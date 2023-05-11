from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

stavka_kb = InlineKeyboardMarkup(row_width=2,

    inline_keyboard=[

        [
            InlineKeyboardButton(text='💸 10 ₽', callback_data='Rate 10'),
            InlineKeyboardButton(text='💸 50 ₽', callback_data='Rate 50')
        ],
        [
            InlineKeyboardButton(text='💸 100 ₽', callback_data='Rate 100')
        ],

    ]

)

bombs_kb = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='3 💣', callback_data='Bombs 3'),
            InlineKeyboardButton(text='10 💣', callback_data='Bombs 10'),
            InlineKeyboardButton(text='24 💣', callback_data='Bombs 24')
        ],

    ]
)


again_rate = InlineKeyboardMarkup(
    row_width=3,
    inline_keyboard=[
        [
            InlineKeyboardButton('Оставить ставку такой-же', callback_data='Мины ставка')
        ]
    ])