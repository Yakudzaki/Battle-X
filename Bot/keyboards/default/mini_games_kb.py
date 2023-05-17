from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

mini_games = ReplyKeyboardMarkup(row_width=2,

    keyboard=[

        [

            KeyboardButton(text='Баскетбол 🏀'),

            KeyboardButton(text='Футбол ⚽')

        ],

        [

            KeyboardButton(text='Дартс 🎯'),

            KeyboardButton(text='Боулинг 🎳')

        ],

        [

            KeyboardButton(text='Слоты 🎰'),

            KeyboardButton(text='Кости 🎲')

        ],
        [
            KeyboardButton(text='Главное меню ◀')
        ]


    ], input_field_placeholder='Выберите игру', resize_keyboard=True, one_time_keyboard=True

)
