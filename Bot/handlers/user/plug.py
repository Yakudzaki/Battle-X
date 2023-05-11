from aiogram import types
from loader import dp

@dp.callback_query_handler(
    lambda m: m.data == 'Plug',
    state='*')
async def plug(call: types.CallbackQuery):
    await call.answer('Кнопка не активна', show_alert=True)