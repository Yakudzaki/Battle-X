from loader import dp, bot
from aiogram import types
from keyboards.inline.topup_kb import topup_btns


@dp.callback_query_handler(text='topup')
async def topup (call: types.CallbackQuery):
    await call.message.edit_text('💳 Выберите способ пополнения:️\n\n'
                                 '📥 Для пополнения с помощью других способов обращайтесь к администратору @pegasusfg', reply_markup=topup_btns)