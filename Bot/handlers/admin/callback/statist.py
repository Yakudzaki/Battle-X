from loader import dp, bot
from aiogram import types
from filters.admin_only import IsAdminCb
from utils.db.db_utils import *

@dp.callback_query_handler(lambda call: call.data.endswith('stat'), IsAdminCb())
async def admin_statistick(call: types.CallbackQuery):
    users_in_bot = get_count_users()
    balance_all_users = get_all_balance()
    await call.message.edit_text(
        'Статистика 📊\n\n'
        f'Всего юзеров в боте - <code>{users_in_bot}</code>\n'
        f'Общий баланс у все юзеров - <code>{balance_all_users}</code>'
    )