from aiogram.types import ContentType
from loader import dp
from utils.db_api.db import update_db
import aiogram.utils.markdown as fmt


@dp.message_handler(content_types=ContentType.TEXT)
async def text(message):
    await update_db(dp=dp, message=message)

    if "слава україні" in message.text.lower():
        await message.reply(f'Героям слава!', disable_notification=True)

    if "слава нації" in message.text.lower():
        await message.reply(f'Смерть ворогам!', disable_notification=True)

    if message.text == 'путін':
        await message.reply(f'Х{fmt.hspoiler("##л#")}!\n(самі розумієте, матюки це погано:( ', disable_notification=True)

    if message.text == 'Путін':
        await message.reply(f'Х{fmt.hspoiler("##л#")}!\n(самі розумієте, матюки це погано:( ', disable_notification=True)
