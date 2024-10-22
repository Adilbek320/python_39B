from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

uz = KeyboardButton(text='Узбекистан')
kz = KeyboardButton(text='Казахстан')
ru = KeyboardButton(text='Россия')

main_menu.add(uz,kz)
main_menu.add(ru)