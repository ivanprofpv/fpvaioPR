from aiogram import types
from aiogram.filters import CommandObject

from bot.commands import bot_commands


async def help_command(message: types.Message, command: CommandObject):
    if command.args:
        for cmd in bot_commands:
            if cmd[1] == command.args:
                return await message.answer(
                    f'{cmd[0]} - {cmd[1]}\n\n{cmd[2]}'
                )
            else:
                return await message.answer('Команда не существует')
    return await message.answer(
        'Помощь по боту\n'
        'Для получения доп.информации о команде, используйте /help <команда>'
    )