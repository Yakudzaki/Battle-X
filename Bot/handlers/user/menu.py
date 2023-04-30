from loader import dp, bot
from aiogram import types
from loguru import logger
from utils.db.db_utils import get_user

@dp.message_handler(text='👾 Игры')
async def games_handler(message: types.Message):
    await message.answer('Вы нажали на кнопку "👾 Игры"')



@dp.message_handler(text='🔐 Профиль')
async def profile_handler(message: types.Message):
    user = get_user(message.from_user.id)
    time = user.created_at
    await message.answer('<b>Ваш профиль:</b>\n\n'
                        f'<b>👤 Никнейм:</b> <code>{user.nickname}</code>\n'
                        f'<b>🆔 ID:</b> <code>{user.bu_id}</code>\n'
                        f'<b>💰 Баланс:</b> <code>{user.balance} ₽</code>\n'
                        f'<b>🎮 Level:</b> <code>{user.level} lvl</code>\n'
                        f'<b>🕹️ Сыграно игр:</b> <code>{user.num_of_games} раз</code>\n'
                        f'<b>📅 Дата регистрации:</b> <code>{time.strftime("%Y-%m-%d %H:%M:%S")}</code>\n'
                        f'<b>👥 Рефералов:</b> <code>{user.referrals} шт.</code>')



@dp.message_handler(text='🛒 Пополнить')
async def recharge_handler(message: types.Message):
    await message.answer('')



@dp.message_handler(text='👥 Рефералы')
async def referrals_handler(message: types.Message):
    await message.answer('Вы нажали на кнопку "👥 Рефералы"')