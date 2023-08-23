# импорты aiogram
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup


async def set_flat_types_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text='Квартира-студия'),
             KeyboardButton(text='1-к. квартира')],

            [KeyboardButton(text='2-к. квартира'),
             KeyboardButton(text='3-к. квартира')],

            [KeyboardButton(text='Все')]
        ],
        resize_keyboard=True
    )

    return markup