import os
import asyncio
import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from bot.commands.bot_commands import bot_commands
from commands import register_user_commands

load_dotenv()
TOKEN = os.getenv("KEY")

async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    dp = Dispatcher()
    bot = Bot(TOKEN)
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')

