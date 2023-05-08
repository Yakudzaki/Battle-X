from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

stavka_kb = InlineKeyboardMarkup(row_width=2,

    inline_keyboard=[

        [

            InlineKeyboardButton(text='10', callback_data='stavka_10'),

            InlineKeyboardButton(text='50', callback_data='stavka_50'),

            InlineKeyboardButton(text='100', callback_data='stavka_100')

        ],

    ]

)

bombs_kb = InlineKeyboardMarkup(row_width=2,

    inline_keyboard=[

        [

            InlineKeyboardButton(text='3', callback_data='bombs_3'),

            InlineKeyboardButton(text='10', callback_data='bombs_10'),

            InlineKeyboardButton(text='24', callback_data='bombs_24')

        ],

    ]

)
