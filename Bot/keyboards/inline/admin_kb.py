from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_adm = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Статистика 📊', callback_data='Adm stat'),
            InlineKeyboardButton(text='Рассылка 📢', callback_data='Adm mail'),
            InlineKeyboardButton(text='Промокоды 📦', callback_data='Adm prom')
        ],
        [
            InlineKeyboardButton(text='Управление юзерами ❗️', callback_data='Adm users'),
            InlineKeyboardButton(text='Репорты ⚠️', callback_data='Adm rep'),
            
        ]
    ]
    )