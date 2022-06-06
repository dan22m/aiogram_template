from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("dev", "Зв'язок з творцем"),
            types.BotCommand("bots", "всі боти")
        ]
    )
