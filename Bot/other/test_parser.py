import time

# оптимизированный драйвер для Selenium, который не активирует сервисы защиты от ботов
import undetected_chromedriver as uc

# selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class AvitoFlatParser:
    def __init__(self, url: str, keywords: list = None, price_from: int = None, price_to: int = None, commission: bool = True):
        """
        :param url: всегда передается url страницы авито с арендой недвижимости на длительный срок отсортированной по дате
        :param keywords: список с типом квартир которые надо искать (Квартира-студия, 1-к. квартира, 2-к. квартира и тд.) до 3-к включительно
        :param price_from: начальная цена обьявлений
        :param price_to: конечная цена обьявлений
        :param commission: показывать ли квартиры с коммисией
        """
        self.url = url
        self.keywords = keywords
        self.price_from = price_from
        self.price_to = price_to
        self.commission = commission

    def __set_up(self):
        """ Установка опций и объявление драйвера """
        options = Options()
        # передаем настройку чтобы UI браузера не отображалось
        # options.add_argument('--headless=new')
        # Отключить использование GPU
        options.add_argument("--disable-gpu")
        # Отключение общей памяти (уменьшает использование RAM)
        options.add_argument("--disable-dev-shm-usage")
        # # Запуск в одном процессе
        options.add_argument("--single-process")

        self.driver = uc.Chrome(options=options)

    def __get_url(self):
        """ Запуск браузера """
        self.driver.get(self.url)

    def __get_filters(self):
        """ Функция определяет с какими параметрами искать квартиры """

        if self.keywords:
            if 'Квартира-студия' in self.keywords:
                self.driver.find_element(By.XPATH, "//label[@data-marker='params[550](5702)/text']").click()
                print('клик на студию')
            if '1-к. квартира' in self.keywords:
                self.driver.find_element(By.XPATH, "//label[@data-marker='params[550](5703)/text']").click()
                print('клик на 1-к')
            if '2-к. квартира' in self.keywords:
                self.driver.find_element(By.XPATH, "//label[@data-marker='params[550](5704)/text']").click()
                print('клик на 2-к')
            if '3-к. квартира' in self.keywords:
                self.driver.find_element(By.XPATH, "//label[@data-marker='params[550](5705)/text']").click()
                print('клик на 3-к')

        if self.price_from:
            elem = self.driver.find_element(By.XPATH, "//input[@data-marker='price-from/input']")
            # ввод цены по одному символу
            [elem.send_keys(num) for num in str(self.price_from)]
            print(f'ввод цены от {self.price_from}')
        if self.price_to:
            elem = self.driver.find_element(By.XPATH, "//input[@data-marker='price-to/input']")
            # ввод цены по одному символу
            [elem.send_keys(num) for num in str(self.price_to)]
            print(f'ввод цены до {self.price_to}')

        if not self.commission:
            self.driver.find_element(By.XPATH, "//label[@data-marker='params[122383](1)/text']").click()
            print('клик на "без комиссии"')

        # клик на поиск по заданным фильтрам
        self.driver.find_element(By.CSS_SELECTOR, "[data-marker='search-filters/submit-button']").click()

        return True

    def __parse_page(self):
        """ Парсит все квартиры на текущей странице """

        self.driver.refresh()

        items = self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='item-title']")

        res = []
        for item in items:
            link = item.get_attribute('href')
            res.append(link)

        return res

    def set_config(self):
        self.__set_up()
        self.__get_url()
        return self.__get_filters()

    def start_parse(self):
        return self.__parse_page()


# ТЕСТ
# для теста раскомментировать этот блок кода и запустить main.py

parser = AvitoFlatParser(
        'https://www.avito.ru/sankt_peterburg_i_lo/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKipNKspMTizJLwrPTElPLVGyrgUEAAD__95qJPwtAAAA&s=104',
        keywords=['Все'],
        price_from=30000,
        price_to=40000,
        commission=True)

parser.set_config()
print(*parser.start_parse(), sep='\n\n')


