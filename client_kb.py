from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

b1 = KeyboardButton('/Библиотека')
b2 = KeyboardButton('/Регистрация')
b4 = KeyboardButton('/Закрыть')
#b3 = KeyboardButton('Поделиться номером', request_contact=True)
#b4 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).insert(b4).add(b2)