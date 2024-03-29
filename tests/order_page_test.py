import allure
import pytest

from page_objects.order_page import OrderPage
from page_objects.base_page import BasePage


class TestOrderPage:
    @allure.title('Позитивный тест на оформление заказа через кнопку "Заказать" в хедере.')
    @allure.description('Тест проверяет полное оформление заказа с двумя наборами данных.')
    @pytest.mark.parametrize('name, surname, address, metro, number', [*OrderPage.personal_date])
    def test_push_order_header_btn(self, driver, name, surname, address, metro, number):

        base_page = BasePage(driver)
        order_page = OrderPage(driver)

        base_page.click_cookie_button()
        order_page.click_order_header_btn()
        order_page.filling_personal_date_action(name, surname, address, metro, number)

        text_order = order_page.check_congratulation_modal()

        assert 'Заказ оформлен' in text_order

    @allure.title('Позитивный тест на оформление заказа через кнопку "Заказать" внизу страницы.')
    @allure.description('Тест проверяет полное оформление заказа с двумя наборами данных.')
    @pytest.mark.parametrize('name, surname, address, metro, number', [*OrderPage.personal_date])
    def test_push_order_lower_btn(self, driver, name, surname, address, metro, number):

        base_page = BasePage(driver)
        order_page = OrderPage(driver)

        base_page.click_cookie_button()
        order_page.click_order_lower_btn()
        order_page.filling_personal_date_action(name, surname, address, metro, number)

        text_order = order_page.check_congratulation_modal()

        assert 'Заказ оформлен' in text_order
