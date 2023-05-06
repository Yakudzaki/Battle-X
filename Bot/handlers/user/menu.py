from loader import dp, bot
from aiogram import types
from loguru import logger
from utils.db.db_utils import get_user
from keyboard.inline.help_kb import help_adm

@dp.message_handler(text='👾 Игры')
async def games_handler(message: types.Message):
    await message.answer('Вы нажали на кнопку "👾 Игры"')



@dp.message_handler(text='🔐 Профиль')
async def profile_handler(message: types.Message):
    user = get_user(message.from_user.id)
    time = user.created_at
    await message.answer('<b>Ваш профиль:</b>\n\n'
                        f'<b>👤 <i>Никнейм:</i> </b> <code>{user.nickname}</code>\n'
                        f'<b>🆔 <i>ID:</i> </b> <code>{user.bu_id}</code>\n'
                        f'<b>💰 <i>Баланс:</i> </b> <code>{user.balance} ₽</code>\n'
                        f'<b>🎮 <i>Level:</i> </b> <code>{user.level} lvl</code>\n'
                        f'<b>🕹️ <i>Сыграно игр:</i> </b> <code>{user.num_of_games} раз</code>\n'
                        f'<b>👥 <i>Рефералов:</i> </b> <code>{user.referrals} шт.</code>\n\n'
                        f'<b>📅 <i>Дата регистрации:</i> </b> <code>{time.strftime("%Y-%m-%d %H:%M")}</code>')



@dp.message_handler(text='🛒 Пополнить')
async def recharge_handler(message: types.Message):
    await message.answer('')



@dp.message_handler(text='👥 Рефералы')
async def referrals_handler(message: types.Message):
    user = get_user(message.from_user.id)
    await message.answer('<b>👥 Партнёрская программа 👥</b>\n\n'
                        f'<b>🔢 Ваши партнёры</b> - <code>{user.referrals}</code> \n\n'
                        f'<b>🔗 Ваша реферальная ссылка</b> - <code>https://t.me/FoYaGamesBot?start={user.bu_id}</code> \n\n'
                         '<b>🎁 Приглашайте людей и зарабатывайте!</b> \n\n'
                         '<i>💰 Чем больше людей вы приглашаете - тем больше зарабатываете! Удачи!</i>')



@dp.message_handler(text='📚 Помощь')
async def help_handler(message: types.Message):
    await message.answer('<b> <i>Связь с администрацией проекта. Только в данных случаях:</i> </b> \n\n'
                         '<b>1️⃣ Найден баг бота</b> \n'
                         '<b>2️⃣ Есть какие то предложения</b> \n'
                         '<b>3️⃣ При обращении указывать свой ID</b> \n\n'
                         '<b>📛 Запрещено писать, о выплатах!</b>', reply_markup=help_adm)
