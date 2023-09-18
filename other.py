from aiogram import types, Dispatcher


#@dp.message_handler()
async def echo_send(message: types.message):

    if message.text == 'Привет':

        await message.answer('Приветствую тебя, друг мой!')
    else:
        await message.answer('Поздоровайся сначала')

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)