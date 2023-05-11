from aiogram.types import
InlineKeyboardMarkup, InlineKeyboardButton 


topup_btns = InlineKeyboardMarkup(row_width=1, 
     inline_keyboard=[ 
         [ 
             InlineKeyboardButton(text='🥝 Qiwi', callback_data='topup_qiwi')
         ],

         [
             InlineKeyboardButton(text='🅿️ Payeer', callback_data='topup_payeer')
         ],
         [
             InlineKeyboardButton(text='💎 TON', callback_data='topup_ton') 
         ]
     ] 
 )