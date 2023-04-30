from loader import dp, bot
from data.config import ADMINS
from .gen_field import generate_field

field = [
    0, 1, 1, 1, 2,
    1, 0, 2, 2, 0,
    1, 1, 0, 0, 2,
    2, 1, 0, 0, 1,
    0, 0, 1, 2, 0
]


async def on_startup(dp):
    for admin in ADMINS:
        await dp.bot.send_message(admin, 'Бот был запущен')
        await dp.bot.send_message(admin, 'Тест', reply_markup=generate_field(field))