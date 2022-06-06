import sqlite3
from aiogram import types, dispatcher
from loader import dp
import base_text
from loguru import logger
from data import config
from utils.misc import logging

import aiogram.utils.markdown as fmt


conn = sqlite3.connect(config.db_name)
cur = conn.cursor()

async def database(dp):
    try:
        conn = sqlite3.connect(config.db_name)
        cur = conn.cursor()
        logger.info("Успішне підключення до бази данних sqlite3")
    except:
        logger.error("Помилка про з'єднанні з базою данних")
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS chats_list(
	                "chat_id"	INT PRIMARY KEY,
	                "chat_name"	TEXT
                    );
                    """)
        conn.commit()
    except:
        logger.error('Помилка при створенні таблиць sqlite3')


async def update_db(dp, message):
    chatt = (message.chat.id, message.chat.full_name, message.chat.full_name)
    cur.execute(
        "INSERT INTO chats_list (chat_id, chat_name) VALUES(?, ?) ON CONFLICT (chat_id) DO UPDATE SET chat_name = ?", chatt)
    conn.commit()
#
#
#
#
#
#
#
#
#
#
#


@dp.message_handler(
    commands="all"
)
async def getAllRows(message: types.Message):
    try:
        sqlite_select_query = """SELECT * from chats_list"""
        cur.execute(sqlite_select_query)
        records = cur.fetchall()
        ltnn = len(records)
        await message.answer(text=f"Всього чатів використовує бота: {ltnn} ")
    except Exception as e:
        await message.answer(f"Виникла помилка:\nERROR:{e}")



@dp.message_handler(
    commands="r",
    commands_prefix="!/*"
)
async def cmd_r(message: types.Message):
    await update_db(dp,message)
    try:
        await logging.logs(lcommand='/r', message=message)
        if message.chat.title == None:
            await dp.bot.send_message(message.chat.id,f'Чат [ <code>{fmt.quote_html(message.from_user.full_name)}</code> ] \nуспішно оновлено в базі:)')
        else:
            await dp.bot.send_message(message.chat.id,f'Чат [ <code>{fmt.quote_html(message.chat.title)}</code> ] \nуспішно оновлено в базі:)')
    except Exception as e:
        await dp.bot.send_message(message.chat.id,f'виникла помилка:\n\n{e}')
