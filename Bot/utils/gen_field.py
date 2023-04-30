from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 0 - Неизвестно
# 1 - Нету
# 2 - Бомба


def generate_field(field):
    result = []
    for y in range(0, 5):
        line = []
        for x in range(1, 6):
            a = field[(y * 5 + x) - 1]
            print((y * 5 + x) - 1)
            if a == 0:
                line.append(InlineKeyboardButton(text='⬜️', callback_data=a))
            elif a == 1:
                line.append(InlineKeyboardButton(text='🟩', callback_data=a))
            else:
                line.append(InlineKeyboardButton(text='💣', callback_data=a))
        result.append(line)
    return InlineKeyboardMarkup(inline_keyboard=result)
            
