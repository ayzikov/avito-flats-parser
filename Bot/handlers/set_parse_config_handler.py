# файлы проекта
from other.FSMStates import SetParams
from other.test_parser import AvitoFlatParser
from keyboards.main_menu_keyboard import main_menu_keyboard


# импорты aiogram
from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(SetParams.flat_type)
async def get_flat_types(message: Message, state: FSMContext):
    """ Состояние выбора типа квартиры """

    # записываю какие типы квартир нужно парсить
    keywords = list()

    # если пользователь ввел что-нибудь, то добавляем это
    # если же нет, то добавляем пустой список
    if message.text != 'Все':
        keywords.append(message.text)

    await state.update_data(flat_types=keywords)

    # устанавливаю след состояние
    await state.set_state(SetParams.price_from)

    text = 'Минималная цена квартир'
    await message.answer(text=text)



@router.message(SetParams.price_from)
async def get_flat_types(message: Message, state: FSMContext):
    """ Состояние выбора начальной цены """

    # записываю начальную цену
    await state.update_data(price_from=message.text)

    # устанавливаю след состояние
    await state.set_state(SetParams.price_to)

    text = 'Максимальная цена квартир'
    await message.answer(text=text)


@router.message(SetParams.price_to)
async def get_flat_types(message: Message, state: FSMContext):
    """ Состояние выбора конечной цены """

    # записываю конечную цену
    await state.update_data(price_to=message.text)

    # устанавливаю след состояние
    await state.set_state(SetParams.commission)

    text = 'Показывать ли квартиры с комиссией?'
    await message.answer(text=text)


@router.message(SetParams.commission)
async def get_flat_types(message: Message, state: FSMContext):
    """ Состояние выбора с комиссией или без """

    # сбрасываем текущее состояние пользователя
    await state.set_state(state=None)

    # записываю нужна ли комиссия
    if message.text.lower() == 'да' or 'if':
        await state.update_data(commission=True)
    else:
        await state.update_data(commission=False)

    text = ('Подождите немного\n'
            'Параметры устанавливаются...')
    await message.answer(text=text)

    # получаем данные для парсинга от пользователя (из состояния)
    data = await state.get_data()

    # создаем объект парсера
    parser = AvitoFlatParser(
        'https://www.avito.ru/sankt_peterburg_i_lo/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKipNKspMTizJLwrPTElPLVGyrgUEAAD__95qJPwtAAAA&s=104',
        keywords=data['flat_types'],
        price_from=data['price_from'],
        price_to=data['price_to'],
        commission=data['commission'])

    await state.update_data(parser=parser)

    # устанавливаем параметры для парсинга
    if parser.set_config():
        text = 'Параметры для поиска установлены'
    else:
        text = ('При установки параметров произошла ошибка\n'
                'Попробуйте позже или обратитесь к разработчику\n'
                '@Ayzikov')

    markup = await main_menu_keyboard()
    await message.answer(text=text, reply_markup=markup)
