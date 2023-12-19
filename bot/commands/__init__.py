__all__ = ['start', 'bot_commands']

from aiogram import Router
from aiogram.filters import Command
from aiogram.filters import CommandStart

from bot.commands.help import help_command
from bot.commands.start import start

bot_commands = (
    ('start', 'короткое описание команды старт', 'полное описание команды старт'),
    ('help', 'короткое описание команды help', 'полное описание команды help'),
)

def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart)
    router.message.register(help_command, Command(commands=['help']))
