from loader import dp, bot
from data.config import ADMINS, ADMINS_CHAT
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
        await bot.send_message(admin, '✅ Бот запущен!')
    await bot.send_message(5614722872, 'пон')
    await bot.send_message(ADMINS_CHAT[0], '✅ Бот запущен!')
