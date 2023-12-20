from aiogram.types import Message, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def start(message: Message) -> None:
    menu_builder = ReplyKeyboardBuilder()
    menu_builder.button(
        text='Помощь'
    )
    menu_builder.add(
        KeyboardButton(text='Отправить контакт', request_contact=True)
    )
    menu_builder.row(
        KeyboardButton(text='Отправить голосование', request_poll=KeyboardButtonPollType())
    )

    await message.answer(
        'Меню',
        reply_markup=menu_builder.as_markup(resize_keyboard=True)
    )