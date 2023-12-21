import os
import asyncio
import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from sqlalchemy import URL

from bot.commands.bot_commands import bot_commands
from commands import register_user_commands

from db import BaseModel, create_async_engine, get_session_maker, proceed_schemas

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

    postgres_url = URL.create(
        'postgresql+asyncpg', # indicates which database we are using, then which driver
        username=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        host='localhost',
        database=os.getenv('DB_NAME'),
        port=5432
    )

    # create a connection to the database with data from the variable
    async_engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)
    await proceed_schemas(async_engine, BaseModel.metadata)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')

