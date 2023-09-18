from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from dataBase import sqlite_db


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):

    try:
        await bot.send_message(message.from_user.id, 'Я помогу тебе найти весь необходимый материал, для изучения проблемной темы.', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: @GubzikBot')


async def close_window(message:types.Message):
    await bot.send_message(message.from_user.id, 'Хорошо, я закрою', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['Библиотека'])
async def bender_drink_command(message: types.Message):
    await sqlite_db.sql_read(message)

@dp.message_handler(commands=['Регистрация'])


def register_handlers_client(dp: Dispatcher):
    from create_bot import dp
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(bender_drink_command, commands=['Библиотека'])
    dp.register_message_handler(close_window, commands=['Закрыть'])
