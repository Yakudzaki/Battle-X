from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def play_rate(smile: str) -> InlineKeyboardMarkup:
    price_list: list = [5, 10, 100]
    markup = [list()]

    for price in price_list:
        markup[0].append(InlineKeyboardButton(f'{price} ₽ {smile}', callback_data=f'Rate {price}'))
    
    

    return InlineKeyboardMarkup(row_width=2, inline_keyboard=markup)

