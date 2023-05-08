from loader import dp, bot
from aiogram import types
from loguru import logger
from utils.db.db_utils import get_user
from keyboards.inline.help_kb import help_adm
from keyboards.inline.profile_kb import prof_kb


@dp.message_handler(text='📒 Профиль')
async def profile_handler(message: types.Message):
    user = get_user(message.from_user.id)
    time = user.created_at
    await message.answer('<b>Ваш профиль:</b>\n\n'
                        f'<b>👤 Никнейм:</b> <code>{user.nickname}</code>\n'
                        f'<b>🆔 ID:</b> <code>{user.bu_id}</code>\n'
                        f'<b>💰 Баланс:</b> <code>{user.balance} ₽</code>\n'
                        f'<b>🎮 Level:</b> <code>{user.level} lvl</code>\n'
                        f'<b>🕹️ Сыграно игр:</b> <code>{user.num_of_games} раз</code>\n'
                        f'<b>👥 Рефералов:</b> <code>{user.referrals} шт.</code>\n\n'
                        f'<b>📅 Дата регистрации:</b> <code>{time.strftime("%Y-%m-%d %H:%M")}</code>', reply_markup=prof_kb)







@dp.message_handler(text='👥 Рефералы')
async def referrals_handler(message: types.Message):
    user = get_user(message.from_user.id)
    await message.answer('<b>👥 Партнёрская программа 👥</b>\n\n'
                        f'<b>🔢 Ваши партнёры</b> - <code>{user.referrals}</code> \n\n'
                        f'<b>🔗 Ваша реферальная ссылка</b> - <code>https://t.me/FoYaGamesBot?start={user.bu_id}</code> \n\n'
                         '<b>🎁 Приглашайте людей и зарабатывайте!</b> \n\n'
                         '💰 Чем больше людей вы приглашаете - тем больше зарабатываете! Удачи!')



