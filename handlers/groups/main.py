from aiogram import types
from loader import dp
import base_text
from data import config
from utils.misc import logging
from utils.db_api.db import update_db
import sqlite3


conn = sqlite3.connect(config.db_name)
cur = conn.cursor()


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    try:
        await message.answer(base_text.start_msg)
        await update_db(dp=dp, message=message)
        await logging.logs(lcommand='/start', message=message)
    except Exception as e:
        await logging.logserror(lcommand='/start', message=message, e=e)
        await message.answer(f'виникла помилка\n\n{e}')


@dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    try:
        await message.answer(base_text.help_msg)
        await update_db(dp=dp, message=message)
        await logging.logs(lcommand='/help', message=message)
    except Exception as e:
        await logging.logserror(lcommand='/help', message=message, e=e)
        await message.answer(f'виникла помилка\n\n{e}')


@dp.message_handler(commands='bots')
async def cmd_bots(message: types.Message):
    try:
        await message.answer(base_text.bots_msg)
        await update_db(dp=dp, message=message)
        await logging.logs(lcommand='/bots', message=message)
    except Exception as e:
        await logging.logserror(lcommand='/bots', message=message, e=e)
        await message.answer(f'виникла помилка\n\n{e}')


@dp.message_handler(commands='test')
async def cmd_test(message: types.Message):
    try:
        await message.answer(base_text.test_msg)
        await update_db(dp=dp, message=message)
        await logging.logs(lcommand='/test', message=message)
    except Exception as e:
        await logging.logserror(lcommand='/test', message=message, e=e)
        await message.answer(f'виникла помилка\n\n{e}')
