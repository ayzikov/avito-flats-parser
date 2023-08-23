# файлы проекта
from keyboards.main_menu_keyboard import main_menu_keyboard

# импорты aiogram
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext


router = Router()

@router.message(Command(commands=['start', 'refresh']))
async def hello_message(message: Message, state: FSMContext):
    await state.clear()

    text = 'Приветственное сообщение'
    markup = await main_menu_keyboard()

    await message.answer(text=text, reply_markup=markup)



