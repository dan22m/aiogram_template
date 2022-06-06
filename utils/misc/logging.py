import logging
from loader import dp
from data import config
from loguru import logger
import aiogram.utils.markdown as fmt


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO
                    )

logger.add(config.log_file_name, format="{time}  {level}  {message}",
           level="DEBUG")


async def logs(message, lcommand):
    await dp.bot.send_message(config.log_chat_id,
                              f"[ <a href='t.me/{message.chat.username}'>{fmt.quote_html(message.chat.title)}</a> ]\n"
                              f"\U0001F464 <a href='tg://user?id={message.from_user.id}'>{fmt.quote_html(message.from_user.full_name)}</a>\n"
                              f"use {lcommand}\n\n"
                              f"user <code>#{message.from_user.id}</code> \nchat <code>#{message.chat.id}</code>",
                              disable_web_page_preview=True, disable_notification=True
                              )
    logger.info(
        f"\n---------------------------------------------------------\n"
        f"[ t.me/{message.chat.username} : {message.chat.title} ]\n"
        f"t.me/{message.from_user.username}:{message.from_user.full_name}\n"
        f"use {lcommand}\n"
        f"user #{message.from_user.id}\n"
        f"chat #{message.chat.id}"
        f"\n---------------------------------------------------------\n"
    )


async def logserror(message, lcommand, e):
    await dp.bot.send_message(config.errors_chat_id,
                              f'ERROR\n\n'
                              f"[ <a href='t.me/{message.chat.username}'>{fmt.quote_html(message.chat.title)}</a> ]\n"
                              f"\U0001F464 <a href='tg://user?id={message.from_user.id}'>{fmt.quote_html(message.from_user.full_name)}</a>\n"
                              f"use {lcommand}\n\n"
                              f"user <code>#{message.from_user.id}</code> \nchat <code>#{message.chat.id}</code>\n\n"
                              f"{e}", disable_web_page_preview=True
                              )
    logger.error(
        f"\n---------------------------------------------------------\n"
        f"ERROR\n"
        f"[ t.me/{message.chat.username} : {message.chat.title} ]\n"
        f"t.me/{message.from_user.username}:{message.from_user.full_name}\n"
        f"use {lcommand}\n"
        f"user #{message.from_user.id}\n"
        f"chat #{message.chat.id}\n\n"
        f"{e}"
        f"\n---------------------------------------------------------\n"
    )
