from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 0 - Неизвестно
# 1 - Бомба
# 2 - Бомба
# 3 - Крестик


def generate_field(field, finish=False):
    bombs = '⬜️' if not finish else '💣'
    result = []
    if not finish:
        for y in range(0, 5):
            line = []
            for x in range(1, 6):
                a = field[(y * 5 + x) - 1]
                if a == 0:
                    line.append(InlineKeyboardButton(text='⬜️', callback_data=f'Мины {a} {(y * 5 + x) - 1}'))
                elif a == 1:
                    line.append(InlineKeyboardButton(text=bombs, callback_data=f'Мины {a} {(y * 5 + x) - 1}'))
                elif a == 2:
                    line.append(InlineKeyboardButton(text='💎', callback_data=f'Мины {a} {(y * 5 + x) - 1}'))
                else:
                    line.append(InlineKeyboardButton(text='❌', callback_data=f'Мины {a} {(y * 5 + x) - 1}'))
            result.append(line)
        result.append([InlineKeyboardButton('Забрать деньги 💸', callback_data='Мины приз')])
    else:
        for y in range(0, 5):
            line = []
            for x in range(1, 6):
                a = field[(y * 5 + x) - 1]
                if a == 0:
                    line.append(InlineKeyboardButton(text='⬜️', callback_data=f'Plug'))
                elif a == 1:
                    line.append(InlineKeyboardButton(text=bombs, callback_data=f'Plug'))
                elif a == 2:
                    line.append(InlineKeyboardButton(text='💎', callback_data=f'Plug'))
                else:
                    line.append(InlineKeyboardButton(text='❌', callback_data=f'Plug'))
            result.append(line)
        result.append([InlineKeyboardButton('Попробовать снова 🔄', callback_data='Мины заново')])
    return InlineKeyboardMarkup(inline_keyboard=result)
            
