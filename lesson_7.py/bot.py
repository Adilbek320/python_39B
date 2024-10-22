from aiogram import types,Bot,Dispatcher,executor
from mybuttons import main_menu

api = '8195897242:AAEwWlyIbI7U2ZH2w6bYvIgwwndpx-Awmbg'
bot = Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    await sms.answer(text='Salem')
    
@dp.message_handler(text='Узбекистан')
async def send_weather(sms:types.Message):
    image = open(file='lesson_9/bot.png', mode='rb')
    await sms.answer_photo(
        photo=image,
        reply_markup=main_menu
    )


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)