from aiogram import types

import qrcode

async def choice_btn(text): 

    qr = qrcode.QRCode(
          version=1,
          box_size=10,

          border=4,
          )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img.save("qrcode.png","png")

async def choose_hand_btn(): 
    btn = types.InlineKeyboardMarkup()
    btn.add(

        types.InlineKeyboardButton("👊", callback_data="hand:stone"),
        types.InlineKeyboardButton("🖐", callback_data="hand:paper"),
        types.InlineKeyboardButton("✌️", callback_data="hand:scissors"),
        
    )
    return btn 

