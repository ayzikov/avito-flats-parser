from aiogram.fsm.context import FSMContext

async def start_parsing(message, parser, state: FSMContext):
    '''
    Запуск парсера, получение ссылок и вывод их в чат с пользователем
    :param message: объект Message
    :param parser: объект парсера
    :return: None
    '''

    # получаем 10 ссылок
    links = parser.start_parse()[:10]

    # получаем список ссылок, которых до этого не было
    new_links = await check_links(links, state)

    # записываем список новых (только что полученных с парсера) ссылок в состояние
    await state.update_data(links=links)

    # приводим список ссылок в красивый вид
    text = '\n\n'.join(new_links)

    # если список со ссылками не пустой, то отправляем
    if text:
        await message.answer(text=text, disable_web_page_preview=True)


async def check_links(links: list, state: FSMContext):
    '''
    на вход функции подается список со ссылками,
    она их фильрует возвращает ссылка которые еще не были отправлены пользователю
    '''

    data = await state.get_data()
    prev_links = data.get('links', list())

    new_links = [link for link in links if link not in prev_links]

    return new_links

