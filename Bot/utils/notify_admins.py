from loader import dp, bot
from data.config import ADMINS, ADMINS_CHAT


async def on_startup(dp):
    for admin in ADMINS:
        await bot.send_message(admin, '✅ Бот запущен!')
    await bot.send_message(ADMINS_CHAT, '✅ Бот запущен!')
