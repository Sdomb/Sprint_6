import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.header_page import HeaderPage
from page_objects.order_page import OrderPage


class TestHeaderPage:
    @allure.title('Тест проверки перехода на другую страничку тапом по логотипу.')
    @allure.description('Проверяем в тесте что если нажать на логотип Яндекса, '
                        'в новом окне через редирект откроется главная страница Дзена.')
    def test_check_working_yandex_logo(self, driver):

        header_page = HeaderPage(driver)

        header_page.click_on_yandex_logo()
        window = driver.window_handles
        second_window_handle = window[1]
        driver.switch_to.window(second_window_handle)
        WebDriverWait(driver, 6).until(expected_conditions.url_contains('https://dzen.ru/'))
        url_new_page = driver.current_url

        assert url_new_page == 'https://dzen.ru/?yredirect=true'

    @allure.title('Тест проверки редиректа на главную страничку тапом на логотип самоката.')
    @allure.description('Проверяем что если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_check_working_scooter_logo(self, driver):

        header_page = HeaderPage(driver)
        order_page = OrderPage(driver)

        order_page.click_order_header_btn()
        order_url = driver.current_url
        header_page.click_on_scooter_logo()
        home_url = driver.current_url

        assert order_url != home_url
