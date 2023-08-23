# импорты aiogram
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup


async def main_menu_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text='Задать параметры')],

             [KeyboardButton(text='Начать парсинг'),
              KeyboardButton(text='Остановить парсинг')]
        ],
        resize_keyboard=True
    )

    return markup