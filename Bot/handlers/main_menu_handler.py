import asyncio

import aioschedule as schedule

# файлы проекта
from other.FSMStates import SetParams
from keyboards.set_flat_filters_keyboards import set_flat_types_keyboard
from other.interval_parsing import start_parsing


# импорты aiogram
from aiogram import F
from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(F.text == 'Задать параметры')
async def set_parameters(message: Message, state: FSMContext):

    # поле нажатия на кнопку устанавливается состояние в котором бот ожидает от пользователя виды квартир
    await state.set_state(SetParams.flat_type)

    text = 'Выберите нужные типы квартир'
    markup = await set_flat_types_keyboard()

    await message.answer(text=text, reply_markup=markup)


@router.message(F.text == 'Начать парсинг')
async def start_interval_parsing(message: Message, state: FSMContext):
    """ Начало парсинга """

    # получаем объект класса для парсинга
    data = await state.get_data()

    try:
        parser = data['parser']

        # запуск парсера в определенном интервале
        schedule.every(1).to(2).minutes.do(start_parsing, message=message, parser=parser, state=state)

        # проверка на наличие задач в планировщике
        while True:
            await schedule.run_pending()
            await asyncio.sleep(1)

    except KeyError:
        text = 'Перед началом парсинга нужно задать параметры'
        await message.answer(text=text)


@router.message(F.text=='Остановить парсинг')
async def stop_interval_parsing(message: Message, state: FSMContext):
    # строка для остановки парсинга
    schedule.clear()

    text = 'Парсинг остановлен'
    await message.answer(text=text)

