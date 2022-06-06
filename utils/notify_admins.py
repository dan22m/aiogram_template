from email import message
import logging
from aiogram_broadcaster import TextBroadcaster
from aiogram import Dispatcher

from data.config import ADMINS, errors_chat_id


async def on_startup_notify(dp: Dispatcher):
    try:
        await TextBroadcaster(ADMINS, f"Bot started!").run()
    except Exception as err:
        logging.exception(err)
        await TextBroadcaster(errors_chat_id, f'Виникла помилка при запуску\n\n{err}').run()
