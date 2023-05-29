import logging

from aiogram import Bot, Dispatcher, executor, types

from btn import *

logging.basicConfig(level=logging.INFO)

BOT_THOKEN = '6084780027:AAHKczacgJgBbRs3ZPxYJLatdslFR5M3tkI'
bot = Bot(token=BOT_THOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot)

@dp.message_handler()
async def echo(message: types.Message):
        text = message.text
    
        btn = await choice_btn(text)

        photo = types.InputFile("qrcode.png")

        await message.answer_photo( caption="this is URL", photo=photo)

if __name__ == '__main__':
    executor.start_polling(dp)