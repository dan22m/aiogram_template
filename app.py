from aiogram import executor

from loader import dp
import middlewares
import filters
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api.db import database
from data.config import skip_updates


async def on_startup(dispatcher):

    # Установка стандартних команд
    await set_default_commands(dispatcher)

    # Повідомлення про запуск
    await on_startup_notify(dispatcher)

    # Перевірка бази
    await database(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup,
                           skip_updates=skip_updates)
