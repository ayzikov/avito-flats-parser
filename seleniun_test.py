import time

# оптимизированный драйвер для Selenium, который не активирует сервисы защиты от ботов
import undetected_chromedriver as uc

# selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
# передаем настройку чтобы UI браузера не отображалось
# options.add_argument('--headless=new')

driver = uc.Chrome(options=options)
driver.get("https://www.avito.ru/sankt_peterburg_i_lo/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKipNKspMTizJLwrPTElPLVGyrgUEAAD__95qJPwtAAAA&s=104")


elem = driver.find_element(By.XPATH, "//label[@data-marker='search-form/suggest']").send_keys("ПРОВЕРКА")
# elem = driver.find_element(By.CSS_SELECTOR, "[data-marker='price-from'].div.span").send_keys("ПРОВЕРКА")
# elem2 = driver.find_element(By.CSS_SELECTOR, "[data-marker='category[1000005]/hasBack']").text
driver.close()
